from flask import Flask, request, render_template
from collections import defaultdict
import stories

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/play')
def form():
    prompts = stories.story.prompts
    return render_template('play.html', prompts = prompts)


@app.route('/finish')
def finish():
    result = request.args.to_dict(flat=False)
    return render_template('finish.html', result = stories.story.generate(result))