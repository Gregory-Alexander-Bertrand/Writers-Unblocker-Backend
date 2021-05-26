from .users_routes import apply_users_routes
from .prompts_routes import apply_prompts_routes
from .stories_routes import apply_stories_routes
from .comments_routes import apply_comments_routes

def apply_routes(app):
    apply_users_routes(app)
    apply_prompts_routes(app)
    apply_stories_routes(app)
    apply_comments_routes(app)
