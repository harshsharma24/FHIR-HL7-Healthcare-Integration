import uuid
from datetime import datetime
from common_models import PatientData, EncounterData

def parse_segment(msg, segment_name):
    """
    Finds and returns a list of fields for the given segment (e.g., PID, PV1).
    """
    for line in msg.strip().split('\n'):
        if line.startswith(segment_name):
            return line.strip().split('|')
    return []

def transform_adt_a03(msg):
    # --- Parse segments ---
    pid = parse_segment(msg, "PID")
    pv1 = parse_segment(msg, "PV1")

    # --- Patient Fields from PID ---
    identifier = pid[3]  # PID-3: Patient ID
    name_field = pid[5]  # PID-5: Last^First
    last_name, first_name = name_field.split('^')[0:2]
    dob_str = pid[7]     # PID-7: Date of Birth
    gender = "male" if pid[8] == "M" else "female"

    birth_date = datetime.strptime(dob_str, "%Y%m%d")

    patient_id = str(uuid.uuid4())
    patient = PatientData(
        id=patient_id,
        identifier=identifier,
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        birth_date=birth_date
    )

    # --- Encounter Fields from PV1 ---
    admit_str = pv1[44] if len(pv1) > 44 else ''
    discharge_str = pv1[45] if len(pv1) > 45 else ''

    admit_time = datetime.strptime(admit_str, "%Y%m%d%H%M") if admit_str else None
    discharge_time = datetime.strptime(discharge_str, "%Y%m%d%H%M") if discharge_str else None

    encounter = EncounterData(
        id=str(uuid.uuid4()),
        status="finished",
        patient_id=patient_id,
        class_code=pv1[2],  # PV1-2: Patient Class (e.g., 'I')
        admit_time=admit_time,
        discharge_time=discharge_time
    )

    return patient, encounter

# Example usage:
# hl7_msg = """MSH|^~\&|HIS|NorthHealthHosp|EKG|NorthDept|202507130730||ADT^A01|MSG00001N|P|2.5
# PID|1||123456^^^NorthHealthHosp^MR||Doe^John^A||19800515|M
# PV1|1|I|2000^2012^01^NHI|3|||004777^Provider^North^MD"""
# details = transform_adt_a03(hl7_msg)
# import pprint; pprint.pprint(details)