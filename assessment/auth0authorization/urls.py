from django.urls import path

from . import views

urlpatterns = [
    path('api/public', views.public),
    path('api/status', views.private),
    path('api/validate', views.consulta),
    path('api/private-scoped', views.private_scoped),
    path('api/receive_jwt', views.receive_jwt)
]