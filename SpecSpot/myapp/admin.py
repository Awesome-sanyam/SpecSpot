# myapp/admin.py

from django.contrib import admin
from .models import Feedback,Phone,GlossaryTerm

# This line makes the Feedback model visible in the admin panel
admin.site.register(Feedback)
admin.site.register(Phone)
admin.site.register(GlossaryTerm)