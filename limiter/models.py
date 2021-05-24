from django.db import models


class Users(models.Model):
    """
    This model stores users and weight (priority) of them
    """
    user_name = models.CharField(max_length=30, null=False, blank=False)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return self.user_name


class UserProcessQueue(models.Model):
    """
    This model stores queue of tasks based on inputs
    """
    user = models.ForeignKey(to=Users, null=False, blank=False, on_delete=models.CASCADE, related_name='process')
    time_to_complete = models.IntegerField(default=1)
    time_completed = models.IntegerField(default=1)
    is_stopped = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.user.user_name

    def stop(self):
        self.is_stopped = True
        self.save()

    def run(self):
        self.is_stopped = False
        self.save()

    def finish(self):
        self.is_stopped = True
        self.is_finished = True
        self.save()

    def handle_process(self):
        self.time_completed += 1
        self.save()
        if self.time_completed == self.time_to_complete:
            self.finish()
