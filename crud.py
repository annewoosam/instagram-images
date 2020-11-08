"""CRUD operations."""

from model import db, Instagram_Channel, connect_to_db

import datetime


def create_instagram_channel(channel_name, posts, followers, following, about, first_post_date, date_updated):
   

    instagram_channel = Instagram_Channel(channel_name=channel_name,
                  posts=posts,
                  followers=followers,
                  following=following,
                  about=about,
                  first_post_date=first_post_date,
                  date_updated=date_updated)

    db.session.add(instagram_channel)

    db.session.commit()

    return instagram_channel

def get_instagram_channels():
    """Return all rows of instagram_channels data."""

    return Instagram_Channel.query.all()

 def create_image(channel_name, format, image_url, video_views, hearts, comments, tags, date_posted, date_updated):
   

    image = Image(channel_name=channel_name,
                  format=format,
                  image_url=image_url,
                  video_views=video_views,
                  hearts=hearts,
                  comments=comments,
                  tags=tags,
                  date_posted=date_posted,
                  date_updated=date_updated)

    db.session.add(image)

    db.session.commit()

    return image

def get_images():
    """Return all rows of images data."""

    return Image.query.all()

def create_instagram_comment(channel_name,image_id, comment, commentator, replied, date_posted, date_updated):
   
    instagram_comment = Instagram_Comment(channel_name=channel_name,
                  image_id=image_id,
                  comment=comment,
                  commentator=commentator,
                  replied=replied,
                  date_posted=date_posted,
                  date_updated=date_updated)

    db.session.add(instagram_comment)

    db.session.commit()

    return instagram_comment

def get_instagram_comments():
    """Return all rows of instagram_comments data."""

    return Instagram_Comment.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
