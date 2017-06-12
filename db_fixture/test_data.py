import sys
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB



# create data
datas = {
    'luc_users':[
        {'username': 'yayatest', '`password`': '279f1abf531fe88e7c51781635ea6720', 'pass_salt': 44143, 'status': 20, 'employee_id': 0,'login_times': 0, 'last_failed_login_times': 0},

    ]
}


# Inster table datas
def init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
