access_log_format = "remote!%({X-Forwarded-For}i)s|method!%(m)s|url-path!%(U)s|query!%(q)s|username!%(u)s|protocol!%(H)s|status!%(s)s|response-length!%(b)s|referrer!%(f)s|user-agent!%(a)s|request-time!%(L)s"
accesslog = "-"
logger_class = "rockument.ps_gunicorn_logger.GunicornLogger"
log_level = "warning"
# only works for docker
worker_tmp_dir = "/dev/shm"
# workers=2
# threads=4
worker_class = "gthread"
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-FORWARDED-PROTO': 'https',}