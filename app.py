from flask import Flask
from config.database import engine
from models.base import Base
from routes.animal_routes import animal_bp
from routes.tutor_routes import tutor_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)
app.register_blueprint(tutor_bp)
app.register_blueprint(animal_bp)
app.register_blueprint(auth_bp)

Base.metadata.create_all(engine)

if __name__ == "__main__":
  app.run(debug=True)
