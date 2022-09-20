from itertools import product
from . import views
from django.urls import path
from django.template import RequestContext

app_name = 'mysite'
urlpatterns= [
    path('home/', views.home, name='home'),
    path('add_product/', views.addProduct, name="add_product"),
    path('add_category/', views.addCategory, name="add_category"),
    path('category/<str:category>/', views.category, name="category"),
    path('product/<str:product_name>/<int:product_id>', views.product, name='product'),
    path('test/', views.test, name="test")
]