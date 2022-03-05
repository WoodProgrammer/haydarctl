import glob
import unittest
from src.terragrunt import Terragrunt
from tests.utils import check_file, check_file_size

class TestTerragrunt(unittest.TestCase):

    def test_set_modules(self):
        tg_obj = Terragrunt(tg_root_addr="haydar-workspace/infra_hede")
        expected_module_value = 2
        modules = tg_obj.set_modules(tg_root_addr="haydar-workspace/infra_hede")

        self.assertEqual(len(modules), expected_module_value)

    def test_state_checker(self):
        workspace="infra_hede"
        
        tg_obj = Terragrunt(tg_root_addr="infra_hede")
        tg_obj.state_checker(workspace=workspace)

        file_status = check_file("infra_hede/infra_hede-haydar-terragrunt-development-eu-west-1-s3-terragrunt.hclplan_output")
        file_size   = check_file_size("infra_hede/infra_hede-haydar-terragrunt-development-eu-west-1-s3-terragrunt.hclplan_output")
        self.assertEqual(file_status, True)
        self.assertNotEqual(file_size, 0)