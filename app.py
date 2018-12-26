from models import Post
from database import Database
from models import Menu, Post, Blog

Database.connect()

menu = Menu()

menu.read_or_write()




