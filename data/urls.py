from django.urls import path
from data.views import prototype_data_cleaner

app_name = 'data'

urlpatterns = [
    path('', prototype_data_cleaner, name='prototype_data_cleaner'),
]