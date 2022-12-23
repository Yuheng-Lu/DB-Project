from flask.views import MethodView
from flask_smorest import Blueprint


blp = Blueprint("ml", __name__, description="ML Model Demo")


@blp.route("/machine-learning-model")
class Home(MethodView):
    def get(self):
        return {"message": "Try our ML model in this link: https://colab.research.google.com/drive/1dgv2vjAvjnUaMrQa_msUfHqF2WjvZ93X?usp=sharing"}
