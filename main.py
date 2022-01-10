import logging
from src.terragrunt import Terragrunt
from src.issue_generator import TerragruntIssueGenerator

## Terragrunt testing purposes
if __name__ == "__main__":

    obj = Terragrunt(terragrunt_root_addr="/tmp/infra_hede")

    issue_obj = TerragruntIssueGenerator()
    obj.fetch_list_of_state_files()
    obj.state_checker()
    plan_resources = obj.aggregator()

    modules = obj.modules
    print(modules)

    for module in modules:
        repo = "infra_hede"
        try:
            plan_output = plan_resources[module]
            issue_obj.create_template_file(repo=repo, plan_output=plan_output, module_name=module)
        except Exception as exp:
            logging.error(exp)
            continue