from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer,CartSerializer,CartItemsSerializer,UserSerializer,OrderSerializer,OrderItemsSerializer
from django.http.response import JsonResponse
from django.http.response import Http404
from .models import Product,Cart,CartItems,User,Order,OrderItems

# Create your views here.

class ProductView(APIView):

    def get_product(self,pk):
        try:
            product = Product.objects.get(pk=pk)
            return product
        except:
            return JsonResponse("product does not exist", safe=False)

    def get(self,request,pk=None):
        if pk:
            data = self.get_product(pk=pk)
            serializer = ProductSerializer(data)
        else:
            data = Product.objects.all()
            serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Product Added successfully")
        return Response("Failed to add product")

    def delete(self,request,pk=None):
        product_to_delete = Product.objects.get(pk=pk)
        product_to_delete.delete()
        return JsonResponse("Product deleted successfully", safe=False)

    def put(self,request,pk=None):
        product_to_update = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=product_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response("Product updated successfully")
        return Response("Failed to update Product")

class UserView(APIView):

    def get_user(self,pk):
        try:
            user = User.objects.get(pk=pk)
            return user
        except:
            return JsonResponse("user does not exist", safe=False)

    def get(self,request,pk=None):
        if pk:
            data = self.get_user(pk=pk)
            serializer = UserSerializer(data)
        else:
            data = User.objects.all()
            serializer = UserSerializer(data, many=True)
        return Response(serializer.data)


class CartView(APIView):

    def get_cart(self,pk):
        try:
            cart = Cart.objects.get(pk=pk)
            return cart
        except:
            return JsonResponse("product does not exist", safe=False)

    def get(self,request,pk=None):
        if pk:
            data = self.get_cart(pk=pk)
            serializer = CartSerializer(data)
        else:
            data = Cart.objects.all()
            serializer = CartSerializer(data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Added to cart")
        return Response("Failed to add to cart")

    def delete(self,request,pk=None):
        item_to_delete = Cart.objects.get(pk=pk)
        item_to_delete.delete()
        return JsonResponse("Removed from cart", safe=False)




class CartItemsView(APIView):

    # def get_cartItems(self,cartId):
    #     try:
    #         cartItems = CartItems.objects.get(cartId=cartId)
    #         print(cartItems)
    #         return cartItems
    #     except:
    #         return JsonResponse("product does not exist", safe=False)

    def get(self,request,cartId=None):
        if cartId:
            data = CartItems.objects.filter(cartId=cartId)
            serializer = CartItemsSerializer(data, many=True)
        else:
            data = CartItems.objects.all()
            serializer = CartItemsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = CartItemsSerializer(data=data)
        if serializer.is_valid():
            insert = serializer.save()
            print(insert)
            return Response("Added to cart")
        return Response("Failed to add to cart")

    def delete(self,request,pk=None):
        item_to_delete = CartItems.objects.get(pk=pk)
        delete = item_to_delete.delete()
        print(delete)
        return JsonResponse("Removed from cart", safe=False)






class OrderView(APIView):

    def get_order(self,pk):
        try:
            order = Order.objects.get(pk=pk)
            return order
        except:
            return JsonResponse("user does not exist", safe=False)

    def get(self,request,pk=None):
        if pk:
            data = self.get_order(pk=pk)
            serializer = OrderSerializer(data)
        else:
            data = Order.objects.all()
            serializer = OrderSerializer(data, many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
 
            return Response(serializer.data)
        return Response("Failed to Placed Order")


class OrderItemsView(APIView):

    def get_orderitems(self,pk):
        try:
            orderItems = OrderItems.objects.get(pk=pk)
            return orderItems
        except:
            return JsonResponse("user does not exist", safe=False)

    def get(self,request,pk=None):
        if pk:
            data = self.get_orderitems(pk=pk)
            serializer = OrderItemsSerializer(data)
        else:
            data = OrderItems.objects.all()
            serializer = OrderItemsSerializer(data, many=True)
        return Response(serializer.data)

    
    def post(self,request):
        data = request.data
        serializer = OrderItemsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # print(cartItems)
            return Response("Orderitems Placed Successfully")
        return Response("Failed to Placed Order")


# class OrderItems(APIView):

#     def post(self,request):
