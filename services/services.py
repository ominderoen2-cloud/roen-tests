from validators.validators import validate_member_data
from database.database import get_all_members , add_member , delete_member , update_member_data, connect_db
def create_member(data):
    clean_data  = validate_member_data(data) 
    success = add_member(clean_data["id"] , clean_data["name"] , clean_data["credit"])
    if not success:
        return {"message":"user already exists"} , 409
    return {"message":"successfully registered"} , 201
def list_member():
    data = get_all_members()

    print("DATA:", data)
    print("TYPE:", type(data))

    return data, 200
def remove_member(member_id):
    success = delete_member(member_id)
    if not success :
        return {"message":"member not fpound"} , 404
    return {"message":"member successfully deleted"} , 200
def update_member(data ,member_id):
    clean_data , error , status = validate_member_data(data)
    if error:
        return error , status
    success = update_member_data(clean_data["name"] , clean_data["credit"] , member_id)
    if not success:
        return {"message":"not updated"},400
    return {"message":"successfully updated"} , 200
def get_by_id(member_id):
    conn = connect_db()
    cursor = conn.cursor()
    try:
       cursor.execute("SELECT FROM enneclub WHERE id = %s", (member_id,))
    except FileNotFoundError:
        return {"message":"member not found"}
    row = cursor.fetchone()
    if row is None:
       return{ 
        "id":row[0] , "name":row[1] , "credit":row[2]}
        
    

