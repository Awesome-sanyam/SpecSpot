"""
URL configuration for SpecSpot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# myproject/urls.py
# SpecSpot/SpecSpot/urls.py
# myproject/urls.py

# In SpecSpot/urls.py

from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include your myapp URLs
    path('', include('myapp.urls')),
    # --- ADD THIS LINE ---
    # This includes all of Django's built-in authentication URLs like login and logout.
    # The {% url 'logout' %} tag will now work correctly.
    # path('accounts/', include('django.contrib.auth.urls')),
]