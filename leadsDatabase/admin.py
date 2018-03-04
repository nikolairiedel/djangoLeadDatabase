from django.contrib import admin
from .models import Lead

# Registers the defined model for a lead at the admin site.
# The database can then be accessed from the UI of the admin page.
admin.site.register(Lead)
