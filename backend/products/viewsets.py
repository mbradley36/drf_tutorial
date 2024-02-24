from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

# viewsets have a lot of functionality built in.
# The below class can handle all crud functionality for the Producy model
# This does mean that a bunch of url routing is already set up and it's
# somewhat less intuitive to know what all is being covered.
# Tutorial dude prefers using APIViews(see views file) instead


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
