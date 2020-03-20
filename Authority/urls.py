from django.urls import path

from Authority.views import sorted_list

urlpatterns = [
    path('sorted_list/', sorted_list, name='sorted_list')
]
