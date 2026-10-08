from django.urls import path
from . import views
urlpatterns =[
    path('',views.index),
    path('index2/<int:vall>/',views.index2),
    path('<int:bookId>',views.viewbook),
]