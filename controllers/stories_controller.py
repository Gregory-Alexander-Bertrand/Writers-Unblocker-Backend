from flask import Flask, request
import models

def create_story():
    user = models.User.query.filter_by(id=request.headers['Authorization']).first()
    prompt = models.Prompt.query.filter_by(id=request.json['prompt_id']).first()
    story = models.Story(
        title = request.json["title"],
        story = request.json["story"],
        user = user,
        prompt = prompt
    )
    models.db.session.add(story)
    models.db.session.commit()
    return{ "story": story.to_json()}