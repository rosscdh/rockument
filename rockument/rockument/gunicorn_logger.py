import logging
from gunicorn import glogging


class NoHealthCheckFilter(logging.Filter):
    def filter(self, record):
        return (record.getMessage().find('user-agent!ELB-HealthChecker') == -1 and record.getMessage().find('/health') == -1)


class GunicornLogger(glogging.Logger):

    def setup(self, cfg):
        super().setup(cfg)
        # Add filters to Gunicorn logger
        logger = logging.getLogger("gunicorn.access")
        logger.addFilter(NoHealthCheckFilter())