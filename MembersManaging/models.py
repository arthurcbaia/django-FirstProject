from django.db import models

# Create your models here.
class MembersManage(models.Model):

    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.CharField(max_length = 20)

    def __str(self):
        return self.name