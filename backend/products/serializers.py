from rest_framework import serializers

from .validators import unique_product_title, validate_title_no_hello
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(
        validators=[unique_product_title, validate_title_no_hello])
    name = serializers.CharField(source='title', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Product
        # fields can be instance methods, properties
        fields = [
            # 'user',
            'pk',
            'title',
            'content',
            'name',
            'price',
            'sale_price',
            'my_discount'
        ]

    # def validate_title(self, value):
    #     # iexact is case insensitive
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializer.ValidationError("This title exists")
    #     return value

    def get_my_discount(self, obj):
        # can use obj to grab foreign keys and other params
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
