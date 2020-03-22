from django.urls import path

from Authority.views import sorted_list_3, home, sorted_list_1, sorted_list_2, sendEmail3, sendEmail2, sendEmail1

urlpatterns = [
    path('sorted_list_1/', sorted_list_1, name='sorted_list_1'),
    path('sorted_list_2/', sorted_list_2, name='sorted_list_2'),
    path('sorted_list_3/', sorted_list_3, name='sorted_list_3'),
    path('home/', home, name='sorted_list'),
    path('send_email_3/', sendEmail3, name='send_email_3'),
    path('send_email_2/', sendEmail2, name='send_email_2'),
    path('send_email_1/', sendEmail1, name='send_email_1')

]
