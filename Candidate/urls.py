from django.urls import path

from Candidate.views import handleResume

urlpatterns = [
    path('submitCV/', handleResume, name='submitCV')
]
