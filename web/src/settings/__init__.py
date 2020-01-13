import os

env_name = os.getenv('ENV_NAME', 'dev')

if env_name == 'prod':
    from .prod import *
else:
    from .dev import *
