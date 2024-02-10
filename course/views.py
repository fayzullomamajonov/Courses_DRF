from urllib import response
from django.shortcuts import render
from .serializer import CourseSerializer,CourseUpdateSerializer
from rest_framework import generics,status,viewsets
from rest_framework.views import APIView
from .models import CourseModel
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# ******************************************************
# It is generics 

# class CourseList(generics.ListCreateAPIView):
#     queryset = CourseModel.objects.all()
#     serializer_class = CourseSerializer


# class CourseUpdateAPIView(generics.UpdateAPIView):
#     queryset = CourseModel.objects.all()
#     serializer_class = CourseSerializer
#     lookup_field = "pk"

# class CourseDeleteAPIView(generics.DestroyAPIView):
#     queryset = CourseModel.objects.all()
#     serializer_class = CourseSerializer
#     lookup_field = 'pk'
    

# ******************************************************
# It is APIView

# class CourseList(APIView):
#     def get(self, request):
#         courses = CourseModel.objects.all()
#         serializer = CourseSerializer(courses,many=True)
#         return Response(data=serializer.date)
    

# class CourseDetail(APIView):
#     def get(self, request, pk):
#         try:
#             course = CourseModel.objects.get(id=pk)
#         except CourseModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND, data={"detail": "Course not found"})
        
#         serializer = CourseUpdateSerializer(course)
#         return Response(data=serializer.data)

#     def post(self, request, pk):
#         try:
#             course = CourseModel.objects.get(id=pk)
#             serializer = CourseUpdateSerializer(instance=course, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data=serializer.data, status=status.HTTP_200_OK)
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         except CourseModel.DoesNotExist:
#             serializer = CourseUpdateSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class CourseDelete(APIView):
#     def delete(self,request,pk):
#         try:
#             course = CourseModel.objects.get(id=pk)
#         except CourseModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND,data={"detail":"Course not found"})
        
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# *******************************************************************

# It is ViewSet

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()
    permission_classes = [IsAuthenticated]
