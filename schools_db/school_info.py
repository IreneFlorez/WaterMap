from schools_db import School
import json

#Total Database Items check
total_db_items = len([row.school for row in School.query.all()])
print(total_db_items)

# schools set and schools list
schools_set = set([row.school for row in School.query.all()])
schools_list = [x for x in schools_set]

# get a school name from schools list
school_1 = schools_list[1]

# Create school object 
def create_school_db_obj(school_name):
    return School.query.filter_by(school=school_name).all()[0]

def create_json_object(db_obj):
    data = {}
    data["nces_dist_id"] = db_obj.nces_dist_id
    data["status"] = db_obj.status
    data["county"] = db_obj.county
    data["district"] = db_obj.district
    data["school"] = db_obj.school
    data["street"] = db_obj.street
    data["city"] = db_obj.city
    data["zip"] = db_obj.zip
    data["state"] = db_obj.state
    data["address"] = db_obj.address
    data["phone"] = db_obj.phone
    data["web"] = db_obj.web
    data["admin_first_name"] = db_obj.admin_first_name
    data["admin_last_name"] = db_obj.admin_last_name
    data["admin_email"] = db_obj.admin_email
    data["last_update"] = db_obj.last_update
    return json.dumps(data)

def school_info(school_name):
    school_obj = create_school_db_obj(school_name)
    return create_json_object(school_obj)

# Test code below
# test_json = school_info(school_1)
# print(json.loads(test_json))