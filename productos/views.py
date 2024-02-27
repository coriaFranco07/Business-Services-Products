from django.http import Http404
from django.shortcuts import get_object_or_404, render
from productos.models import Producto, CategoriaProd
from django.db.models import Count


# Create your views here.
def producto(request):
    productos = Producto.objects.filter(disponibilidad=True)  # Obtén solo productos disponibles
    categorias = CategoriaProd.objects.filter(producto__in=productos).annotate(num_productos=Count('producto')).filter(num_productos__gt=0)
    return render(request, "productos/productos.html", {"productos": productos, "categorias": categorias})

def categoria(request, categoria_slug):
    try:
        categoria = get_object_or_404(CategoriaProd, slug=categoria_slug)
        productos = Producto.objects.filter(categorias=categoria)
        return render(request, "productos/categoria.html", {"categoria": categoria, "productos": productos})
    except Http404:
        return render(request, "productos/pagina_no_encontrada.html")