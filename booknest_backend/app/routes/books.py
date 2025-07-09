from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request

blp = Blueprint(
    "Books",
    "books",
    url_prefix="/books",
    description="CRUD operations and filtering for books"
)

# PUBLIC_INTERFACE
@blp.route("/")
class BooksListAPI(MethodView):
    """
    Handles listing and creating books.
    """
    # PUBLIC_INTERFACE
    def get(self):
        """
        Get all books with optional filtering, search, pagination.

        Query params:
        - q: search term
        - category: filter by category
        - tag: filter by tag(s)
        - page/limit: for pagination

        Returns: JSON list of books (placeholder)
        """
        # TODO: Implement actual database query/filtering
        return {"books": [], "message": "Book list endpoint – filtering/search not yet implemented"}

    # PUBLIC_INTERFACE
    def post(self):
        """
        Create a new book (placeholder).
        Expects JSON body with book info.
        """
        data = request.get_json()
        # TODO: Validate and create book in DB
        return {"message": "Book created", "book": data}, 201


# PUBLIC_INTERFACE
@blp.route("/<int:book_id>")
class BookDetailAPI(MethodView):
    """
    Handles getting, updating, deleting a single book.
    """
    # PUBLIC_INTERFACE
    def get(self, book_id):
        """Retrieve book by ID (placeholder)"""
        # TODO: Fetch book from DB by ID
        return {"message": f"Get book {book_id}", "book": None}

    # PUBLIC_INTERFACE
    def put(self, book_id):
        """Update a book (placeholder)"""
        data = request.get_json()
        # TODO: Validate data and update book in DB
        return {"message": f"Book {book_id} updated", "book": data}

    # PUBLIC_INTERFACE
    def delete(self, book_id):
        """Delete a book (placeholder)"""
        # TODO: Delete book from DB
        return {"message": f"Book {book_id} deleted"}
