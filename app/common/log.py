from logging import config, StreamHandler, Formatter  # noqa: F401
from traceback import format_exception
from json import dumps
from socket import gethostname


def create_logger():
    log_level = "INFO"
    handlers = ["stdout"]

    dict_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"jsonlog": {"()": LogFormatter}},
        "handlers": {
            "stdout": {
                "class": "logging.StreamHandler",
                "formatter": "jsonlog",
                "stream": "ext://sys.stdout",
                "level": log_level,
            }
        },
        "loggers": {"": {"handlers": handlers, "propagate": True, "level": log_level}},
    }
    config.dictConfig(dict_config)


def get_level_num(string_level):
    return {
        "CRITICAL": 2,
        "ERROR": 3,
        "WARNING": 4,
        "INFO": 6,
        "DEBUG": 7,
        "NOTSET": 6,
    }[string_level]


class LogFormatter(Formatter):
    def __init__(self):
        self._env = "prod"
        self._host = gethostname()

    def format(self, record):
        log = {
            "timestamp": record.created,
            "_application": "gs-auto-ml",
            "_environment": self._env,
            "_log_type": "application",
            "host": self._host,
            "level": get_level_num(record.levelname),
            "short_message": str(record.msg),
        }

        if record.levelname == "ERROR" and record.exc_info is not None:
            lines = format_exception(
                record.exc_info[0], record.exc_info[1], record.exc_info[2]
            )
            log["full_message"] = "".join("" + line for line in lines)

        for attr in vars(record):
            if attr[0] == "_":
                log[attr] = getattr(record, attr)

        return dumps(log)
