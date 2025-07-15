import os
from adt_transformations.adt_01 import transform_adt_a01
from identify_route import identify_transform

Tenants=['epic_north','epic_south']
dir= './incoming'

def process_file(file_path,tenant):
        
        with open(file_path, 'r') as file:
            msg = file.read()
            # print(msg)
            print(f"**************{tenant}**************")

            transform_fn= identify_transform(msg)           
            print(transform_fn)
            bundle = transform_fn(msg)
            # print(bundle)

def poll_once():
    for tenant in Tenants:
        incoming_dir=os.path.join(dir,tenant)

        if not os.path.isdir(incoming_dir):
            os.makedirs(incoming_dir,exist_ok=True)
            continue

        for filename in os.listdir(incoming_dir):
            if not filename.lower().endswith('.hl7'):
                continue
            file_path = os.path.join(incoming_dir, filename)
            if not os.path.isfile(file_path):
                continue        

            process_file(file_path,tenant)

poll_once()
