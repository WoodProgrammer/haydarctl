## Config Drift Results

:scream: :fire: There is a config drift on Terragrunt module <b>tests/haydar-terragrunt/development/eu-west-1/s3/terragrunt.hcl</b> :scream: :fire:

<hr></hr>

<pre>
<code>
[0m[1maws_s3_bucket.this[0]: Refreshing state... [id=alb-development-access-logs-haydarctl][0m
[0m[1maws_s3_bucket_policy.this[0]: Refreshing state... [id=alb-development-access-logs-haydarctl][0m
[0m[1maws_s3_bucket_public_access_block.this[0]: Refreshing state... [id=alb-development-access-logs-haydarctl][0m

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  [33m~[0m update in-place
 [36m<=[0m read (data resources)
[0m
Terraform will perform the following actions:

[1m  # data.aws_iam_policy_document.combined[0][0m will be read during apply
  # (config refers to values not yet known)[0m[0m
[0m [36m<=[0m[0m data "aws_iam_policy_document" "combined"  {
      [32m+[0m [0m[1m[0mid[0m[0m                      = (known after apply)
      [32m+[0m [0m[1m[0mjson[0m[0m                    = (known after apply)
      [32m+[0m [0m[1m[0msource_policy_documents[0m[0m = (known after apply)
    }

[1m  # data.aws_iam_policy_document.elb_log_delivery[0][0m will be read during apply
  # (config refers to values not yet known)[0m[0m
[0m [36m<=[0m[0m data "aws_iam_policy_document" "elb_log_delivery"  {
      [32m+[0m [0m[1m[0mid[0m[0m   = (known after apply)
      [32m+[0m [0m[1m[0mjson[0m[0m = (known after apply)

      [32m+[0m [0mstatement {
          [32m+[0m [0m[1m[0mactions[0m[0m   = [
              [32m+[0m [0m"s3:PutObject",
            ]
          [32m+[0m [0m[1m[0meffect[0m[0m    = "Allow"
          [32m+[0m [0m[1m[0mresources[0m[0m = [
              [32m+[0m [0m"arn:aws:s3:::alb-development-access-logs-haydarctl/*",
            ]

          [32m+[0m [0mprincipals {
              [32m+[0m [0m[1m[0midentifiers[0m[0m = [
                  [32m+[0m [0m"arn:aws:iam::156460612806:root",
                ]
              [32m+[0m [0m[1m[0mtype[0m[0m        = "AWS"
            }
        }
    }

[1m  # aws_s3_bucket.this[0][0m will be updated in-place[0m[0m
[0m  [33m~[0m[0m resource "aws_s3_bucket" "this" {
        [1m[0mid[0m[0m                          = "alb-development-access-logs-haydarctl"
        [1m[0mtags[0m[0m                        = {
            "Environment" = "development"
            "Name"        = "alb-development-access-logs-haydarctl"
            "Terraform"   = "true"
        }
        [90m# (12 unchanged attributes hidden)[0m[0m

      [32m+[0m [0mserver_side_encryption_configuration {
          [32m+[0m [0mrule {
              [32m+[0m [0mapply_server_side_encryption_by_default {
                  [32m+[0m [0m[1m[0msse_algorithm[0m[0m = "AES256"
                }
            }
        }


      [31m-[0m [0mwebsite {
          [31m-[0m [0m[1m[0mindex_document[0m[0m = "index.html" [90m->[0m [0m[90mnull[0m[0m
        }
        [90m# (1 unchanged block hidden)[0m[0m
    }

[1m  # aws_s3_bucket_policy.this[0][0m will be updated in-place[0m[0m
[0m  [33m~[0m[0m resource "aws_s3_bucket_policy" "this" {
        [1m[0mid[0m[0m     = "alb-development-access-logs-haydarctl"
      [33m~[0m [0m[1m[0mpolicy[0m[0m = jsonencode(
            {
              [31m-[0m [0mStatement = [
                  [31m-[0m [0m{
                      [31m-[0m [0mAction    = "s3:PutObject"
                      [31m-[0m [0mEffect    = "Allow"
                      [31m-[0m [0mPrincipal = {
                          [31m-[0m [0mAWS = "arn:aws:iam::156460612806:root"
                        }
                      [31m-[0m [0mResource  = "arn:aws:s3:::alb-development-access-logs-haydarctl/*"
                      [31m-[0m [0mSid       = ""
                    },
                ]
              [31m-[0m [0mVersion   = "2012-10-17"
            }
        ) [33m->[0m [0m(known after apply)
        [90m# (1 unchanged attribute hidden)[0m[0m
    }

[0m[1mPlan:[0m 0 to add, 2 to change, 0 to destroy.
[0m[90m
─────────────────────────────────────────────────────────────────────────────[0m

Note: You didn't use the -out option to save this plan, so Terraform can't
guarantee to take exactly these actions if you run "terraform apply" now.
Releasing state lock. This may take a few moments...

</code>
</pre>