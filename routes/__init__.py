from .users_routes import apply_users_routes
from .prompts_routes import apply_prompts_routes

def apply_routes(app):
    apply_users_routes(app)
    apply_prompts_routes(app)
