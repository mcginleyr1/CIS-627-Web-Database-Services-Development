#!/bin/python

# monkey patching for gevent
import gevent.monkey
gevent.monkey.patch_all()
from psycogreen.gevent import patch_psycopg
patch_psycopg()

import os
import logging
import sys

from flask.ext.cors import CORS
from flask.ext.script import Manager, Server

from app.utilities.encoders import FlaskJSON
from app.settings import cfg

application = FlaskJSON(__name__)
application.config.update(cfg)
application.logger.addHandler(logging.StreamHandler(sys.stdout))
application.logger.setLevel(cfg['LOGLEVEL'])
logger = application.logger

cors_routes = {
    r"/api/v1/*": {"origins": "*"},
    r"/api/v2/*": {"origins": "*"},
    r"/api/pilot/*": {"origins": "*"}
}

cors = CORS(application, resources=cors_routes)

manager = Manager(application)
manager.add_command(
    "runserver",
    Server(
        host="0.0.0.0",
        port=application.config['API_PORT']
    ))


@application.after_request
def add_header(response):
    response.headers['X-Frame-Options'] = 'ALLOW-FROM https://zodiacmetrics.looker.com'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, private'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = "none"
    return response

import app.handlers.integrations_api
import app.handlers.customer_lookup
import app.handlers.forecasting
import app.handlers.models
import app.handlers.retention_output
import app.handlers.ab_test
import app.handlers.datasets
import app.handlers.forgot_password
import app.handlers.output_utilities
import app.handlers.saved_query
import app.handlers.api
import app.handlers.diagnostics
import app.handlers.health
import app.handlers.pilot_api
import app.handlers.transaction_output
import app.handlers.clv_output
import app.handlers.emaildataset
import app.handlers.integrations_api
import app.handlers.pivot_table
import app.handlers.user
import app.handlers.dau
import app.handlers.looker_embed
import app.handlers.loyalty
import app.handlers.actions


import app.admin as admin
import app.error_handlers

application.register_blueprint(app.handlers.api.admin_api_bp)
application.register_blueprint(app.handlers.ab_test.ab_bp)
application.register_blueprint(app.handlers.pivot_table.piv_bp)
application.register_blueprint(app.handlers.datasets.ds_bp)
application.register_blueprint(app.handlers.emaildataset.email_bp)
application.register_blueprint(app.handlers.health.health_bp)
application.register_blueprint(app.handlers.diagnostics.diag_bp)
application.register_blueprint(app.handlers.models.models_bp)
application.register_blueprint(app.handlers.clv_output.clv_bp)
application.register_blueprint(app.handlers.output_utilities.output_utils_bp)
application.register_blueprint(app.handlers.retention_output.retention_bp)
application.register_blueprint(app.handlers.transaction_output.transaction_bp)
application.register_blueprint(app.handlers.customer_lookup.customer_bp)
application.register_blueprint(app.handlers.pilot_api.pilot_api_bp)
application.register_blueprint(app.handlers.saved_query.query_bp)
application.register_blueprint(app.business_logic.auth.security_bp)
application.register_blueprint(app.handlers.integrations_api.integrations_bp)
application.register_blueprint(app.handlers.user.user_api_bp)
application.register_blueprint(app.handlers.forecasting.forecasting_bp)
application.register_blueprint(app.handlers.forgot_password.fp_bp)
application.register_blueprint(app.handlers.dau.dau_bp)
application.register_blueprint(app.handlers.looker_embed.looker_embed_bp)
application.register_blueprint(app.handlers.loyalty.loyalty_bp)
application.register_blueprint(app.error_handlers.bp)
application.register_blueprint(app.handlers.actions.bp)


# Initialize Admin
admin.register_admin(application)

