from django.core.management import BaseCommand
from core.rnd_opt import main

__author__ = 'vadim'


class Command(BaseCommand):
    help = 'process'

    def add_arguments(self, parser):
        parser.add_argument('multiplier', nargs='+', type=float)
        parser.add_argument('module', nargs='+', type=int)
        parser.add_argument('init_value', nargs='+', type=float)


    def handle(self, *args, **options):
        main(options['multiplier'][0], options['module'][0], options['init_value'][0])