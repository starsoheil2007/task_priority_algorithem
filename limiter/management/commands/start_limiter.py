from django.core.management.base import BaseCommand
import time
from limiter.models import *


class Command(BaseCommand):
    help = "This ... "
    one_path = []
    count = 0
    before_informed_no_process = False

    def handle(self, *args, **options):
        while True:
            # Get all not finished process
            all_waiting_process = UserProcessQueue.objects.filter(is_finished=False, is_stopped=True)
            # Get running process if exist
            try:
                running_process = UserProcessQueue.objects.get(is_stopped=False)
                self.stdout.write(self.style.SUCCESS("We have one running task. No ({}):".format(running_process.pk)))
            except UserProcessQueue.DoesNotExist:
                running_process = None
            # First check we don't have any process to do
            if len(all_waiting_process) == 0:
                self.stdout.write(self.style.SUCCESS("We don't have any user to process"))
            else:
                self.stdout.write(self.style.SUCCESS("We have {} uncompleted process".format(len(all_waiting_process))))
                # Pick high priority process from uncompleted process
                most_priority_process = pick_most_priority_process(all_waiting_process)
                # Pick check priority of most most priority process with running task
                if running_process:
                    if running_process.user.weight < most_priority_process.user.weight:
                        running_process.stop()
                        limited_f(most_priority_process)
                        self.stdout.write(
                            self.style.WARNING("Task No {} for user {} changed with Task No {} for user {} with this priority ({} < {})".format(running_process.pk, running_process.user.pk, most_priority_process.pk, most_priority_process.user.pk,
                                                                                                                                                running_process.user.weight, most_priority_process.user.weight)))
                    else:
                        limited_f(running_process)
                        self.stdout.write(self.style.SUCCESS("We continued Task No {} for user {} ".format(running_process.pk, running_process.user.pk)))
                else:
                    # Pick check priority of most most priority process with running task
                    limited_f(most_priority_process)
                    self.stdout.write(self.style.SUCCESS("We started Task No {} for user {} ".format(most_priority_process.pk, most_priority_process.user.pk)))
            time.sleep(10)


def pick_most_priority_process(all_process):
    return all_process.order_by("-user__weight", "id").first()


def limited_f(user_process):
    user_process.run()
    user_process.handle_process()
