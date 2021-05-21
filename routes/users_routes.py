from controllers import users_controller

def apply_users_routes(app):
    app.route('/users', methods=["POST"])(users_controller.user_create)
    app.route('/login', methods=["POST"])(users_controller.user_login)