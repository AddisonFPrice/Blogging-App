from database import Database
import uuid
import datetime

# This is our post class. It sets the properties for all the objects and the methods related to the blog post.
class Post:
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date_created = date
        self.id = uuid.uuid4().hex if id is None else id

# This converts the user's input into JSON data to be inserted into Mongodb
    def json_data(self):
        return {
            'post_id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'date_created': self.date_created
        }

# This method inserts the JSON data created above into Mongodb
    def insert(self):
        Database.insert(collection='posts',
                        data=self.json_data())

# This method returns data from a single post (hence, .find_one) from Mongodb as "post_object"
    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id': id})
        post_object = cls(**post_data)
        return post_object

