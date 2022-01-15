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


parser.add_argument("--workspace",
                       action='store',
                       type=str,
                       help="The place to clone and store the repositories, plan files and states",
                       default="./haydar-workspace")

args = parser.parse_args()

def main(config_file, template_directory, workspace):

    with open(config_file, "r") as stream:
        try:
            config_values = yaml.safe_load(stream)
        except yaml.YAMLError as error:
            logging.error(exc)

    organization = config_values["organization"]
    repo_list = config_values["repo_list"]

    gh_obj = GithubUtils()

    for repo in repo_list:
        gh_obj.clone_repo("{}/{}".format(organization, repo), "{}/{}".format(workspace, repo))


    for repo in repo_list:

        obj = Terragrunt(tg_root_addr="{}/{}".format(workspace, repo))

        issue_obj = TerragruntIssueGenerator()
        obj.state_checker(workspace=workspace)
        plan_resources = obj.aggregator(workspace=workspace)

        modules = obj.modules
        print(modules)

        for module in modules:
            try:
                plan_output = plan_resources[module]
                content = issue_obj.create_template_file(repo=repo, plan_output=plan_output, module_name=module)
                issue_obj.save_template_content(template_directory=template_directory, content=content)
            except Exception as exp:
                logging.error(exp)
                continue


if __name__ == "__main__":
    config_file = args.config
    directory = args.output
    workspace = args.workspace

    check_config_file = Path(config_file).exists()
    check_directory = Path(directory).is_dir()

    if check_directory == True and check_config_file == True:
        logging.warning("The repo check just started on  the repositories are according to the {} file .. ".format(config_file))
        main(config_file=config_file, template_directory=directory, workspace=workspace)
    else:
        logging.error("File status {}".format(check_config_file))
        logging.error("Directory status {}".format(check_directory))

        logging.error("Please check the directory and file names directory:: {} file:: {} ".format(directory, config_file))
        sys.exit(1)