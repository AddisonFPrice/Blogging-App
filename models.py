from database import Database

class Post:
    def __init__(self, blog_id, title, content, author, date, id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date_created = date
        self.id = id

    def json_data(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'date_created': self.date_created
        }

    def insert(self):
        Database.insert(collection='posts',
                        data=self.json_data())

    @classmethod
    def from_mongo(cls, post_id):
        post_data = Database.find_one(collection='posts', query={'_id': post_id})
        post_object = cls(**post_data)
        return post_object

