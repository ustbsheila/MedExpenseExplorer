from flask import Blueprint

import_bp = Blueprint('import', __name__)
main_bp = Blueprint('main', __name__)

# Import routes from the sub-modules
from . import main_routes, import_routes