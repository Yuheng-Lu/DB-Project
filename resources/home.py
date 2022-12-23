from flask.views import MethodView
from flask_smorest import Blueprint


blp = Blueprint("home", __name__, description="Home Page")


@blp.route("/")
class Home(MethodView):
    def get(self):
        return {"message": "Welcome! Sorry for not having a user interface, I'm not a frontend developer. But this app fully functions in the backend. Try to throw some requests!"}
