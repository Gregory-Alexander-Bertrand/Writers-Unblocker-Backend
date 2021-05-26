from controllers import comments_controller

def apply_comments_routes(app):
    app.route('/stories/story/<int:id>/comment', methods=["post"])(comments_controller.create_comment)