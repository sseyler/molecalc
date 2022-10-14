import logging

import models
from flask import Blueprint, request, render_template
from pyramid import httpexceptions
from pyramid.view import notfound_view_config, view_config

from molecalc_lib import gamess_results

_logger = logging.getLogger('molecalc:views')

calc = Blueprint("", __name__, template_folder='templates', static_folder='static')


@view_config(route_name="calculation", renderer="templates/page_calculation.html")
def view_calculation(request):
    """View for looking up calculations."""

    # Get the key
    matches = request.matchdict
    hashkey = matches["one"]

    print(matches)

    # Look up the key
    calculation = (
        request.dbsession.query(models.GamessCalculation)
        .filter_by(hashkey=hashkey)
        .first()
    )

    if calculation is None:
        raise httpexceptions.exception_response(404)

    if hashkey == "404":
        raise httpexceptions.exception_response(404)

    data = gamess_results.view_gamess_calculation(calculation)

    return data
