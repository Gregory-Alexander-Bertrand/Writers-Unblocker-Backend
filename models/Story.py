from .db import db

class Story(db.Model):
    __tablename__ = 'stories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    story = db.Column(db.String, nullable=False)
    prompts_id = db.Column(db.Integer, db.ForeignKey('prompts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    prompt = db.relationship('Prompt')
    user = db.relationship('User', backref='stories')
    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "story": self.story,
            "prompts_id": self.prompts_id,
            "user_id": self.user_id,
            "comments": [c.to_json() for c in self.comments]
        }
