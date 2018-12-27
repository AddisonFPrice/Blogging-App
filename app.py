from models import Post
from database import Database
from models import Menu, Post, Blog

Database.connect()

menu = Menu()

menu.run_menu()




