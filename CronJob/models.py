from django.contrib.auth.models import User
from django.db import models


# Create your models here

class CronJob(models.Model):
    # Title
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    # Auth
    username = models.CharField(max_length=127)
    password = models.CharField(max_length=127)

    # User
    author = models.ForeignKey(User, on_delete=models.deletion.CASCADE)

    # Execution
    """
    executionType = models.CharField(max_length=127, choices=(('all', 'Alle'),             # Results in select?
                                                        ('everyDay', 'Alle'),
                                                        ('allwaysAt', 'Immer am'),
                                                        ('all', 'Alle')))
    """
    executionType = models.CharField(max_length=10)
    executionValue = models.DateTimeField()

    # Notify
    notifyFailure = models.BooleanField()
    notifySuccessPreviousFailure = models.BooleanField()
    notifyDisableFailure = models.BooleanField()

    def __str__(self):
        return self.title
