from .base import *  # noqa
from .base import List, env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY", default="unsafe-secret-key")


ALLOWED_HOSTS: List[str] = ["*"]
