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

Let's check this example ; 

<img src="./docs/img/config-drift.png"></img>

In this example diagram at day-0 teams create their own resource on AWS.After that some of the manual changes and non-imported resources can make your code blocks too far away from the desired state of the terraform.

To check your state and code block compability in specified time periods you can use the haydarctl.

## How it works ?

Haydarctl needs two important thing;

* python3
* terragrunt

After you installed them you can start to run it.

Haydarctl get the directory address from command line and you can run this any directory address you want.

Example usage ;

```sh
  $ python3 main.py  --output drift_output_address --workspace infra_address
```

haydarctl start to fetch github repositories and checks the each terragrunt modules and compares the states built-in terragrunt commands and generates drift templates.To see the examples you can check the <b>issues</b> directory.


## Respect to ; 

<i>Haydar Haydar - Neşet Ertaş</i>

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YnKI_7WY3nE/0.jpg)](https://www.youtube.com/watch?v=YnKI_7WY3nE)


# TODO 
* pip packages
