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
        # 1. First, we go to the database and grab every single Quote we have.
        # Analogy: This is like the waiter gathering all the menus from the kitchen.
        quotes = Quote.objects.all()
        
        # 2. Next, we pass those quotes into our serializer (the translator).
        # We set 'many=True' because we are sending a LIST of quotes, not just one.
        # Analogy: This is like the waiter handing the menus to a translator 
        # so they can be written in a language the customer understands.
        serializer = QuoteSerializer(quotes, many=True)
        
        # 3. Finally, we return the translated data as a "Response".
        # Analogy: The waiter brings the translated menus back to the customer's table.
        return Response(serializer.data)
