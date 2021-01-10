import json
from flask import Response


def object_not_found_by_id(model, field_id):
    """Returns Response, NOT FOUND"""
    msg = {
        'message': f'{model} with ID {field_id} not found.',
    }
    msg = json.dumps(msg)
    return Response(msg,
                    mimetype="application/json",
                    status=404
                    )
