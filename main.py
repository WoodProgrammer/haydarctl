import yaml
import logging
import argparse
from src.terragrunt import Terragrunt
from src.issue_generator import TerragruntIssueGenerator
from src.gh_utils import GithubUtils

## Terragrunt testing 

parser = argparse.ArgumentParser(description="Path of the configuration file")

# Add the arguments
parser.add_argument("--config",
                       action='store',
                       type=str,
                       help="the path of the configuration file",
                       default="./config/haydar.yaml")

args = parser.parse_args()

print(args.config)

'''
if __name__ == "__main__":


    arg_result = check_args()


    if arg_result[1] == True:
        main(args)
    else:
        logging.error(arg_result)
        exit 1
'''


def check_args():
    pass


def main(args):

    with open("config/haydar.yaml", "r") as stream:
        try:
            config_values = yaml.safe_load(stream)
        except yaml.YAMLError as error:
            logging.error(exc)

    organization = config_values["organization"]
    repo_list = config_values["repo_list"]

    gh_obj = GithubUtils()

    for repo in repo_list:
        gh_obj.clone_repo("{}/{}".format(organization, repo), "/tmp/{}".format(repo))


    for repo in repo_list:

        obj = Terragrunt(terragrunt_root_addr="/tmp/{}".format(repo))

        issue_obj = TerragruntIssueGenerator()
        obj.fetch_list_of_state_files()
        obj.state_checker()
        plan_resources = obj.aggregator()

        modules = obj.modules
        print(modules)

        for module in modules:
            try:
                plan_output = plan_resources[module]
                issue_obj.create_template_file(repo=repo, plan_output=plan_output, module_name=module)
            except Exception as exp:
                logging.error(exp)
                continue


