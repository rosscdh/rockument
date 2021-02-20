from jslog4kube import LOGGING
from logging.config import dictConfig

LOGGERS = {
    "default": {
        "handlers": ["json-stdout"],
        "formatters": ["json"],
        "propagate": True,
        "level": "DEBUG",
    },
    "rq.worker": {
        "handlers": ["json-stdout"],
        "formatters": ["json"],
        "propagate": True,
        "level": "DEBUG",
    },
}


LOGGING["loggers"].update(LOGGERS)

dictConfig(LOGGING)