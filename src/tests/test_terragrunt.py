import glob
import unittest
from src.terragrunt import Terragrunt
from src.tests.utils import check_file, check_file_size

class TestTerragrunt(unittest.TestCase):

    def test_set_modules(self):
        tg_obj = Terragrunt(terragrunt_root_addr="src/tests/haydar-terragrunt")
        expected_module_value = 2
        modules = tg_obj.set_modules(terragrunt_root_addr="src/tests/haydar-terragrunt")

        self.assertEqual(len(modules), expected_module_value)

    def test_state_checker(self):
        workspace="haydar-workspace"
        
        tg_obj = Terragrunt(terragrunt_root_addr="src/tests/haydar-terragrunt")
        tg_obj.state_checker(workspace=workspace)

        file_status = check_file("haydar-workspace/s3plan_output")
        file_size   = check_file_size("haydar-workspace/s3plan_output")
        self.assertEqual(file_status, True)
        self.assertNotEqual(file_size, 0)