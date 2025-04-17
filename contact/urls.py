from django.urls import path, include
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index' ),
    path('cadastro/', views.cadastros, name='cadastros' ),
    path('visualiza/', views.visualizacao, name='visualizacao' ),

]