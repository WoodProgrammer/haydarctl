import os
import sys
import yaml
import logging
import argparse
from pathlib import Path
from haydarctl.terragrunt import Terragrunt
from haydarctl.issue_generator import TerragruntIssueGenerator


def directory_handler(directory):
    full_path = os.getcwd()
    return full_path+"/"+directory

def main():

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


    directory = args.output
    workspace = args.workspace

    template_directory = directory_handler(directory)
    workspace_directory = directory_handler(workspace)



    print("Parameters {} {}".format(directory, workspace_directory))

    check_directory = Path(directory).is_dir()

    if check_directory is True:
        logging.warning("The repo check just started in this terragrunt directory {}".format(directory))
    else:
        logging.error("Directory status {}".format(check_directory))
        logging.error("Please check the directory:: {} ".format(directory))
        sys.exit(1)


    obj = Terragrunt(tg_root_addr="{}".format(workspace_directory))

    issue_obj = TerragruntIssueGenerator()
    obj.state_checker(workspace=workspace_directory)
    plan_resources = obj.aggregator(workspace=workspace_directory)

    modules = obj.modules
    print("Object modules {}".format(modules))

    for module in modules:
        try:
            plan_output = plan_resources[module]
            content = issue_obj.create_template_file(plan_output=plan_output, module_name=module)
            issue_obj.save_template_content(workspace=workspace, template_directory=template_directory, content=content)
        except Exception as exp:
            logging.error(exp)
            continue
    

    print("The output files is extracted in here Happy Terragrunting .. ")


directory_handler("fix")