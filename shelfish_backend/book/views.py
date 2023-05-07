from django.shortcuts import render
from .serializers import BookSerializer 
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Book
# Create your views here.
class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    
class BookAPIView(APIView):
    def get_object(self, pk):
            try:
                return Book.objects.get(pk=pk)
            except Book.DoesNotExist:
                raise Http404
            
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = BookSerializer(data)

        else:
            data = Book.objects.all()
            serializer = BookSerializer(data, many=True)

            return Response(serializer.data)
        
    def post(self, request, format=None):
        data = request.data
        serializer = BookSerializer(data=data)

        # Check if the data passed is valid
        serializer.is_valid(raise_exception=True)

        # Create Todo in the DB
        serializer.save()

        # Return Response to User

        response = Response()

        response.data = {
            'message': 'Book Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        # Get the todo to update
        book_to_update = Book.objects.get(pk=pk)

        # Pass the instance to update to the serializer, and the data and also partial to the serializer
        # Passing partial will allow us to update without passing the entire Todo object
        serializer = BookSerializer(instance=book_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
        }

        return response
    
    def delete(self, request, pk, format=None):
        book_to_delete =  Book.objects.get(pk=pk)

        # delete the todo
        book_to_delete.delete()

        return Response({
            'message': 'Book Deleted Successfully'
        })
