from flask import Blueprint, render_template

from monocker_api.api.restplus import restplus_api
from monocker_api.api.models import getFreshModels

#==============================================================================
# Models API 
#==============================================================================
# define namespace
bp = Blueprint('monocker_ui', __name__)

#set default route
@bp.route('/')
def index():
  return render_template('index.html', models=getFreshModels())

#==============================================================================
