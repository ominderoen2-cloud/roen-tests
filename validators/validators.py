def validate_member_data(data , require_id=True):
    member_id = data.get("id")
    name = data.get("name")
    credit_score = data.get("credit")
    if require_id :
        if not member_id or not name or credit_score is None :
            return None , {"message":"missing fields "} , 400
        try :
            credit_score = int(credit_score)
        except ValueError :
            return None , {"message" : "credit must be a number"} , 400
    return {
        "id":member_id , "name":name , "credit":credit_score
    }
        