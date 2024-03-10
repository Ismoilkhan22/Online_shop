from xml.etree.ElementInclude import include

from django.urls import path
from . import views
from . import views_2
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products", views_2.ApiProduct2),
router.register("category", views_2.ApiCategory2),
urlpatterns = [
                  # path('products/', views.ApiProducts.as_view()),
                  # path('product/<str:pk>/', views.ApiProduct.as_view()),
                  # path('categories/', views.ApiCategories.as_view()),
                  # path('category/<str:pk>/', views.ApiCategory.as_view())
              ] + router.urls
