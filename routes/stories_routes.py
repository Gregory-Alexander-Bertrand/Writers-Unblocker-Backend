from controllers import stories_controller

def apply_stories_routes(app):
    app.route('/stories', methods=["POST"])(stories_controller.create_story)