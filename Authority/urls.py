from django.urls import path

from Authority.views import sorted_list_3, home, sorted_list_1, sorted_list_2

urlpatterns = [
    path('sorted_list_1/', sorted_list_1, name='sorted_list_1'),
    path('sorted_list_2/', sorted_list_2, name='sorted_list_2'),
    path('sorted_list_3/', sorted_list_3, name='sorted_list_3'),
    path('home/', home, name='sorted_list')
]
