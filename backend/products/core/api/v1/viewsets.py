from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from products.core.api.v1.serializers import ProductSerializer
from products.core.models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginViewSet(TokenObtainPairView):
    pass


class ProductViewSet(APIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data or None)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):

        if pk:
            try:
                product = Product.objects.get(pk=pk)
                serializer = self.serializer_class(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response(
                    {'detail': 'Produto não encontrado'},
                    status=status.HTTP_404_NOT_FOUND,
                )

        products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)

        # if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateViewSet(APIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, pk=None):

        try:
            product = Product.objects.get(pk=pk)
            serializer = self.serializer_class(product, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Product.DoesNotExist:
            return Response(
                {'detail': 'Produto não encontrado'}, status=status.HTTP_404_NOT_FOUND
            )


class ProductDeleteViewSet(APIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk=None):
        try:
            Product.objects.get(pk=pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(
                {'detail': 'Produto não encontrado'}, status=status.HTTP_404_NOT_FOUND
            )
