from flask import Flask

from adapters.api.blueprints.v1_bp import v1

# Define blueprints
blueprints = [v1]

def create():
    app = Flask("flask-api")

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app