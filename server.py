"""Server for YourFolder app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Instagram_Channel, Image, Instagram_Comment, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_instagram_channels():

    stats=crud.get_instagram_channels()
    
    channel_id=[q[0] for q in db.session.query(Instagram_Channel.channel_id).all()]

    channel_name=[q[0] for q in db.session.query(Instagram_Channel.channel_name).all()]
     
    posts=[q[0] for q in db.session.query(Instagram_Channel.posts).all()]

    followers=[q[0] for q in db.session.query(Instagram_Channel.followers).all()]

    following=[q[0] for q in db.session.query(Instagram_Channel.following).all()]

    about=[q[0] for q in db.session.query(Instagram_Channel.about).all()]

    first_post_date=[q[0] for q in db.session.query(Instagram_Channel.first_post_date).all()]
      
    date_updated=[q[0] for q in db.session.query(Instagram_Channel.date_updated).all()]

    return render_template('instagram_channels.html', channel_id=channel_id, channel_name=channel_name, posts=posts, followers=followers, following=following, about=about, first_post_date=first_post_date, date_updated=date_updated)

@app.route('/images')

def all_instagram_channels():

    stats=crud.get_instagram_channels()
    
    image_id=[q[0] for q in db.session.query(Instagram_Channel.image_id).all()]

    channel_name=[q[0] for q in db.session.query(Instagram_Channel.channel_name).all()]
     
    format=[q[0] for q in db.session.query(Instagram_Channel.format).all()]

    image_url=[q[0] for q in db.session.query(Instagram_Channel.image_url).all()]

    video_views=[q[0] for q in db.session.query(Instagram_Channel.video_views).all()]

    hearts=[q[0] for q in db.session.query(Instagram_Channel.hearts).all()]

    comments=[q[0] for q in db.session.query(Instagram_Channel.comments).all()]

    tags=[q[0] for q in db.session.query(Instagram_Channel.tags).all()]

    date_posted=[q[0] for q in db.session.query(Instagram_Channel.date_posted).all()]

    date_updated=[q[0] for q in db.session.query(Instagram_Channel.date_updated).all()]

    return render_template('images.html', image_id=image_id, channel_name=channel_name, format=format, image_url=image_url, video_views=video_views, hearts=hearts, comments=comments, tags=tags, date_posted=date_posted, date_updated=date_updated)

@app.route('/comments')

def all_instagram_comments():

    stats=crud.get_instagram_comments()
    
    comment_id=[q[0] for q in db.session.query(Instagram_Comment.comment_id).all()]

    channel_name=[q[0] for q in db.session.query(Instagram_Comment.channel_name).all()]
     
    image_id=[q[0] for q in db.session.query(Instagram_Comment.image_id).all()]

    comment=[q[0] for q in db.session.query(Instagram_Comment.comment).all()]

    commentator=[q[0] for q in db.session.query(Instagram_Comment.commentator).all()]

    replied=[q[0] for q in db.session.query(Instagram_Comment.replied).all()]

    date_posted=[q[0] for q in db.session.query(Instagram_Comment.date_posted).all()]
      
    date_updated=[q[0] for q in db.session.query(Instagram_Comment.date_updated).all()]

    return render_template('instagram_comments.html', comment_id=comment_id, channel_name=channel_name, image_id=image_id, comment=comment, commentator=commentator, replied=replied, date_posted=date_posted, date_updated=date_updated)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()