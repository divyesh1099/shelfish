from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list = ('title', 'available')

admin.site.register(Book, BookAdmin)