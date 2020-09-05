import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

STATIC_FOLDER = os.path.join(BASE_DIR, "frontend/build")

TEMPLATES_FOLDER = os.path.join(BASE_DIR, "frontend/templates")




class TestConfig():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@127.0.0.1:3306/test"

#
# template = r"C:\Users\Administrator\Desktop\mall_4\frontend\template"
# static = r"C:\Users\Administrator\Desktop\mall_4\frontend\build"


class ProdConfig():
    DEBUG = False
