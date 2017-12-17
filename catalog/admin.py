from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.
admin.site.register(Genre)

# Define the admin class for author
class AuthorAdmin(admin.ModelAdmin):
    # Unfortunately we can't directly specify the genre field in list_display
    # because it is a ManyToManyField (Django prevents this because there would
    # be a large database access "cost" in doing so). Instead we'll define a
    # display_genre function to get the information as a string (this is the
    # function we've called above; we'll define it below).
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # The fields attribute lists just those fields that are to be displayed on
    # the form, in order. Fields are displayed vertically by default, but will
    # display horizontally if you further group them in a tuple (as shown in the
    # "date" fields above).
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Sometimes it can make sense to be able to add associated records at the same time.
# For example, it may make sense to have both the book information and information
# about the specific copies you've got on the same detail page. You can do this by
# declaring inlines, of type TabularInline (horizonal layout) or StackedInline
# (vertical layout, just like the default model layout).
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# How to create and register the new models; for the purpose of this
# demonstration, we'll instead use the @register decorator to register
# the models (this does exactly the same thing as the admin.site.register() syntax):
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    # Once you've got a lot of items in a list, it can be useful to be able to filter
    # which items are displayed. This is done by listing fields in the list_filter attribute.
    # The list view will now include a filter box to the right.
    list_filter = ('status', 'due_back')

    # Each section has its own title (or None, if you don't want a title) and an associated
    # tuple of fields in a dictionary the format is complicated to describe, but fairly
    # easy to understand if you look at the code fragment immediately below.
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )