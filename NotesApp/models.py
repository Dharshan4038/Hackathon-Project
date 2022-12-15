from django.db import models

# Create your models here.
class Notes(models.Model):
    NoteId = models.AutoField(primary_key=True)
    NoteTitle = models.CharField(max_length=100)
    NoteContent = models.CharField(max_length=5000)
    NoteCreated = models.DateField()
    