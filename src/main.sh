#!/bin/bash
set -eo pipefail

export BASE_PATH=$(pwd)
export GITHUB_HOST=${GITHUB_HOST:-github.com}
export ISSUES_MESSAGE_BODY_FILE=$BASE_PATH/drift_messages

ctrlc_count=0

function handler()
{
    echo "Closing by something else .. :D"
}

trap handler SIGINT SIGTERM ERR EXIT

terragrunt_state_fetcher(){
    ## this function using for the terragrunt

    MODULES=$(find . -name "terragrunt.hcl" -exec dirname {} \; | grep -v ".terragrunt-cache" | sed 's/\.\///g' | grep '/')

    for module in $MODULES;
    do
        echo "Pulling state for $module"; \
        mkdir -p states/$module; \
        terragrunt state pull --terragrunt-working-dir $module > states/$module/tg.tfstate; \
    done
}

raw_terraform_state_checker(){
    ## this function using for the raw terraform modules

    MODULES=$(find . -name "*.tf" -exec dirname {} \; | sed 's/\.\///g'|uniq)
    for module in $MODULES;
    do

        echo "Pulling state for $module";
        mkdir -p states/$module;
        sleep 100
        pushd $module
         terraform refresh
         terraform plan > state_result_$module
         STATE_RESULT=$(cat state_result_$module |grep "Your infrastructure matches the configuration.")

         if [ -z "$STATE_RESULT" ]
         then
            echo $STATE_RESULT
            echo "There is a config drift on module $module"
            echo "Creating issue on repo ... .. "
            echo -e "The module $module contains a config drift" > ${ISSUES_MESSAGE_BODY_FILE}
         else
            echo "There is no config drift on module $module"
         fi
        popd

    done
}

create_issue_on_github(){

    if [ -e "$ISSUES_MESSAGE_BODY_FILE" ]
    then
        gh issue create --title "Config Drift Results" --body-file ${ISSUES_MESSAGE_BODY_FILE}
        rm ${ISSUES_MESSAGE_BODY_FILE}
    else
        echo "There is nothing to create issue"
    fi

}

get_repositories(){
    echo $ORGANIZATION

    if [ -z $REPO_LIST ] || [ -z $ORGANIZATION ];
    then
        echo "There is nothing to pull cause of <ORGANIZATION> or <REPO_LIST> one of is empty"
        exit 1
    else
        echo "Pulling repos under $ORGANIZATION"
        for repo in $REPO_LIST
        do
            gh repo clone "$GITHUB_HOST/$ORGANIZATION/$repo"
        done
    fi
}

#raw_terraform_state_checker
#create_issue_on_github
#get_repositories