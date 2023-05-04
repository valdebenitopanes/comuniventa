from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'accept': 'image/*'}) # Añadir atributo 'accept' para aceptar solo imágenes

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.content_type.split('/')[0] != 'image': # Verificar que se trata de una imagen
                raise forms.ValidationError('El archivo no es una imagen.')
        else:
            raise forms.ValidationError('Este campo es obligatorio.')
        return image
