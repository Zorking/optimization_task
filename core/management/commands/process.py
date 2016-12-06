from django.core.management import BaseCommand
from core.rnd_opt import rnd_opt

__author__ = 'vadim'


class Command(BaseCommand):
    help = 'process'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        rnd_opt()