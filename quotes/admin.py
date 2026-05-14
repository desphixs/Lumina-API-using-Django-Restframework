from django.contrib import admin

# We need to import our Quote model so the admin panel can find it.
# The '.' means "look in the current folder".
from .models import Quote

# Registering a model is like giving it a "VIP pass" to the Django Admin panel.
# Once registered, you can create, edit, and delete quotes through a nice web interface.
# Analogy: This is like adding a new product category to your store's cash register 
# so the cashier (you) can start scanning and selling those items.
admin.site.register(Quote)
