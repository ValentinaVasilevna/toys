from django.urls import path
from . import views

urlpatterns = [
    path("", views.cat_index, name="cat_index"),#
    path("cat/<int:pk>/", views.cat_detail, name="cat_detail"),
    path("cat/<int:n>/all/<int:pk>/", views.toy_detail, name="toy_detail"),
#    path("all/", views.toy_index, name="toy_index"),#
#    path("all/<int:pk>/", views.toy_detail, name="toy_detail"),
]	
