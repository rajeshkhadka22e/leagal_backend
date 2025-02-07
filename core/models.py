# models.py
from django.db import models
from filehub.fields import ImagePickerField

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question



class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = ImagePickerField()
    bio = models.TextField(help_text="Full detail information for this team member.")

    def __str__(self):
        return self.name