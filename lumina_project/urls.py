"""
URL configuration for lumina_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
# We import our QuoteList view from the 'quotes' app.
# The 'as_view()' part is needed because QuoteList is a "Class-Based View".
from quotes.views import QuoteList

# The 'urlpatterns' list is like a "GPS map" for your website. 
# It tells Django: "When a user visits this specific web address (URL), 
# take them to this specific view (the logic)."
urlpatterns = [
    # This path is the entry door for the Admin dashboard.
    path('admin/', admin.site.urls),
    
    # This path points to our list of quotes.
    # When a user visits 'http://127.0.0.1:8000/api/quotes/', 
    # Django will call our QuoteList view to handle the request.
    # Analogy: This is like putting a "Quotes Section" sign on a specific 
    # aisle in a store so customers know exactly where to go.
    path('api/quotes/', QuoteList.as_view()),
]
