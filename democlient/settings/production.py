from .common import *

ADMIN_ENABLED = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kgg1ds^ellb78u7=qrvi*&pv#vx6%ie_grj7hywxy*+f$i5to2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com','127.0.0.1']

OIDC_PROVIDERS = {
    "fortify-id": {
        "srv_discovery_url": "https://login.staging.fortify-id.com/auth/realms/demo",
        "behaviour": OIDC_DEFAULT_BEHAVIOUR,
        "client_registration": {
            "client_id": "demo-python-client",
            "client_secret": "612c5f0e-588b-4bcf-9b9c-86cb94852d84",
            "redirect_uris": ["https://fortifyid-demo-app.herokuapp.com/openid/callback/login/"],
            "post_logout_redirect_uris": ["https://fortifyid-demo-app.herokuapp.com//openid/callback/logout/"],
            "token_endpoint_auth_method": "client_secret_post",
        }
    }
}
