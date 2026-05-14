# We import 'Q' from Django's database models. 
# Think of 'Q' as a "Search Query" tool that lets us ask more complex questions 
# to the database, like "Find me quotes that mention 'Success' OR 'Failure'".
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
# We need to import our model and serializer so the view knows what to display.
from .models import Quote
from .serializers import QuoteSerializer

# An 'APIView' is the most basic way to build an API endpoint in Django.
# Think of a View as the "waiter" in a restaurant. 
class QuoteList(APIView):
    
    # The 'get' method handles "GET" requests, which are used to "get" data.
    # Analogy: This is like a customer saying "Can I see the menu, please?"
    def get(self, request):
        # 1. We check if the user has asked for a specific "category" in the URL.
        # Analogy: "I'd like to see the 'Desserts' section please."
        category = request.query_params.get('category')

        # 2. We also check if the user has asked for a specific "search" word in the URL.
        # Analogy: "I'm looking for anything that has the word 'Chocolate' in it."
        search = request.query_params.get('search')

        # 3. We start by looking at all our quotes.
        quotes = Quote.objects.all()

        # 4. If the user provided a category, we filter the list.
        if category:
            # 'category__iexact' matches the name exactly, ignoring capitalization.
            quotes = quotes.filter(category__iexact=category)
        
        # 5. If the user provided a search word, we filter the list again!
        if search:
            # We use 'Q' objects with the '|' symbol, which means "OR".
            # 'text__icontains' means "does the quote text contain this word?"
            # 'author__icontains' means "does the author name contain this word?"
            # Analogy: "Find me quotes where the TEXT mentions 'success' OR 
            # the AUTHOR name mentions 'success'."
            quotes = quotes.filter(
                Q(text__icontains=search) | Q(author__icontains=search)
            )
        
        # 6. Next, we pass our (possibly double-filtered!) quotes into our serializer.
        serializer = QuoteSerializer(quotes, many=True)
        
        # 7. Finally, we return the translated data as a "Response".
        return Response(serializer.data)
