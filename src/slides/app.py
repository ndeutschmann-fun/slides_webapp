"""Instantiation of the barebones Flask app"""
import os
from flask import Flask, redirect, url_for 
import slides
from slides.engine import SlideEngine

template_dir = os.path.join(os.path.dirname(slides.__file__), "pages", "templates")
static_dir = os.path.join(template_dir, "static")
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config.update(EXPLAIN_TEMPLATE_LOADING=True)

engine = SlideEngine()

@app.route("/")
def index():
    return redirect(url_for("editor"))
    