# We import 'serializers' from Django REST Framework. 
# Think of a serializer as a "translator" that converts complex database objects 
# into a simple format (like JSON) that frontend apps and mobile phones understand.
from rest_framework import serializers

# We also need to import our 'Quote' model so the serializer knows what it is translating.
from .models import Quote

# A 'ModelSerializer' is a special tool that automatically figures out how 
# to translate each field in our model for us.
# Analogy: It's like a smart universal remote that already knows all the codes 
# for every TV in the house without you having to program each button manually.
class QuoteSerializer(serializers.ModelSerializer):
    
    # The 'Meta' class is like the "instruction manual" for the serializer.
    # It tells the serializer which model to use and which fields to include.
    class Meta:
        # We tell the serializer to focus on our 'Quote' model.
        model = Quote
        
        # We use '__all__' to tell the serializer to translate every single field 
        # (id, text, author, category, created_at) into JSON.
        # Analogy: This is like telling a translator to translate every single 
        # word in a book, rather than just picking a few chapters.
        fields = '__all__'
