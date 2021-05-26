from .db import db

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    stories_id = db.Column(db.Integer, db.ForeignKey('stories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    story = db.relationship('Story', backref='comments')
    user = db.relationship('User')

    def to_json(self):
        return {
            "id": self.id,
            "body": self.body,
            "stories_id": self.stories_id,
            "users_id": self.user_id
        }