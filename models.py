from database import Database
import uuid
import datetime

# This is our post class. It sets the properties for all the objects and the methods related to the blog post.
class Post:
    def __init__(self, blog_id, title, content, author, date_created=datetime.datetime.utcnow(), _id=uuid.uuid4().hex):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date_created = date_created
        self._id = _id

# This converts the user's input into JSON data to be inserted into Mongodb
    def json_data(self):
        return {
            '_id': self._id,
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
    def __init__(self,  author, title, description, _id=uuid.uuid4().hex):
        self.author = author
        self.title = title
        self.description = description
        self._id = _id

    def new_post(self):
        title = input("Give your Blog post a title: ")
        content = input("Write something interesting: ")
        post = Post(_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    date_created=datetime.datetime.utcnow())
        post.save_post()

    def save_blog(self):
        Database.insert(collection='blogs',
                        data=self.json_data)

    def json_data(self):
        return{
            'author':self.author,
            'title': self.title,
            'description': self.description,
            '_id': uuid.uuid4().hex
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


class Menu(object):
    def __init__(self):
        self.user_input = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user_input))
        else:
            self._prompt_user_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user_input})
        if blog is not None:
            self.user_blog = Blog.get_blogs(blog['id'])
            return True
        else:
            return False

    def _prompt_user_account(self):
        title = input("Give your Blog a title: ")
        description = input("Describe what your Blog is about: ")
        blog = Blog(author=self.user_input,
                    title=title,
                    description=description,
                    _id=uuid.uuid4().hex
                    )
        blog.save_blog()
        self.user_blog = blog

    def read_or_write(self):
        use_case = input("would you like to read (R) or Write (W)? ")
        if use_case == 'R':
            self._list_blogs()
            self._view_blog()
        elif use_case == 'W':
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find('blogs', {})
        for blog in blogs:
            print("ID: {}, Title: {}, Author {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_of_interest = input("Copy + Paste the blog's ID here: ")
        blogs = Blog.get_blogs(blog_of_interest)
        for post in blogs:
            print("Date: {}, title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))


