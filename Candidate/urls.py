from django.urls import path

from Candidate import views
from Candidate.views import handleResume, personal
from django.conf.urls.static import static

urlpatterns = [
    path('', handleResume, name='submitCV'),
    path('personal/', personal, name='personal'),
]
