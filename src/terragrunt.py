import os
import glob
import json
import logging
import subprocess
from pathlib import Path

class TerragruntUtils(object):
    def __init__(self):
        pass

    def gather_directories(self, terragrunt_root_addr="tests/haydar-terragrunt/"):
        pathname = terragrunt_root_addr + "/**/terragrunt.hcl"
        modules = glob.glob(pathname, recursive=True)

        return modules


class Terragrunt(object):
    def __init__(self, terragrunt_root_addr):
        self.utils = TerragruntUtils()
        self.modules = self.set_modules(terragrunt_root_addr)

    
    def set_modules(self, terragrunt_root_addr="tests/haydar-terragrunt/"):
        modules = self.utils.gather_directories(terragrunt_root_addr)
        return modules

    def state_checker(self, workspace): ## that is responsible to fetch states from the remote address
        
        for module in self.modules:
            module_directory = module.replace("terragrunt.hcl", "")
            splitted_module = module.split("/")
            module_name = splitted_module[splitted_module.index("terragrunt.hcl")-1]
            try:
                
                subprocess.run("terragrunt refresh -lock=false --terragrunt-working-dir {}".format(module_directory, module_directory), shell=True, check=True)
                subprocess.run("terragrunt plan -lock=false --terragrunt-working-dir {} > {}/{}plan_output ".format(module_directory, workspace,module_name), shell=True, check=True)

            except Exception as exp:
                logging.warning(exp)

    def aggregator(self, workspace): ## aggregate plan output with issue templates
        plan_map = {}
    
        for module in self.modules:
            module_directory = module.replace("terragrunt.hcl", "")
            splitted_module = module.split("/")
            module_name = splitted_module[splitted_module.index("terragrunt.hcl")-1]
            plan_output = "{}/states/{}plan_output".format(workspace, module_name)
            
            try:
                contents = Path(plan_output).read_text()
                plan_map[module] = contents
            except Exception as exp:
                logging.warning(exp)

        return plan_map
