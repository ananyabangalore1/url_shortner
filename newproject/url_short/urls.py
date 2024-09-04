from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.shorten_url, name='shorten_url'),  # Shorten URL form
    path('<str:short_code>', views.redirect_url, name='redirect_url'),  # Redirect based on short code
]
