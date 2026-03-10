from django.urls import path
from . import views

urlpatterns = [
    path('',        views.form_page,    name='test_form_page'),
    path('submit/', views.submit_form,  name='test_form_submit'),
    path('success/',views.success_page, name='test_form_success'),
]
