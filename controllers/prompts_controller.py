from flask import Flask, request
import models

def create_prompt():
    prompt = models.Prompt(
        prompt = request.json["prompt"],
        genre = request.json["genre"]
    )
    models.db.session.add(prompt)
    models.db.session.commit()
    return { "prompt": prompt.to_json()}

def prompts_index():
    prompts = models.Prompt.query.all()
    return {"prompts": [p.to_json() for p in prompts]}

