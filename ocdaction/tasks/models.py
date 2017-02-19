from __future__ import unicode_literals

from django.db import models


class Task(models.Model):
    """a task is a user created task that can be completed
    by a user to track anxiety
    """
    task_name = models.CharField(max_length=100)
    is_archived = models.BooleanField(default=False)
    task_fears = models.CharField(max_length=300, blank=True)
    task_compulsions = models.CharField(max_length=300, blank=True)
    task_goals = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey('profiles.OCDActionUser', on_delete=models.CASCADE)

    # TODO add a task anxiety score once score model is created

    def __str__(self):
        return self.task_name


class AnxietyScore(models.Model):
    SCORE_ZERO = '0'
    SCORE_ONE = '1'
    SCORE_TWO = '2'
    SCORE_THREE = '3'
    SCORE_FOUR = '4'
    SCORE_FIVE = '5'
    SCORE_SIX = '6'
    SCORE_SEVEN = '7'
    SCORE_EIGHT = '8'
    SCORE_NINE = '9'
    SCORE_TEN = '10'

    ANXIETY_SCORE_CHOICES = (
        (SCORE_ZERO, 'Zero'),
        (SCORE_ONE, 'One'),
        (SCORE_TWO, 'Two'),
        (SCORE_THREE, 'Three'),
        (SCORE_FOUR, 'Four'),
        (SCORE_FIVE, 'Five'),
        (SCORE_SIX, 'Six'),
        (SCORE_SEVEN, 'Seven'),
        (SCORE_EIGHT, 'Eight'),
        (SCORE_NINE, 'Nine'),
        (SCORE_TEN, 'Ten'),
    )
    score = models.CharField(
        max_length=2,
        choices=ANXIETY_SCORE_CHOICES,
        default=SCORE_ZERO
    )
    user = models.ForeignKey('profiles.OCDActionUser', on_delete=models.CASCADE)
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE)