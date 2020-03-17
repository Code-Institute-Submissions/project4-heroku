from django.db import models

# The models.

# The default is empty. This does not add a default product to the database.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='images')




    # What will be returned here is a string with the name.
    def __str__(self):
        return self.name
