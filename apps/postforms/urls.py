from django.urls import path

from . import views


app_name = 'postforms'
urlpatterns = [
    path('<slug:url>/', views.CustomFormView.as_view(), name='custom_form'),
]
