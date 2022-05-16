from . import views
from django.urls import path

urlpatterns = [
    path('',views.testProduct,name='testProduct'),
]
