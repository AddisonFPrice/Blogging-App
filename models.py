from database import Database
import uuid
import datetime

# This is our post class. It sets the properties for all the objects and the methods related to the blog post.
class Post:
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=uuid.uuid4().hex):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date_created = date
        self.id = id

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
    def save_post(self):
        Database.insert(collection='posts',
                        data=self.json_data())

# This method returns data from a single post (hence, .find_one) from Mongodb as "post_object"
    @classmethod
    def get_post(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id': id})
        post_object = cls(**post_data)
        return post_object

    @classmethod
    def get_blog(cls, blog_id):
        blog_data = Database.find(collection='posts', query={'blog_id': blog_id})
        posts_object = cls(**blog_data)
        return posts_object



class Blog:
    def __init__(self,  author, title, description, blog_id, id=uuid.uuid4().hex):
        self.author = author
        self.title = title
        self.description = description
        self.blog_id = blog_id
        self.id = id

    def new_post(self):
        title = input("Give your Blog post a title: ")
        content = input("Write something interesting: ")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=datetime.datetime.utcnow())
        post.save_post()

    def save_post(self):
        Database.insert(collection='blogs',
                        data=self.json_data)

    def json_data(self):
        return{
            'author':self.author,
            'title': self.title,
            'description': self.description,
            'blog_id': self.blog_id,
            'id': uuid.uuid4().hex
        }

    @classmethod
    def get_posts(cls, blog_id):
        posts_data = Database.find(collection='blogs',
                      query={'blog_id': blog_id})
        posts_object = cls(**posts_data)
        return posts_object


    @staticmethod
    def get_blogs(id):
        return [Blog for Blog in Database.find(collection='blogs', query={'blog_id': id})]

    




