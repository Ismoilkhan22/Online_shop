from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from . import views_2
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'products/', views_2.ApiProduct2)
router.register(r'category/', views_2.ApiCategory2)
router.register(r'carts/', views_2.CartViewSet)

product_router = routers.NestedDefaultRouter(router, r'products/', lookup="product")
product_router.register(r'reviews/', views_2.ReviewViewSet, basename="product-reviews")
urlpatterns = [

    path("", include(router.urls)),
    path("", include(product_router.urls))

]
