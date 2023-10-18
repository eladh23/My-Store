from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer, CartSerializer, ProductSerializer
from .models import Cart, CartItem, Product


@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        all_products = Product.objects.all()
        all_products_json = ProductSerializer(all_products, many=True).data
        return Response(all_products_json)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ProductSerializer(
            product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def carts(request):
    if request.method == 'GET':
        # Retrieve the user's cart if it exists
        user = request.user  # Assuming you are using authentication
        try:
            cart = Cart.objects.get(user=user)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            # If the user doesn't have a cart, you can return an empty cart or an appropriate response
            return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        # Create a new cart for the user
        user = request.user  # Assuming you are using authentication
        cart = Cart(user=user)
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def cart_detail(request, id):
    try:
        cart = Cart.objects.get(pk=id)
    except Cart.DoesNotExist:
        return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve the details of the specific cart
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    if request.method == 'PUT':
        # Update the cart's details
        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        # Delete the cart
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def cartsItem(request):
    if request.method == 'GET':
        cartsItem = CartItem.objects.all()
        cartsItem_json = CartItemSerializer(cartsItem, many=True).data
        return Response(cartsItem_json)
    elif request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cartItem_detail(request, id):
    try:
        cartitem = CartItem.objects.get(pk=id)
    except CartItem.DoesNotExist:
        return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve the details of the specific cart
        serializer = CartItemSerializer(cartitem)
        return Response(serializer.data)

    if request.method == 'PUT':
        # Update the cart's details
        serializer = CartItemSerializer(
            cartitem, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        # Delete the cart
        cartitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
