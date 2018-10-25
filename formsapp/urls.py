from django.urls import path
from formsapp import views

# class based built in View
from django.views.generic import TemplateView

urlpatterns = [
    path('contact-us/', views.ContactUsFormView.as_view()),
    path('register/', views.register),
    path('create-book/', views.BookFormView.as_view()),
    path('about-us/', TemplateView.as_view(template_name='formsapp/aboutus.html')),
    path('contactus-success/', TemplateView.as_view(template_name='formsapp/contactus-success.html')),
    path('books/', views.BookListView.as_view()),
    path('create-author/', views.AuthorCreateView.as_view()),
    path('update-author/<int:pk>', views.AuthorUpdateView.as_view()),
    path('author-success/<int:author_id>', views.author_create_success, name='author-detail'),
    path('author-delete/<int:pk>', views.AuthorDeleteView.as_view())
]
