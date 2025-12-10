from django.urls import path
from . import views

app_name = 'curriculo'

urlpatterns = [
    path('spiff/', views.curriculo_spiff, name='curriculo_spiff'),
    path('spiff/v2/', views.curriculo_spiff_v2, name='curriculo_spiff_v2'),
]

