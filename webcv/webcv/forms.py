from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

class Registro(forms.Form):
    username = forms.CharField(required=True,max_length=50,min_length=3,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Ingresa nombre'
    }))
    email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Ingresa correo'
    }))
    password = forms.CharField(required=True,max_length=10,min_length=4,
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Ingresa contraseña'
    }))

    password_validation_correct = forms.CharField(required=True,max_length=10,min_length=4,
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Confirma tu contraseña'
    }),
    label="Confirmar contraseña")

    groups = forms.ModelChoiceField(
        # queryset=Group.objects.all(),
        queryset = Group.objects.exclude(name='Manage'),
        required=True,
        label=('Selecciona'),
        empty_label='Selecciona el tipo de usuario',
    )

    #validation exist field email or username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('Usuario ya creado!')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError(f'{email} ya fue registrado!')
        return email
    
    #validation confirmation password
    def clean(self):
        cleaned_data = super().clean() #get date forms clean and validate
        if cleaned_data.get('password_validation_correct') != cleaned_data.get('password'):
            self.add_error('password_validation_correct','La contraseña no coincide')

    def save(self):
        group =self.cleaned_data.get('groups')
        print(group)
        user = User.objects.create_user(
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password')
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )
     
        user.groups.add(group.id)

        return user
    
       
    
    