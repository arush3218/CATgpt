from django.urls import reverse, path, include
from .views import index, response

from.views import index

urlpatterns = [
    path('', index, name = 'index'),
    path('response', response, name = 'response'),
]
