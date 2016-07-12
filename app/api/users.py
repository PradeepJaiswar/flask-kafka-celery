"""
 Simple API endpoint for returning users
"""
from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify, make_response)


users = Blueprint('users', __name__, url_prefix='/api/users')


@users.route('/', methods=['GET'])
def index():

   data = {
      'a' : "A",
      'b' : "B",
      'c' : "C",
   }
   return make_response(jsonify(data))
