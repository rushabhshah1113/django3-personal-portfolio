from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 250)
    date = models.DateField()

    # This function tells you the name of the object within the admin
    # Don't have to make migrations here because functions on blog don't change DATABASE
    def __str__(self):
        return self.title
