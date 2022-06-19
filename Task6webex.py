import requests 
import json 

access_token = "OTgwYTNlODEtMTlhZS00MDI5LTliOGQtMDAzZTAzOGEyNzAxZmUwYjZmYTgtYWU4_P0A1_5998ff09-9c27-4407-818f-2305709e8d49"

groups_struc = {
 "groups": [
      { "group": { "group_name": "devasc_skills_NB" ,    
                   "members": [   
                     {"person_name": "Yvan", "email": "yvan.rooseleer@biasc.be"},
                     {"person_name": "Nawfal", "email": "nawfal.bourass@student.odisee.be"},
                     ]
                 }
      }
   ]
}

url = 'https://api.ciscospark.com/v1/rooms'

headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
for rec in groups_struc["groups"]:
    create_group_name = rec["group"]["group_name"]
    print("Creating ... " + create_group_name)
    payload_space={"title": create_group_name}
    res_space = requests.post(url, headers=headers, json=payload_space)

    
    for mbr in rec["group"]["members"]:
        
        person_email = mbr["email"] 
        url2 = 'https://api.ciscospark.com/v1/memberships'
        payload_member = {'personEmail': person_email}
        res_member = requests.post(url2, headers=headers, json=payload_member)