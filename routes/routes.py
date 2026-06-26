from services.services import create_member , remove_member , list_member , update_member , get_by_id
from flask import Blueprint , jsonify , request
member_bp = Blueprint("member_bp" , __name__)
@member_bp.route ("/member" , methods=["POST"])
def create():
    response , status = create_member(request.json)
    return jsonify(response) , status
@member_bp.route ("/member/<member_id>" , methods = ["DELETE"])
def delete(member_id):
    response , status = remove_member(member_id)
    return jsonify(response) , status
@member_bp.route ("/member" , methods = ["GET"])
def list_all():
    response , status = list_member()
    print(response)
    print(type(response))
    return jsonify(response) , status
@member_bp.route("/member/<member_id>" , methods = ["PUT"] )
def update(member_id):
    response , status = update_member(request.json ,member_id )
    return jsonify(response) , status
@member_bp.route("/member/<member_id>" , methods = ["GET"])
def get_one(member_id):
    response , status = get_by_id(member_id)
    return jsonify(response) , status


    