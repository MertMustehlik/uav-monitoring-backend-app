class DefaultConfig(object):
    def __init__(self):
        self.DEBUG = True
        self.SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost:3306/uav-task-app'
        self.DATABASE_CONNECT_OPTIONS = {}
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False

configuration = DefaultConfig()