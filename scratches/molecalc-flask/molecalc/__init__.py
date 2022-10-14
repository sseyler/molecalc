import os
import sys

from flask import Flask
from flask.helpers import get_debug_flag

from .config import DevConfig, ProdConfig
from .extensions import db
from . import views


here = os.path.dirname(__file__)
sys.path.append(here)


def create_app(config_object=DevConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(views.bp)


def register_errorhandlers(app):
    # def errorhandler(error):
    #     response = error.to_json()
    #     response.status_code = error.status_code
    #     return response
    #
    # app.errorhandler(InvalidUsage)(errorhandler)
    app.register_error_handler(404, views.page_not_found)


def register_shellcontext(app):
    """Register shell context objects."""
    # def shell_context():
    #     """Shell context objects."""
    #     return {
    #         'db': db,
    #         'User': user.models.User,
    #         'UserProfile': profile.models.UserProfile,
    #         'Article': articles.models.Article,
    #         'Tag': articles.models.Tags,
    #         'Comment': articles.models.Comment,
    #     }
    #
    # app.shell_context_processor(shell_context)
    pass


def register_commands(app):
    """Register Click commands."""
    # app.cli.add_command(commands.mycommand)
    pass


def main():
    """This function returns a Flask application."""
    CONFIG = DevConfig if get_debug_flag() else ProdConfig

    app = create_app(CONFIG)

    return app


if __name__ == "__main__":
    pass
