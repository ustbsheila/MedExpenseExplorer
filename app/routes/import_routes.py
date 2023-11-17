from importdata.dataImporter import start_data_import_process
from . import import_bp


@import_bp.route('/import')
def import_data():
    res = "============Importing Open Payments Datasets.============\n"
    res += start_data_import_process()

    return res
