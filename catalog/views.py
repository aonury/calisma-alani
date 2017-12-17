from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # The first part of the view function fetches counts of records using the
    # objects.all() attribute on the model classes. It also gets a list of
    # BookInstance objects that have a status field value of 'a' (Available).
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # At the end of the function we call the render() function to create and
    # return an HTML page as a response (this shortcut function wraps a number
    # of other functions, simplifying this very common use-case). This takes
    # as parameters the original request object (an HttpRequest), an HTML
    # template with placeholders for the data, and a context variable (a Python
    # dictionary containing the data that will be inserted into those placeholders).
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )


# The generic view will query the database to get all records for the
# specified model (Book) then render a template located at /locallibrary/catalog/
# templates/catalog/book_list.html. Within the template you can access the list of
# books with the template variable named object_list OR book_list (i.e. generically "the_model_name_list").
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    # With this addition, as soon as you have more than 10 records the view will start
    # paginating the data it sends to the template. The different pages are accessed
    # using GET parameters to access page 2 you would use the URL: /catalog/books/?page=2.

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
  
class BookDetailView(generic.DetailView):
    # All you need to do now is create a template called /locallibrary/catalog/templates/
    # catalog/book_detail.html, and the view will pass it the database information for the specific
    # Book record extracted by the URL mapper. Within the template you can access the list of books with
    # the template variable named object OR book (i.e. generically "the_model_name").
    model = Book