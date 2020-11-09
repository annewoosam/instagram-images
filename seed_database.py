"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb instagram_data')

os.system('createdb instagram_data')

model.connect_to_db(server.app)

model.db.create_all()


# Create YourModelNameLowerCasedHere table's initial data.

with open('data/instagram_channel.json') as f:

    instagram_channel_data = json.loads(f.read())

instagram_channel_in_db = []

for instagram_channel in instagram_channel_data:
    channel_name, posts, followers, following, about, first_post_date, date_updated= (
                                   instagram_channel['channel_name'],
                                   instagram_channel['posts'],
                                   instagram_channel['followers'],
                                   instagram_channel['following'],
                                   instagram_channel['about'],
                                   instagram_channel['first_post_date'],
                                   instagram_channel['date_updated'])

    db_instagram_channel = crud.create_instagram_channel(
                                 channel_name,
                                 posts,
                                 followers,
                                 following,
                                 about,
                                 first_post_date,
                                 date_updated)

    instagram_channel_in_db.append(db_instagram_channel)
#
with open('data/image.json') as f:

    image_data = json.loads(f.read())

image_in_db = []

for image in image_data:
    channel_name, format, image_url, video_views, hearts, comments, tags, date_posted, date_updated= (
                                   image['channel_name'],
                                   image['format'],
                                   image['image_url'],
                                   image['video_views'],
                                   image['hearts'],
                                   image['comments'],
                                   image['tags'],
                                   image['date_posted'],
                                   image['date_updated'])

    db_image= crud.create_image(
                                 channel_name,
                                 format,
                                 image_url,
                                 video_views,
                                 hearts,
                                 comments,
                                 tags,
                                 date_posted,
                                 date_updated)

    image_in_db.append(db_image)

#
with open('data/instagram_comment.json') as f:

    instagram_comment_data = json.loads(f.read())

instagram_comment_in_db = []

for instagram_comment in instagram_comment_data:
    channel_name, image_id, comment, commentator, replied, date_posted, date_updated= (
                                   instagram_comment['channel_name'],
                                   instagram_comment['image_id'],
                                   instagram_comment['comment'],
                                   instagram_comment['commentator'],
                                   instagram_comment['replied'],
                                   instagram_comment['date_posted'],
                                   instagram_comment['date_updated'])

    db_instagram_comment = crud.create_instagram_comment(
                                 channel_name,
                                 image_id,
                                 comment,
                                 commentator,
                                 replied,
                                 date_posted,
                                 date_updated)

    instagram_comment_in_db.append(db_instagram_comment)