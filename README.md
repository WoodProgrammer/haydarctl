## haydarctl [DEMO]


# Why haydarctl ? 

In IAC universe we can seperate drift problem in two main part.<a href="https://github.com/snyk/driftctl/">Resource</a> and Configuration drifts.According to the daily support cases or less privileged user access or bypassed manual changes from the terraform code blocks that can cause configurational drifts.

Let's check this example ; 

<img src="./docs/img/config-drift"></img>

In this example diagram at day-0 teams create their own resource on AWS.After that some of the manual changes and non-imported resources can make your code blocks too far away from the desired state of the terraform.

To check your state and code block compability in specified time periods you can use the haydarctl.

## How it works ? 
At the first you have to define your organization name and list of the repositories;

Example config/haydar.yaml file ;

```yaml
organization: WoodProgrammer
repo_list:
  - infra_hede
```

and you need to export your git account token as environment variable ; 

```sh
    export GH_TOKEN=<YOU-SUPER-SECRET-GITHUB-TOKEN>
```

Finally you can run the main.py like that ; 

```sh
    python3 main.py --config <YOUR_CONFIG_FILE> --output <OUTPUT_DIRECTORY>
```

haydarctl start to fetch github repositories and checks the each terragrunt modules and compares the states built-in terragrunt commands and generates drift templates.To see the examples you can check the <b>issues</b> directory.


## Respect to ; 

<i>Haydar Haydar - Neşet Ertaş</i>

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YnKI_7WY3nE/0.jpg)](https://www.youtube.com/watch?v=YnKI_7WY3nE)

