from django.db import models
from django.urls import reverse # used to generate urls by reversing the URL patterns
import uuid # required for unique book instances

# Create your models here.
class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Language(models.Model):
    """
    Model representing a Language (e.g. English, French, Japanese, etc.)
    """
    
    LANGUAGE = [
      ('EN', 'English'),
      ('FR', 'French'),
      ('JP', 'Japanese'),
      ('TR', 'Turkish'),
    ]
    
    name = models.CharField(max_length=200, choices=LANGUAGE, help_text="Enter a the book's natural language (e.g. English, French, Japanese etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    # The other parameters of interest in the author field are null=True, which allows the database
    # to store a Null value if no author is selected, and on_delete=models.SET_NULL, which will set
    # the value of the author to Null if the associated author record is deleted.
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        # get_absolute_url() returns a URL that can be used to access a detail record for
        # this model (for this to work we will have to define a URL mapping that has the
        # name book-detail, and define an associated view and template).
        return reverse('book-detail', args=[str(self.id)])

    
import uuid # Required for unique book instances

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    # UUIDField is used for the id field to set it as the primary_key for this model.
    # This type of field allocates a globally unique value for each instance
    # (one for every book you can find in the library)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    # DateField is used for the due_back date (at which the book is expected to come
    # available after being borrowed or in maintenance). This value can be blank or
    # null (needed for when the book is available). The model metadata (Class Meta)
    # uses this field to order records when they are returned in a query
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    # status is a CharField that defines a choice/selection list. As you can see,
    # we define a tuple containing tuples of key-value pairs and pass it to the choices
    # argument. The value in a key/value pair is a display value that a user can select,
    # while the keys are the values that are actually saved if the option is selected.
    # We've also set a default value of 'm' (maintenance) as books will initially be created
    # unavailable before they are stocked on the shelves.
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.book.title)

    
class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)