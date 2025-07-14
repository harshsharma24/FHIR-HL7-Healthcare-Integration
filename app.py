import os

Tenants=['epic_north','epic_south']
dir= './incoming'

def process_file(incoming_dir):
    for filename in os.listdir(incoming_dir):
        file_path= os.path.join(incoming_dir, filename)
        
        if not os.path.isfile(file_path):
            continue

        if not filename.endswith('.hl7'):
            continue
        
        print(f"{filename}")

        file = open(file_path, 'r')
        print(file.read())
        file.close()

def poll_once():
    for tenant in Tenants:
        incoming_dir=os.path.join(dir,tenant)

        if not os.path.isdir(incoming_dir):
            os.makedirs(incoming_dir,exist_ok=True)
            continue

        try:
            process_file(incoming_dir)
        
        except Exception as e:
            print(f"Error- {e}")

poll_once()
