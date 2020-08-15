from pyramid.config import Configurator
from logger.log import logger
from src.get_big_query import upload_csv,create_data_Set,create_schema
import configparser

try:
    config = configparser.ConfigParser()
    config.read("config/config.ini")
    http_host = config.get("HTTP", "host")
    http_port = int(config.get("HTTP", "port"))
except Exception as e:
    logger.error(msg="Error occured while reading configuration from config file", exc_info=True)


def xmpp_start():
    try:


        with Configurator() as config:
            config.add_request_method(upload_csv, 'upload_csv', reify=True)
            config.add_request_method(create_data_Set, 'create_data_Set', reify=True)
            config.add_route('upload_csv', '/upload_csv/')
            config.add_route('create_data_Set', '/create_data_Set')
            config.add_view(upload_csv, route_name='fbbot', renderer='json', request_method=("POST", "GET"))
            config.add_view(create_data_Set, route_name='healthCheck', renderer='json', request_method=("POST", "GET"))

            app = config.make_wsgi_app()

        logger.info("initializing xmpp server...")
        logger.info("Server is running on {0}:{1}".format(http_host, str(http_port)))
        server = make_server(http_host, http_port, app)
        server.serve_forever()
    except Exception as e:
        logger.error(msg ="Error while running server",exc_info=True)
