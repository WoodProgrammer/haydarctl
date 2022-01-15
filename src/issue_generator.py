from jinja2 import Environment, FileSystemLoader

class TerragruntIssueGenerator(object):
    def __init__(self):
        env = Environment(loader=FileSystemLoader('templates'), autoescape=True)

        self.template = env.get_template('terragrunt_gh_issue_templates/issue_template.jinja')
    

    def create_template_file(self, repo, plan_output, module_name):

        output_from_parsed_template = self.template.render(plan_output="{}".format(plan_output), module_name=module_name)
        return output_from_parsed_template


    def save_template_content(self, repo, template_directory, content):

        with open("{}/{}.md".format(template_directory, repo), "w") as fh:
            fh.write(content)