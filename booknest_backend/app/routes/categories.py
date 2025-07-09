from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request

blp = Blueprint(
    "Categories",
    "categories",
    url_prefix="/categories",
    description="Endpoints for managing categories/tags for books"
)

# PUBLIC_INTERFACE
@blp.route("/")
class CategoriesListAPI(MethodView):
    """
    List or create book categories/tags (placeholder).
    """
    # PUBLIC_INTERFACE
    def get(self):
        """List categories/tags (placeholder)"""
        # TODO: Fetch categories/tags from DB
        return {"categories": [], "message": "List all categories (placeholder)"}

    # PUBLIC_INTERFACE
    def post(self):
        """Create new category/tag (placeholder)"""
        data = request.get_json()
        # TODO: Create category/tag in DB
        return {"message": "Category created (placeholder)", "category": data}
