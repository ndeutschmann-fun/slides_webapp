from flask import render_template, redirect, url_for, request
from slides.app import app, engine

@app.route("/editor")
def editor():
    return render_template("editor.html", engine=engine)

@app.route("/editor_submit", methods=['POST'])
def editor_submit():
    result = request.form
    new_content = result["editor"]
    engine.set_content(new_content)
    return redirect(url_for("render"))