from django.urls import path
from utility import views

urlpatterns = [
    path('sum/', view=views.total, name='sum'),
    path('avg/', view=views.avg, name='average'),
    path('product/', view=views.product, name='product'),
]
