from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class PatientData:
    id: str                      
    identifier: str              
    first_name: str
    last_name: str
    gender: str                  
    birth_date: datetime 

@dataclass
class EncounterData:
    id: str                     
    status: str                  
    patient_id: str              
    class_code: str              
    admit_time: Optional[datetime]
    discharge_time: Optional[datetime]
    encounter_type: Optional[str] = None  

@dataclass
class HL7Context:
    tenant_id: Optional[str]
    message_control_id: Optional[str]
    received_time: datetime