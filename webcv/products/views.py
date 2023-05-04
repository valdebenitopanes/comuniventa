from .forms import ProductForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
# from usuarios.models import Seller
# Create your views here.
class ProductListViewSeller(LoginRequiredMixin,ListView):
    template_name = 'products/seller.html'
    # queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        # Obtener el usuario logeado
        user = self.request.user
        # Obtener los productos del vendedor que ha iniciado sesión
        queryset = Product.objects.filter(seller=user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Productos'
        context['subtitle'] = 'lista de productos'

        # Obtener el usuario logeado
        user = self.request.user

        # Obtener los grupos a los que pertenece el usuario
        groups = user.groups.all()

        # Verificar si el usuario pertenece al grupo "seller"
        is_seller = groups.filter(name="seller").exists()

        context['is_seller'] = is_seller
        return context


class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Productos'
        context['subtitle'] = 'lista de productos'

        # Obtener el usuario logeado
        user = self.request.user

        # Obtener los grupos a los que pertenece el usuario
        groups = user.groups.all()

        # Verificar si el usuario pertenece al grupo "seller"
        is_seller = groups.filter(name="seller").exists()

        context['is_seller'] = is_seller
        return context


class ProductDetaiView(DetailView):
    model = Product
    template_name = 'products/product.html'

    # def get_queryset(self):
    #     queryset =  Product.objects.get(id==self.kwargs['pk'])
    #     return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(
            category__title__icontains=self.query())
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('data-search')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query
        return context


class SellerProductListView(ListView):
    template_name = 'seller_product_list.html'

    # def get_queryset(self):
    #     seller = Seller.objects.get(user=self.request.user)
    #     return Product.objects.filter(category=seller.category)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['seller'] = Seller.objects.get(user=self.request.user)
    #     return context


@login_required
def create_product(request):
    # Obtener el objeto de grupo 'seller'
    seller_group = Group.objects.get(name='seller')
    # Verificar que el usuario logeado pertenece al grupo 'seller'
    if seller_group.user_set.filter(id=request.user.id).exists():
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.seller_id = request.user.id
                product.save()
                messages.success(request, 'Producto creado exitosamente!')
                return redirect('index')
        else:
            form2 = ProductForm()
        return render(request, 'products/create.html', {'form': form2})
    else:
        messages.warning(request, 'Debe ser vendedor para agregar productos.')
        return redirect('index')
