from controllers import prompts_controller

def apply_prompts_routes(app):
    app.route('/prompt', methods=["POST"])(prompts_controller.create_prompt)
    app.route('/prompts', methods=["GET"])(prompts_controller.prompts_index)