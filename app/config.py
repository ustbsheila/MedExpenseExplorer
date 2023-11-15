class Config:
    # Flask app configuration
    DEBUG = True  # Set to False in production

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ustbsheila:12345@localhost:3306/openpaymentdb'  # Local development
    SQLALCHEMY_ECHO = True