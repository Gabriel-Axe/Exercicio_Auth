from flask import Flask
from config.database import engine
from models.base import Base
from routes.tutor_routes import tutor_bp
from routes.vet_routes import vet_bp

app = Flask(__name__)
app.register_blueprint(tutor_bp)
app.register_blueprint(vet_bp)

Base.metadata.create_all(engine)

if __name__ == "__main__":
  app.run(debug=True)
