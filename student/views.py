from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,BasePermission,SAFE_METHODS
from .models import Section,Student,Product,Items
from .serializers import SectionSerializer,StudentSerializer,productSerializer,ItemsSerializer
# Create your views here.

# ------Section get List and create----------
class SectionListCreateView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        obj=Section.objects.all()
        serializer=SectionSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
# -----Section update , view and delete -------
class SectionViewUpdateDelete(APIView):
    def get(self,request,id):
        try:
            obj=Section.objects.get(id=id)

        except Section.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=SectionSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            obj=Section.objects.get(id=id)

        except Section.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        serializer=SectionSerializer(obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        try:
            obj=Section.objects.get(id=id)

        except Section.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        serializer=SectionSerializer(obj,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            obj=Section.objects.get(id=id)

        except Section.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)


# ------Student get List and create----------
class StudentListCreateView(APIView):
    def get(self,request):
        obj=Student.objects.all()
        serializer=StudentSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
# -----student update , view and delete -------
class StudentViewUpdateDelete(APIView):
    def get(self,request,id):
        try:
            obj=Student.objects.get(id=id)

        except Student.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=StudentSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            obj=Student.objects.get(id=id)

        except Student.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        serializer=StudentSerializer(obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        try:
            obj=Student.objects.get(id=id)

        except Student.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        serializer=StudentSerializer(obj,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            obj=Student.objects.get(id=id)

        except Student.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)

# function based view
@api_view(['GET'])
def product_view(request):
    obj=Product.objects.all()
    serializer=productSerializer(obj,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def Items_view(request):

    get_obj=Items.objects.filter(price_including_tax__isnull=True)
    for item in get_obj:
        item.price_including_tax=item.price*item.price
        item.save()
    obj=Items.objects.all()
    serializer=ItemsSerializer(obj,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)