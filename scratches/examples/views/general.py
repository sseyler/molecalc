import logging

from flask import Blueprint, request, render_template
from pyramid.view import notfound_view_config, view_config

_logger = logging.getLogger('molecalc:views')


general = Blueprint("", __name__, template_folder='templates', static_folder='static')


# Error Views

@notfound_view_config(renderer='templates/page_404.html')
def not_found(request):
    request.response.status = 404
    return {}


# Static page view

@view_config(route_name='about', renderer='templates/page_about.html')
def about(request):
    """Static about page
    """
    return {}


@view_config(route_name='help', renderer='templates/page_help.html')
def page_help(request):
    """Static help page
    """
    return {}
