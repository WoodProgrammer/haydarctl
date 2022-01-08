import os
import glob
import json
import logging
import subprocess

class Terragrunt(object):
    def __init__(self):
        pass

    def fetch_list_of_state_files(self, terragrunt_root_addr="tests/haydar-terragrunt/"): ## function to fetch state files from remote address
        pathname = terragrunt_root_addr + "/**/terragrunt.hcl"
        modules = glob.glob(pathname, recursive=True)

        for module in modules:
            directory = module.replace("terragrunt.hcl", "")
            try:
                os.makedirs("/tmp/states/{}".format(directory), exist_ok=True)
                subprocess.run("terragrunt state pull --terragrunt-working-dir {} > /tmp/states/{}tg.tfstate".format(directory, directory), shell=True, check=True)
            except Exception as exp:
                print(exp)

    def state_checker(self): ## that is responsible to fetch states from the remote address
        pass

    def aggregator(self): ## aggregate plan output with issue templates
        pass
