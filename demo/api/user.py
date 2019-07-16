from sanic import Blueprint, response
from flask_restful import marshal
from demo.model.user import User, user_fields
from demo.model.util import session


api = Blueprint(__name__)


@api.route('/api/users')
async def get_users(request):
    users = session.query(User).all()
    return response.json(marshal(users, user_fields))

