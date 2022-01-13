## haydarctl [DEMO]

`haydarctl` checks detect and notifies the IAC state and config drifts based on the infrastructure code definitions on Terragrunt.

Let's check how it works;


At the first you have to define your organization name and list of the repositories;

Example `config/haydar.yaml` file ;

```yaml

organization: WoodProgrammer
repo_list:
  - infra_hede
```
You just set your organization name and list of the repository.

Now you have to create a token that is able to clone your repositories under the repo_list ;

```sh
    export GH_TOKEN=<YOU-SUPER-SECRET-GITHUB-TOKEN>
    python3 main.py --config <YOUR_CONFIG_FILE> --output <OUTPUT_DIRECTORY>
```

After we cloned your repositories in the list script will start to run `terragrun plan` and `refresh` command at the background and check the configurational change.

According to the plan and refresh outputs you will see what a kind of changes applied out of the your terraform code blocks.

### Notification:
haydarctl creates issues on your repository just for now and you can check the example issues under issues directory.

## TODO
- Improve terragrunt capabilities
- Multi branch support
- UI based on demand checks
- Terraform support
