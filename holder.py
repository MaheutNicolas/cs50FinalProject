import os

global link
path = os.path.dirname(os.path.abspath(__file__))
link = os.path.join(path, 'cardGame.db')
