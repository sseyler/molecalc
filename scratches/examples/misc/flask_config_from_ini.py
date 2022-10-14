def config_from_ini(app, config_file = None, section='flask'):
    """
    Configure Flask from an INI file
    Parameters:
        app         - Flask application instance
        config_file - Path to the configuration file (INI format)
        section     - Section name to load key/values from
    """
    if config_file is None:
        config_file = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
    logging.debug('Loading Flask configuration from %s' % config_file)
    config = configparser.ConfigParser()
    config.read(config_file)
    flask_config = dict(config.items(section))
    for cfg_key in flask_config:
        app.config[cfg_key.upper()] = flask_config[cfg_key]`

######################################################################################
# Usage example:
# ------ config.ini -----
# [flask]
# DEBUG = True
# ENV = Development
#
# ------ app.py -----
# from flask import Flask
# app = Flask(__name__)
# config_from_ini(app, config_file='config.ini', section='flask')
# app.run()