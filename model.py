from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

# test = YourClassNameHereInTitleCaseSingular(channel_name='WinningCheckers', email_date='2020-01-31',number_subscribers = '1', month_end_at='2019-12-31', subscribers='0', views='1', minutes_watched='2', likes='3', comments='4', posts='5', shares='6')

class Instagram_Channel(db.Model):
    """A class for Instagram_Channel."""
    
    __tablename__ = 'instagram_channels'

    channel_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    channel_name = db.Column(db.String)

    posts =  db.Column(db.Integer)

    followers = db.Column(db.Integer)

    following = db.Column(db.Integer)

    about = db.Column(db.String)

    first_post_date = db.Column(db.Date)

    date_updated = db.Column(db.Date)

    def __repr__(self):
        return f'<Instagram_Channel channel_id={self.channel_id} channel_name={self.channel_name}>'

class Image(db.Model):
    """A class for Instagram Images."""
    
    __tablename__ = 'images'

    image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    channel_name = db.Column(db.String)

    format =  db.Column(db.String)

    image_url = db.Column(db.String)

    video_views = db.Column(db.Integer)

    hearts = db.Column(db.Integer)

    comments = db.Column(db.String)

    tags = db.Column(db.String)

    date_posted = db.Column(db.Date)

    date_updated = db.Column(db.Date)

    def __repr__(self):
        return f'<Image Image={self.image_id} channel_name={self.channel_name}>'
        
   class Instagram_Comment(db.Model):
    """A class for Instagram_Comments."""
    
    __tablename__ = 'instagram_comments'

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    channel_name = db.Column(db.String)

    image_id =  db.Column(db.Integer)

    comment = db.Column(db.String)

    commentator = db.Column(db.String)

    replied = db.Column(db.String)

    date_posted = db.Column(db.Date)

    date_updated = db.Column(db.Date)

    def __repr__(self):
        return f'<Instagram_Comment comment_id={self.comment_id} channel_name={self.channel_name}>'



def connect_to_db(flask_app, db_uri='postgresql:///instagram_data', echo=True):
   
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
   
    flask_app.config['SQLALCHEMY_ECHO'] = echo
   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)