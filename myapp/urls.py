from django.urls import path, re_path
from myapp import views

app_name = "myapp"

urlpatterns = [
    path(r'', views.index, name="index"),
    path(r'about', views.about, name="about"),
    re_path(r"(?P<cat_no>\d+)", views.detail, name = "detail")
]