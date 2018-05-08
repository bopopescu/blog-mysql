from app import db # no ololo
from app import app

import view
from posts.blueprint import posts  # importing variable 'posts' from blueprint file

app.register_blueprint(posts, url_prefix='/blog')  # linking variable 'posts' with url '/blog'

if __name__ == '__main__' :
    app.run()