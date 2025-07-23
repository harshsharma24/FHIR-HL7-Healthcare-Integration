from adt_transformations.adt_01 import transform_adt_a01
from adt_transformations.adt_03 import transform_adt_a03
from x12_transormations.x12_834 import transform_834

def identify_transform(msg):
    # Basic format detection
    if msg.startswith("ISA*"):
        if "834" in msg:
            return transform_834
        else:
            raise ValueError("Unsupported X12 transaction")
    elif msg.startswith("MSH|"):
        if "ADT^A01" in msg:
            return transform_adt_a01
        elif "ADT^A03" in msg:
            return transform_adt_a03
        else:
            raise ValueError("Unsupported HL7 message type")
    else:
        raise ValueError("Unknown message format")

print("\n--- Running identify_transform tests ---")

msg_adt_a01 = """MSH|^~\\&|EPIC|NorthHealthHosp|ADT|EPICDEPT|202507130730||ADT^A01|MSG00001|P|2.5
PID|1||123456^^^NorthHealthHosp^MR||Doe^John^A||19800515|M
PV1|1|I|2000^2012^01^NHI|3|||004777^Provider^North^MD"""
print("ADT^A01:", identify_transform(msg_adt_a01))

msg_adt_a03 = """MSH|^~\\&|EPIC|NorthHealthHosp|ADT|EPICDEPT|202507130730||ADT^A03|MSG00002|P|2.5
PID|1||789012^^^NorthHealthHosp^MR||Smith^Robert^B||19720620|M
PV1|1|I|2000^305^01^NHI|3|||005888^Physician^Grey^MD"""
print("ADT^A03:", identify_transform(msg_adt_a03))

msg_834 = """ISA*00*          *00*          *ZZ*BLUESHIELD     *ZZ*ASHHEALTH      *240719*0800*^*00501*000000905*1*T*:~
GS*BE*BLUESHIELD*ASHHEALTH*20240719*0800*1*X*005010X220A1~
ST*834*0001~
BGN*00*ENROLL20240719*20240719*0800*PT**4~"""
print("834:", identify_transform(msg_834))