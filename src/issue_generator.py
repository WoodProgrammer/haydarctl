from jinja2 import Environment, FileSystemLoader

class TerragruntIssueGenerator(object):
    def __init__(self):
        env = Environment(loader=FileSystemLoader('templates'), autoescape=False)

        self.template = env.get_template('terragrunt_gh_issue_templates/issue_template.jinja')

    def create_template_file(self, repo, plan_output, module_name, template_directory):

        output_from_parsed_template = self.template.render(plan_output="{}".format(plan_output), module_name=module_name)
        print(output_from_parsed_template)

        with open("{}/{}.md".format(template_directory, repo), "w") as fh:
            fh.write(output_from_parsed_template)