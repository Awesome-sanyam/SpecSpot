# myapp/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_view, name='start'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('Phones/', views.phone_view, name='phones'),
    path('Specification/', views.get_phone_specs, name='specification'),
    path('about/', views.about_view, name='about'),
    path('terms/', views.terms_view, name='terms'),
    path('specs/<str:phone_name>/', views.get_phone_specs, name='get_phone_specs'),
    path('logout/', views.logout_view, name='logout'),
    
    path('api/find-phone/', views.ai_phone_finder, name='ai_find_phone'),
    path('api/submit-feedback/', views.submit_feedback_view, name='submit_feedback'),
    path('api/specs-json/<str:phone_name>/', views.api_get_phone_specs_json, name='api_get_phone_specs_json'),
    
    path('brands/', views.brands_view, name='brands'),
    path('api/brands/', views.api_get_brand_data, name='api_get_brand_data'),

    path('dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('dashboard/feedback/delete/', views.delete_feedback_view, name='delete_feedback'),
    path('dashboard/users/delete/', views.delete_users_view, name='delete_users'),

    path('api/tech-chat/', views.ai_tech_chat, name='ai_tech_chat'),
    path('api/login/', views.login_api_view, name='login_api'),
    path('api/register/', views.register_api_view, name='register_api'),
    
    path('dashboard/phones/add/', views.add_phone_view, name='add_phone'),
    path('dashboard/phones/edit/<int:phone_id>/', views.edit_phone_view, name='edit_phone'),
    path('dashboard/phones/delete/', views.delete_phones_view, name='delete_phones'),

    path('glossary/', views.glossary_view, name='glossary'),
    path('dashboard/glossary/add/', views.add_glossary_view, name='add_glossary'),
    path('dashboard/glossary/edit/<int:term_id>/', views.edit_glossary_view, name='edit_glossary'),
    path('dashboard/glossary/delete/', views.delete_glossary_view, name='delete_glossary'),
    
    path('api/get-tech-news/', views.api_get_tech_news, name='api_get_tech_news'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)