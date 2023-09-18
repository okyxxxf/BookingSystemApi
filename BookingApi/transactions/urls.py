from django.urls import path
from transactions import views


urlpatterns = [
    path('', views.transactions_list),
    path('<int:pk>', views.transaction_details)
]
