from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

debug = DebugToolbarExtension(app)


@app.route('/')
def home_form():
    """Shows form to request words"""

    prompts = story.prompts

    return render_template('questions.html', prompts=prompts)


@app.route('/story')
def show_story():
    """Shows story result"""

    text = story.generate(request.args)

    return render_template('story.html', text=text)




