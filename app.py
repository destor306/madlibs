from flask import Flask, request,  render_template
from stories import stories
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
# this is necessary to do DebugToolbarExtension
app.config['SECRET_KEY'] = "jasonyoo"
debug = DebugToolbarExtension(app)


@app.route('/')
def _home():
    # we are getting dictionaries values and sending it to select.html
    stories_dict = stories.values()
    return render_template("select.html", stories=stories_dict)


@app.route('/question')
def _question():
    # we got input queries from select.html
    # Retrieving story.title to get dictionary values.
    title = request.args["story_id"]
    story = stories[title]
    prompts = story.prompts
    # sending prompts and title to question.html
    return render_template("question.html", prompts=prompts, title=title)


@app.route('/story')
def _story():
    title = request.args["story_id"]
    story = stories[title]
    text = story.generate(request.args)

    return render_template("story.html", text=text, title=title)
