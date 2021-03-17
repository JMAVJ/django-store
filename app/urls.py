from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view()),
    path('product/<int:id>', Product.as_view()),
    path('add-product', add_product),
    path('delete-product/<int:id>', delete_product),
    path('edit-product/<int:id>', edit_product),
]
