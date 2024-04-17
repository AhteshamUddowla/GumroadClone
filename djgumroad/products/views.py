from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product


class ProductListView(generic.ListView):
    template_name = "discover.html"
    queryset = Product.objects.all()

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product.html"
    context_object_name = "product"

class UserProductListView(LoginRequiredMixin, generic.ListView):
    # shows the users created products
    template_name = "products.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

