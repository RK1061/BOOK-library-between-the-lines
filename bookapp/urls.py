from django.urls import path
from bookapp import views 

urlpatterns = [
    path('', views.index),
    path('addbook',views.addbook),
    path('delete/<bookid>', views.deleteBook),
    path('edit/<bookid>', views.editBook)

]

