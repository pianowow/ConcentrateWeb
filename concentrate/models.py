from django.db import models

class db_file(models.Model):
    file_name = models.CharField(max_length=200)
    file = models.FileField()
    
    def __str__(self):
        return self.file_name