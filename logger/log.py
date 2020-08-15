import logging.config


logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s {%(filename)s:%(funcName)s:%(lineno)d} [%(levelname)s] : %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'my.packg': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
    }
})
logger = logging.getLogger(__name__)