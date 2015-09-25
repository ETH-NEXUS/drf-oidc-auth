from django.conf import settings
from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'OIDC_AUTH', None)

DEFAULTS = {
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'OIDC_ENDPOINT': None,
    'OIDC_AUDIENCE': 'test',
    # Number of seconds in the past valid tokens can be issued
    'OIDC_LEEWAY': 600,
    # Time before JWKS will be refreshed
    'OIDC_JWKS_EXPIRATION_TIME': 24*60*60
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = (
)

api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
