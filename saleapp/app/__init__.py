from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary


app = Flask(__name__)

app.secret_key = "HJAGSD6ASDGYQ392812B*JHAWD"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote("Admin@123")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8


db = SQLAlchemy(app)
login_manager = LoginManager(app)


cloudinary.config( 
    cloud_name = "dpmek7kuc", 
    api_key = "618252313352959", 
    api_secret = "SxOHYek8KrWbNBOpmnk7upEYmow",
    secure=True
)


