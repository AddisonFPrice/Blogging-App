from models import Post
from database import Database

Database.connect()

post1 = Post(title="The Rain King", content="He is a king.", author="Addison Price")

print(post1.title, post1.content)


