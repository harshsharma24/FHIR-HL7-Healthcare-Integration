import pprint

def transform_adt_a01(msg: str) -> dict:
    # Split into lines, then fields
    segments= [line.split('|') for line in msg.strip().split('\n')]
    # print(segments)

    #Locate segments we care about
    msh= next(seg for seg in segments if seg[0]== 'MSH')
    pid= next(seg for seg in segments if seg[0]== 'PID')
    pv1= next(seg for seg in segments if seg[0]== 'PV1')

    # print(f"msh: {msh}")
    # print(f"pid: {pid}")
    # print(f"pv1: {pv1}")

    admit_ts=msh[6]
    message_type=msh[8]
    patient_id= pid[3].split('^')[0]
    name_parts=pid[5].split('^')
    family_name= name_parts[0]
    given_name= name_parts[1]
    dob=pid[7]
    gender_code=pid[8]
    patient_class=pv1[2]
    location=pv1[3]

    json_data={
        "message_type" : message_type,
        "admitDateTime" : f"{admit_ts[:4]}-{admit_ts[4:6]}-{admit_ts[6:8]}T{admit_ts[8:10]}:{admit_ts[10:]}:00",
        "patient" : {
            "id" : patient_id,
            "name" :  { 
                "family": family_name, "given" : given_name,
            "birth_date" : f"{dob[:4]}-{dob[4:6]}-{dob[6:8]}",
            "gender" : "male" if gender_code == 'M' else "female"
            },
            "visit" : {
                "class" : patient_class,
                "location": location
            }
        }
    }
    pprint.pprint(json_data)
    return json_data

# # Example usage:
# hl7_msg = """MSH|^~\&|HIS|NorthHealthHosp|EKG|NorthDept|202507130730||ADT^A01|MSG00001N|P|2.5
# PID|1||123456^^^NorthHealthHosp^MR||Doe^John^A||19800515|M
# PV1|1|I|2000^2012^01^NHI|3|||004777^Provider^North^MD"""
# details = transform_adt_a01(hl7_msg)
# import pprint; pprint.pprint(details)