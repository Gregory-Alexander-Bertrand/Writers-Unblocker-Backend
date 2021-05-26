from flask import Flask, request
import models

def create_comment(id):
    user = models.User.query.filter_by(id=request.headers['Authorization']).first()
    story = models.Story.query.filter_by(id=id).first()
    comment = models.Comment(
        body = request.json["body"],
        user = user,
        story = story
    )
    models.db.session.add(comment)
    models.db.session.commit()
    return{ "comment": comment.to_json()}