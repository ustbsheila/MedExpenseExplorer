class Config:
    # Flask app configuration
    DEBUG = True  # Set to False in production

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ustbsheila:12345@localhost:3306/openpaymentdb'  # Local development
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Set your secret key here
    SECRET_KEY = 'a7056ecc939cb8483f9812a426e441b7'