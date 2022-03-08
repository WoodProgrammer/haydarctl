from jinja2 import Environment, FileSystemLoader, Template


class TerragruntIssueGenerator(object):
    def __init__(self):
        env = Environment(
            loader=FileSystemLoader('templates'), 
            autoescape=True)

        self.template = Template("""
## Config Drift Results

:scream: :fire: There is a config drift on Terragrunt module <b>{{module_name}}</b> :scream: :fire:

<hr></hr>

<pre>
<code>
{{plan_output | safe}}
</code>
</pre>
""")

    def create_template_file(self, plan_output, module_name):
        output_from_parsed_template = self.template.render(plan_output="{}".format(plan_output), module_name=module_name)
        return output_from_parsed_template

    def save_template_content(self, template_directory, content, resource_name, resource_prefix):

        with open("{}/{}.{}.md".format(template_directory, resource_prefix,resource_name), "w") as fh:
            fh.write(content)