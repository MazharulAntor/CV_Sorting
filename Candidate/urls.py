from django.urls import path

from Candidate import views
from Candidate.views import handleResume, personal, contact, con
from django.conf.urls.static import static

urlpatterns = [
    path('', handleResume, name='submitCV'),
    path('personal/', personal, name='personal'),

    path('con/', con, name='con'),
    path('con/contact/', contact, name='contact'),
]
