
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from books.models import Book
from books.serializers import BookSerializer
from rest_framework import generics, status, request, viewsets


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        #print(books)
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books.",
            "books": serializer_data,
        }
        return Response(data)



# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer_data = BookSerializer(book).data
            data = {
                "status": 'success',
                "book": serializer_data,
            }
            return Response(data,data=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "status": 'Does not exist',
                    "message": "Book not found."}, status=status.HTTP_404_NOT_FOUND
            )


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({
                "status": 'True',
            "message": "Book deleted."},
            status=status.HTTP_200_OK )
        except Exception:
            return Response({
                "status": 'False',
                "message": "Book not found."
            },status=status.HTTP_400_BAD_REQUEST )



# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            return Response({
                "status": 'True',
                "message": "Book updated."
            },status=status.HTTP_200_OK )






# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        #print(data)
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status': 'success',
                'books': data,
            }
            return Response(data,status=status.HTTP_200_OK)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # crud create, read, update, delete
    # xohlasak customniy querysetni almashtirsak bo'ladi.



class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer