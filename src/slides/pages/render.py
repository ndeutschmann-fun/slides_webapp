from flask import render_template
from slides.app import app, engine

@app.route("/render")
def render():
    return render_template("slide.html", content=engine.content)