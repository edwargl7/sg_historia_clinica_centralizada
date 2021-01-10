"""User Types views"""
import json
from database.utils.json_util import json_serial
from flask import request, jsonify, Response
from flask_restful import Resource

# Models
from clinic_history.user_types.models import UserType