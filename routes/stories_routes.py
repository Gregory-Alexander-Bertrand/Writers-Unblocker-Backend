from controllers import stories_controller

def apply_stories_routes(app):
    app.route('/stories', methods=["POST"])(stories_controller.create_story)
    app.route('/allstories', methods=["Get"])(stories_controller.stories_index)
    app.route('/user/stories', methods=["GET"])(stories_controller.single_user_stories)
    app.route('/stories/story/<int:id>', methods=["DELETE"])(stories_controller.stories_delete)
    app.route('/story/story/<int:id>', methods=["PUT"])(stories_controller.update_story)
   