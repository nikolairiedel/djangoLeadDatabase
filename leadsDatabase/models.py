from django.db import models

# In this case the model consists of the name of a lead and its email adress.
class Lead(models.Model):
    name_text = models.CharField('Lead name', max_length=60)
    email_text = models.EmailField('Lead Email', max_length=254)
    def __str__(self):
        return self.name_text
