from django.db import models

class Profile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Имя: %s, Id: %s" % (self.name, self.id)




