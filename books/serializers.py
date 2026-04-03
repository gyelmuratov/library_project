

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title', 'subtitle', 'author', 'content','isbn', 'price')

    # Object-Level-Validation
    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        #check title if it contains alphabetical chars
        if not title.isalpha():
            raise ValidationError({
                'status': 'False',
                'message': 'Book title alphanumeric is required.'
            })
        # check title and author from database existence
        if Book.objects.filter(title=title).filter(author=author).exists():
            raise ValidationError({
                "status": "False",
                "message": "You cannot upload a book with the same title and author"
            })
        return data

    # FieldValidation
    def validate_price(self, price):
        if price < 0 or price > 999999:
            raise ValidationError({
                'status': 'False',
                'message': 'Price must be between 0 and 999999.'
            })




