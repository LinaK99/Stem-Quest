# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import logging

from flask import Flask, render_template, request, url_for


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("Home.html")

@app.route('/Quiz')
def quiz():
    return render_template('Quiz.html')

@app.route('/Results')
def results():
    return render_template('Results.html')

@app.route('/Logic')
def logic():
    return render_template('Logic.html')

@app.route('/About')
def about():
    return render_template('About.html')

@app.route('/Bio')
def bio():
    return render_template('Bio_EngineerResults.html')

@app.route('/Chem')
def chem():
    return render_template('Chemical_EngineerResults.html')

@app.route('/Civ')
def civ():
    return render_template('Civil_EngineerResults.html')

@app.route('/Computer')
def computerengine():
    return render_template('Computer_EngineerResults.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
