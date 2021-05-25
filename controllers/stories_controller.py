from flask import Flask, request
import models

def create_story():
    print(request.json)
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

def update_story(id):
    print('okay')
    stories = models.Story.query.filter_by(id=id).first()
    stories.title = request.json["title"],
    stories.story = request.json["story"]
    models.db.session.add(stories)
    models.db.session.commit()
    return {"stories": stories.to_json}


def stories_index():
    stories = models.Story.query.all()
    return { "stories": [s.to_json() for s in stories]}

def stories_delete(id):
    stories = models.Story.query.filter_by(id=id).first()
    models.db.session.delete(stories)
    models.db.session.commit()
    return {"stories": stories.to_json()}

def single_user_stories():
    user = models.User.query.filter_by(id=request.headers['Authorization']).first()
    stories = user.stories
    return { "stories": [s.to_json() for s in stories]}




