from django.db import models
from products.models import Product
# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=40)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # crear relacion de modelos
    products = models.ManyToManyField(Product) 

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
