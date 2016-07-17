from django.template import Template, Context


class AdminGenerator(object):

    def __init__(self, model_name, admin_file_resource, model_skeleton):
        self.model_name = model_name
        self.admin_name = model_name + 'Admin'
        self.admin_file_resource = admin_file_resource
        self.model_skeleton = model_skeleton

    def generate(self):
        template = Template(self.model_skeleton)
        context = Context(dict(model_name=self.model_name, admin_name=self.admin_name))

        generated = template.render(context)
        self.admin_file_resource.write(generated)
        self.admin_file_resource.close()