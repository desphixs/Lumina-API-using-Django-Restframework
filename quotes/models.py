from django.db import models

# A "Model" in Django is like a blueprint for a table in your database.
# Think of it as a spreadsheet where each column has a specific type of data it can hold.
class Quote(models.Model):
    # The 'text' field will store the actual inspirational quote.
    # We use TextField because quotes can be long, and this gives them plenty of space.
    # Analogy: This is the large "message" box on a postcard.
    text = models.TextField()

    # The 'author' field stores the name of the person who said the quote.
    # CharField is for shorter pieces of text, and we set a max_length to keep it tidy.
    # Analogy: This is the "From:" line where you sign your name.
    author = models.CharField(max_length=255)

    # The 'category' field helps us group quotes together (like 'Motivation' or 'Focus').
    # This makes it easy for Sarah's app to ask for specific types of inspiration.
    # Analogy: This is like the "Genre" of a book in a library.
    category = models.CharField(max_length=100)

    # The 'created_at' field automatically records the exact date and time a quote is added.
    # 'auto_now_add=True' tells Django to handle the timestamping for us so we don't have to.
    # Analogy: This is like a "Date Received" stamp on a piece of mail.
    created_at = models.DateTimeField(auto_now_add=True)

    # The __str__ method tells Django how to display a single quote in the admin panel.
    # Without this, it would just show something generic like "Quote object (1)".
    def __str__(self):
        # We return the first 50 characters of the quote text so it's easy to identify.
        # It's like seeing a "preview" of a message in your email inbox.
        return self.text[:50]
