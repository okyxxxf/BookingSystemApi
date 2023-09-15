from django.urls import path
from promocodes import views


urlpatterns = [
    path('', views.promocodes_list),
    path('<int:pk>', views.promocodes_details)
]
