from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


class Event(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    picture = models.CharField(max_length=4000)
    location = models.CharField(max_length=255)

class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "event")

class File(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    file_location = models.CharField(max_length=255)

class Reaction(models.Model):
    class ReactionType(models.TextChoices):
        COMMENT = 'COMMENT', "Comment"
        AVAILIBILITY = 'AVAILIBILITY', "Availibility"
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    type = models.CharField(max_length=12, choices=ReactionType.choices, default=ReactionType.COMMENT)
    message = models.CharField(max_length=4000)
    availibility_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)