"""URL routes for the store app."""
from django.urls import path

from store import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
]
