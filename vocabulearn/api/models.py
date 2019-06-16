from django.db import models
from django.utils import timezone


class Folder(models.Model):
    name = models.CharField(max_length=100)


class CardSet(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class FlashCard(models.Model):
    card_set = models.ForeignKey(CardSet, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    front = models.CharField(max_length=2000)
    back = models.CharField(max_length=2000)
    # history: string composed of '0' and '1' for either correct or wrong
    # index 0 is the most recent value
    history_front = models.CharField(max_length=1200, default="")
    history_back = models.CharField(max_length=1200, default="")
    last_trained_date_front = models.DateTimeField(default=timezone.now)
    last_trained_date_back = models.DateTimeField(default=timezone.now)
    front_first = models.BooleanField(default=False)
    marked = models.BooleanField(default=False)


class SetHistory(models.Model):
    card_set = models.ForeignKey(CardSet, on_delete=models.CASCADE)
    history = models.CharField(max_length=2000)
