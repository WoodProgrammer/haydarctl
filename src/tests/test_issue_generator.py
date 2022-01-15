import glob
import unittest
from src.issue_generator import *
from src.tests.utils import check_file

class TestIssueTemplateGenerator(unittest.TestCase):

    def test_template_generation(self):
        file_status = None
        sample_plan_output = """
[1m  # data.aws_iam_policy_document.elb_log_delivery[0][0m will be read during apply
  # (config refers to values not yet known)[0m[0m
[0m [36m<=[0m[0m data "aws_iam_policy_document" "elb_log_delivery"  {
      [32m+[0m [0m[1m[0mid[0m[0m   = (known after apply)
      [32m+[0m [0m[1m[0mjson[0m[0m = (known after apply)
      [32m+[0m [0mstatement {
          [32m+[0m [0m[1m [0mactions [0m [0m   = [
              [32m+[0m [0m"s3:PutObject",
            ]
          [32m+[0m [0m[1m[0meffect[0m[0m    = "Allow"
          [32m+[0m [0m[1m[0mresources[0m[0m = [
              [32m+[0m [0m"arn:aws:s3:::alb-development-access-logs-haydarctl/*",
            ]
          [32m+[0m [0mprincipals {
              [32m+[0m [0m[1m[0midentifiers[0m[0m = [
                  [32m+[0m [0m"arn:aws:iam::156460612806:root",
                ]
              [32m+[0m [0m[1m[0mtype[0m[0m        = "AWS"
            }
        }
    }
        """
        obj = TerragruntIssueGenerator()
        content = obj.create_template_file(repo="infra_hede", plan_output=sample_plan_output, module_name="eu-west-1/s3")
        obj.save_template_content(repo="infra_hede", template_directory="./test-templates", content=content)
      
        file_status = check_file("test-templates/infra_hede.md")

        self.assertNotEqual(content, None)
        self.assertEqual(file_status, True)
