import uuid
from datetime import datetime
from common_models import PatientData, EncounterData

def transform_adt_a01(msg):
    # Split into lines, then fields
    segments = [line.split('|') for line in msg.strip().split('\n')]

    # Locate segments
    msh = next(seg for seg in segments if seg[0] == 'MSH')
    pid = next(seg for seg in segments if seg[0] == 'PID')
    pv1 = next(seg for seg in segments if seg[0] == 'PV1')

    # Extract fields
    admit_ts = msh[6]  # MSH-7: Date/Time of Message
    message_type = msh[8]

    patient_identifier = pid[3].split('^')[0]  # PID-3: Patient ID
    name_parts = pid[5].split('^')             # PID-5: Last^First
    family_name = name_parts[0]
    given_name = name_parts[1] if len(name_parts) > 1 else ""
    dob = datetime.strptime(pid[7], "%Y%m%d")  # PID-7: DOB
    gender = "male" if pid[8] == 'M' else "female"

    patient_id = str(uuid.uuid4())  # UUID for internal reference

    # Construct PatientData
    patient = PatientData(
        id=patient_id,
        identifier=patient_identifier,
        first_name=given_name,
        last_name=family_name,
        gender=gender,
        birth_date=dob
    )

    # Encounter info
    admit_time = datetime.strptime(admit_ts, "%Y%m%d%H%M")
    patient_class = pv1[2]
    # discharge_time will be None in A01
    encounter_id = str(uuid.uuid4())

    encounter = EncounterData(
        id=encounter_id,
        status="in-progress",         # A01 = admitted
        patient_id=patient_id,
        class_code=patient_class,
        admit_time=admit_time,
        discharge_time=None
    )

    return patient, encounter

# Example usage:
# hl7_msg = """MSH|^~\&|HIS|NorthHealthHosp|EKG|NorthDept|202507130730||ADT^A01|MSG00001N|P|2.5
# PID|1||123456^^^NorthHealthHosp^MR||Doe^John^A||19800515|M
# PV1|1|I|2000^2012^01^NHI|3|||004777^Provider^North^MD"""
# details = transform_adt_a01(hl7_msg)
# import pprint; pprint.pprint(details)