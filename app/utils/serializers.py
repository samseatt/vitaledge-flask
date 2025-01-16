# app/utils/serializers.py
def serialize_object_id(data):
    if "_id" in data:
        data["_id"] = str(data["_id"])
    return data
