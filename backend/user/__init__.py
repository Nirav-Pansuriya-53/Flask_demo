from flask_smorest import Blueprint

function_base_user = Blueprint("function_base_user", __name__)
class_base_user = Blueprint("class_base_user", __name__)


# Importing user_apis and models to avoid circular imports

from . import class_base_user_apis, funcation_base_user_apis, models
