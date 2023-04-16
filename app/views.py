"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_file
from .models import Posts, Likes, Follows, Users
import os


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/v1/users/{user_id}/posts', methods=['GET'])
def get_userposts():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/users/{user_id}/follow', methods=['POST'])
def follow_user():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/posts', methods=['GET'])
def get_allposts():
    try:
        if request.method == "GET":
            #Retrieve data from the database
            posts = db.session.query(Posts).all()
            data = []
            
            for post in posts:
                data.append ({
                    'id': post.id,
                    'caption': post.caption,
                    'photo': post.photo,
                    'user_id': post.user_id,
                    'created_on': post.created_on
                })
            return jsonify (data=data), 200 
    except:
        return jsonify({"errors": "Request Failed"}), 401

@app.route('/api/v1/posts/{post_id}/like', methods='POST')
def like_post():
    return jsonify(message="This is the beginning of our API")

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404