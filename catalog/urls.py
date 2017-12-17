from django.conf.urls import url
from . import views

urlpatterns = [
    # This url() function defines a URL pattern (r'^$'), and a view function
    # that will be called if the pattern is detected (views.index a function named
    # index() in views.py).
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'authors/$', views.AuthorListView.as_view(), name='authors'),
    
    # Unlike our previous mappers, in this case we are using our regular expression
    # (RE) to match against a real "pattern" rather than just a string. What this
    # particular RE does is match against any URL that starts with book/,
    # followed by one or more digits (numbers) before the end of line marker.
    # While performing the matching, it "captures" the digits, and passes them to
    # the view function as a parameter named pk
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail')
]