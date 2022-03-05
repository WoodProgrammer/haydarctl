import sys
import yaml
import logging
import argparse
from pathlib import Path
from src.terragrunt import Terragrunt
from src.issue_generator import TerragruntIssueGenerator


parser = argparse.ArgumentParser(description="Path of the configuration file")


parser.add_argument(
                       "--config",
                       action='store',
                       type=str,
                       help="the path of the configuration file",
                       default="./config/haydar.yaml")

parser.add_argument(
                       "--output",
                       action='store',
                       type=str,
                       help="the locationg of the generated template files",
                       default="./issues")


parser.add_argument(
                       "--workspace",
                       action='store',
                       type=str,
                       help="The place to clone and store the repositories, plan files and states",
                       default="./haydar-workspace")

args = parser.parse_args()


def main(template_directory, workspace):
    
    obj = Terragrunt(tg_root_addr="{}".format(workspace))

    issue_obj = TerragruntIssueGenerator()
    obj.state_checker(workspace=workspace)
    plan_resources = obj.aggregator(workspace=workspace)

    modules = obj.modules
    print("Object modules {}".format(modules))

    for module in modules:
        try:
            plan_output = plan_resources[module]
            content = issue_obj.create_template_file(plan_output=plan_output, module_name=module)
            issue_obj.save_template_content(directory=directory, template_directory=template_directory, content=content)
        except Exception as exp:
            logging.error(exp)
            continue
    

    print("The output files is extracted in here Happy Terragrunting .. ")

if __name__ == "__main__":

    directory = args.output
    workspace = args.workspace

    check_directory = Path(directory).is_dir()

    if check_directory is True:
        logging.warning("The repo check just started in this terragrunt directory {}".format(directory))
        main(template_directory=directory, workspace=workspace)

    else:
        logging.error("Directory status {}".format(check_directory))
        logging.error("Please check the directory:: {} ".format(directory))
        sys.exit(1)