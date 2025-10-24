from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    quota = models.IntegerField()

    def __str__(self):
        return self.title

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')

    def __str__(self):
        return f"{self.name} - {self.event.title}"


# Create your models here.
