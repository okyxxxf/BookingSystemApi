from django.urls import path
from concerts import views


urlpatterns = [
    path('', views.concerts_list),
    path('<int:pk>', views.concert_details),
    path('top', views.get_three_last),
]
