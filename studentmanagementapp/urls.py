from django.urls import path
from .views import homeview,StudentDetailView,BookCreateView,SchoolCreateView,StudentCreateView,Search

urlpatterns = [
    path('',homeview,name='home'),
    path('student/<int:pk>/',StudentDetailView.as_view(),name='student-detail'),
    path('student/create/',StudentCreateView.as_view(),name='student-create'),
    path('book/create/',BookCreateView.as_view(),name='book-create'),
    path('school/create/',SchoolCreateView.as_view(),name='school-create'),
    path('search/',Search.as_view(),name='search'),
    # path('',StudentCreateView.as_view(),name='home'),
]