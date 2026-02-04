"""Views for the storefront."""
from dataclasses import dataclass
from typing import List

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render


@dataclass(frozen=True)
class Product:
    """Simple representation of a store product."""

    id: int
    name: str
    price: str
    description: str
    image: str
    badge: str


PRODUCTS: List[Product] = [
    Product(
        id=1,
        name="Aurora Smartwatch",
        price="$199",
        description="Track workouts, receive notifications, and stay connected.",
        image="https://images.unsplash.com/photo-1523275335684-37898b6baf30",
        badge="Best Seller",
    ),
    Product(
        id=2,
        name="Nimbus Headphones",
        price="$149",
        description="Noise-canceling comfort with 30-hour battery life.",
        image="https://images.unsplash.com/photo-1505740420928-5e560c06d30e",
        badge="New",
    ),
    Product(
        id=3,
        name="Lumen Desk Lamp",
        price="$89",
        description="Minimalist lighting with adjustable warmth settings.",
        image="https://images.unsplash.com/photo-1493666438817-866a91353ca9",
        badge="Eco",
    ),
    Product(
        id=4,
        name="Sierra Backpack",
        price="$129",
        description="Weather-ready carry with a padded laptop sleeve.",
        image="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        badge="Limited",
    ),
]


def home(request: HttpRequest) -> HttpResponse:
    """Render the homepage with featured products."""
    context = {
        "products": PRODUCTS,
        "highlights": [
            "Free shipping on orders over $75",
            "30-day hassle-free returns",
            "Dedicated support from product experts",
        ],
    }
    return render(request, "store/home.html", context)


def product_detail(request: HttpRequest, product_id: int) -> HttpResponse:
    """Render details for a single product."""
    product = next((item for item in PRODUCTS if item.id == product_id), None)
    if product is None:
        raise Http404("Product not found")
    return render(request, "store/product_detail.html", {"product": product})
