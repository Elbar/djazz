import os
import akoikelov
from akoikelov.djazz.management.commands.generators.model_generator import ModelGenerator
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    help = 'Generates model class'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str)
        parser.add_argument('model_name', type=str)

    def handle(self, *args, **options):
        package = options['app_name']
        model_name = options['model_name']

        package_dir = os.getcwd() + '/' + package

        if not os.path.exists(package_dir):
            raise CommandError('Given package %s doesn\'t exist!' % package)

        model_skeleton = open(os.path.join(akoikelov.djazz.__path__[0], 'conf', ) + '/tpl/model.py-tpl').read()
        models_file_resource = open(package_dir + '/models.py', 'a')
        generator = ModelGenerator(model_name, model_skeleton, models_file_resource, self)
        finished = False

        while not finished:
            finished = generator.ask()
            self.stdout.write('\n')

        generator.generate()
        self.stdout.write(self.style.SUCCESS('Model %s successfully generated!' % model_name))

    def execute(self, *args, **options):
        super(Command, self).execute(*args, **options)
        return 0
