from flask import Blueprint

import_bp = Blueprint('import', __name__)
main_bp = Blueprint('main', __name__)
search_bp = Blueprint('search', __name__)

# Import routes from the sub-modules
from . import main_routes, import_routes, search_routes
