from django.db import models
from django.core.urlresolvers import reverse

class user_list(models.Model):

    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    email = models.EmailField()

    def __str__(self):

        return ' '.join([self.first_name, self.last_name])

    def get_absolute_url(self):
        return reverse('contacts-view', kwargs={'pk':self.id})
