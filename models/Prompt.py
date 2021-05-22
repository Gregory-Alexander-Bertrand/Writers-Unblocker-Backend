from .db import db

class Prompt(db.Model):
    __tablename__ = 'prompts'
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    def to_json(self):
        return {
            "id": self.id,
            "prompt": self.prompt,
            "genre": self.genre
        }