from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid #generacion aleatoria de slug
from django.contrib.auth.models import User

# Create your models - herencia
# vamos a heredar de la clase model
# las columnas de una base de datos.

class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=0,default=None)
    image = models.ImageField(upload_to='products/',null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,null=False,blank=False,unique=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    # def save(self,*args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Product,self).save(*args,**kwargs)

    # sucede antes de crear
def new_slug(sender, instance,*args, **kwargs):
    # sender es el modelo relacionado
    # instance.slug = slugify(instance.title)
    # condicionar generacion
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                # concatenar variables
                '{}-{}'.format(instance.title,str(uuid.uuid4())[:8])
            )
        instance.slug = slug


pre_save.connect(new_slug,sender=Product)




