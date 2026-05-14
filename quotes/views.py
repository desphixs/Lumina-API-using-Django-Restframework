from rest_framework.views import APIView
from rest_framework.response import Response
# We need to import our model and serializer so the view knows what to display.
from .models import Quote
from .serializers import QuoteSerializer

# An 'APIView' is the most basic way to build an API endpoint in Django.
# Think of a View as the "waiter" in a restaurant. 
# When a customer (the frontend app) makes a request, the waiter (the view) 
# goes to the kitchen (the database), gets the food, and brings it back.
class QuoteList(APIView):
    
    # The 'get' method handles "GET" requests, which are used to "get" data.
    # Analogy: This is like a customer saying "Can I see the menu, please?"
    def get(self, request):
        # 1. We check if the user has asked for a specific "category" in the web address.
        # 'request.query_params' is like a dictionary of all the extra details in the URL.
        # Analogy: This is like a customer saying, "I'd like to see the menu, but 
        # only the 'Desserts' section please."
        category = request.query_params.get('category')

        # 2. We start by looking at all our quotes, but we haven't fetched them yet.
        quotes = Quote.objects.all()

        # 3. If the user DID provide a category, we narrow down our search.
        if category:
            # We use '.filter' to only pick the quotes that match the category.
            # 'category__iexact' means "match the category name exactly, but ignore 
            # if it's uppercase or lowercase (case-insensitive)".
            # Analogy: This is like the waiter flipping through the menus and 
            # only picking out the ones that are labeled 'Desserts'.
            quotes = quotes.filter(category__iexact=category)
        
        # 4. Next, we pass our (possibly filtered) quotes into our serializer (the translator).
        # We set 'many=True' because we are sending a LIST of quotes.
        serializer = QuoteSerializer(quotes, many=True)
        
        # 5. Finally, we return the translated data as a "Response".
        return Response(serializer.data)
