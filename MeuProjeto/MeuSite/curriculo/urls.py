from django.urls import path
from . import views

app_name = 'curriculo'

urlpatterns = [
    path('spiff/', views.curriculo_spiff, name='curriculo_spiff'),
    path('spiff/v2/', views.curriculo_spiff_v2, name='curriculo_spiff_v2'),
    path('ranking/', views.ranking, name='ranking'),
    path("adicionar/", views.adicionar_item, name="adicionar_item"),
    path("editar/<int:id>/", views.editar_item, name="editar_item"),
    path("remover/<int:id>/", views.remover_item, name="remover_item"),

]
