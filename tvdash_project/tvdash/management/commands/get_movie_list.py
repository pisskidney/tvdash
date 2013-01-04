from django.core.management.base import NoArgsCommand
from optparse import make_option

class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        make_option('--only-failed',
            action='store_true',
            dest='only_failed',
            default=False,
            help='Check only the previous failed object'),
        make_option('--wipe-inexistent',
            action='store_true',
            dest='wipe',
            default=False,
            help='Clean image attribute for objects where the original image is missing')
        )

    def handle_noargs(self, **options):
        print 'Lol'
