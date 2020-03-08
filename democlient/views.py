from djangooidc import views as oidcviews
from django.http import QueryDict


def authz_cb(request):
    try:
        return oidcviews.authz_cb(request)
    finally:
        # Clean up the session to avoid automatically prompting the users
        # to authenticate after they logged out
        if 'next' in request.session:
            request.session['next'] = '/'

def openid(request, op_name=None):
    if not 'next' in request.GET.keys() and 'next' in request.session:
        # request.GET dict is immutable so to modify its contents
        # we perform a deepcopy and modify the copy 
        copy = request.GET.copy()
        copy['next'] = request.session['next']
        request.GET = copy
    return oidcviews.openid(request, op_name=op_name)