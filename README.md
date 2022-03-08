<h1 align="center"> haydarctl [DEMO] </h1>


<p align="center">
  <img width="300" height="300" src="./img/logo.png"></img>
</p>


<p align="center">
The config drift checker with terragrunt states to detect manual changes on your infra out of the as-code stack.
</p>

# Why haydarctl ? 

In IAC universe we can seperate drift problem in two main part.<a href="https://github.com/snyk/driftctl/">Resource</a> and Configuration drifts.

According to the daily support cases or less privileged user access or bypassed manual changes from the terraform code blocks that can cause configurational drifts.

In this example diagram at day-0 teams create their own resource on AWS.After that some of the manual changes and non-imported resources can make your code blocks too far away from the desired state of the terraform.

To check your state and code block compability in specified time periods you can use the haydarctl.

## How it works ?

Haydarctl needs two important thing;

* python3
* terragrunt

After you installed them you can start to run it.

Haydarctl get the directory address from command line and you can run this any directory address you want.

## Installation

```sh

  git clone git@github.com:WoodProgrammer/haydarctl.git
  pip3 install --upgrade ./haydarctl

```
To verify the installation run this command

```sh
    haydarctl --help
    haydarctl --output fix --workspace infra_repository
    
        __  __                        __                          __     __
   / / / /  ____ _   __  __  ____/ /  ____ _   _____  _____  / /_   / /
  / /_/ /  / __ `/  / / / / / __  /  / __ `/  / ___/ / ___/ / __/  / /
 / __  /  / /_/ /  / /_/ / / /_/ /  / /_/ /  / /    / /__  / /_   / /
/_/ /_/   \__,_/   \__, /  \__,_/   \__,_/  /_/     \___/  \__/  /_/
                  /____/

    This tools compares Terraform state and Real Resources and it generates a output file for you
    Caveats: This tool is not stable yet and your feedbacks are very important for us please do not hesiate to create Issue&Pr on Github.
    
 
    
```

## Documentation
<a href="https://emirozbirdeveloper.medium.com/configuration-drifts-and-ha-dd55132b2132">Configuration Drifts and Haydarctl</a>
## Usage

You can check this video

haydarctl start to fetch github repositories and checks the each terragrunt modules and compares the states built-in terragrunt commands and generates drift templates.To see the examples you can check the <b>issues</b> directory.


## Respect to ; 

<i>Haydar Haydar - Neşet Ertaş</i>

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YnKI_7WY3nE/0.jpg)](https://www.youtube.com/watch?v=YnKI_7WY3nE)
