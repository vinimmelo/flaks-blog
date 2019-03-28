from .blog.controllers import blog_blueprint
from .main.controllers import main_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(blog_blueprint)
