from django.db import models

# Declare a class that inherits from Model class
class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    # upload_to picks a place to store image in
    image = models.ImageField(upload_to='portfolio/images/')
    # blank = True means some projects don't have URL
    url = models.URLField(blank=True)

    # This function tells you the name of the object within the admin
    def __str__(self):
        return self.title
