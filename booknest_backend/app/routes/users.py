from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request

blp = Blueprint(
    "Users",
    "users",
    url_prefix="/users",
    description="User registration, profile, and management"
)

# PUBLIC_INTERFACE
@blp.route("/register")
class UserRegistrationAPI(MethodView):
    """
    Handles user registration (placeholder).
    """
    # PUBLIC_INTERFACE
    def post(self):
        """
        Register new user.
        Expects JSON body: {username, email, password}
        """
        data = request.get_json()
        # TODO: Validate, hash password, create user in DB
        return {"message": "User registered (placeholder)", "user": data}, 201

# PUBLIC_INTERFACE
@blp.route("/<int:user_id>")
class UserProfileAPI(MethodView):
    """
    Get or update user profile (placeholder).
    """
    # PUBLIC_INTERFACE
    def get(self, user_id):
        """Get user profile by ID (placeholder)"""
        # TODO: Fetch user profile from DB
        return {"user": {"id": user_id, "username": "demo"}}

    # PUBLIC_INTERFACE
    def put(self, user_id):
        """Update user profile (placeholder)"""
        data = request.get_json()
        # TODO: Update user profile in DB
        return {"message": f"User {user_id} updated", "profile": data}
