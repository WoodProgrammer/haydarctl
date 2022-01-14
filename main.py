import os
import sys
import yaml
import logging
import argparse
from pathlib import Path
from src.terragrunt import Terragrunt
from src.issue_generator import TerragruntIssueGenerator
from src.gh_utils import GithubUtils


parser = argparse.ArgumentParser(description="Path of the configuration file")


parser.add_argument("--config",
                       action='store',
                       type=str,
                       help="the path of the configuration file",
                       default="./config/haydar.yaml")

parser.add_argument("--output",
                       action='store',
                       type=str,
                       help="the locationg of the generated template files",
                       default="./issues")

args = parser.parse_args()

def main(config_file, template_directory):
    working_directory = os.environ.get("WORKING_DIRECTORY")
    with open(config_file, "r") as stream:
        try:
            config_values = yaml.safe_load(stream)
        except yaml.YAMLError as error:
            logging.error(exc)

    organization = config_values["organization"]
    repo_list = config_values["repo_list"]

    gh_obj = GithubUtils()

    for repo in repo_list:
        gh_obj.clone_repo(
                repo_addr="{}/{}".format(organization, repo),
                clone_to="{}/{}".format(working_directory, repo))


    for repo in repo_list:

        obj = Terragrunt(terragrunt_root_addr="{}/{}".format(working_directory, repo))

        issue_obj = TerragruntIssueGenerator()
        obj.fetch_list_of_state_files()
        obj.state_checker()
        plan_resources = obj.aggregator()

        modules = obj.modules
        print(modules)

        for module in modules:
            try:
                plan_output = plan_resources[module]
                issue_obj.create_template_file(repo=repo, plan_output=plan_output, module_name=module, template_directory=template_directory)
            except Exception as exp:
                logging.error(exp)
                continue


if __name__ == "__main__":
    config_file = args.config
    directory = args.output

    check_config_file = Path(config_file).exists()
    check_directory = Path(directory).is_dir()

    if check_directory == True and check_config_file == True:
        logging.warning("The repo check just started on  the repositories are according to the {} file .. ".format(config_file))
        main(config_file=config_file, template_directory=directory)
    else:
        logging.error("File status {}".format(check_config_file))
        logging.error("Directory status {}".format(check_directory))

        logging.error("Please check the directory and file names directory:: {} file:: {} ".format(directory, config_file))
        sys.exit(1)