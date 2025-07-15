
from adt_transformations.adt_01 import transform_adt_a01

transformers={
    "ADT^A01" : transform_adt_a01
}

def identify_transform(msg):
    for key, func in transformers.items():
        if key in msg:
            return func
    raise Exception ("No Transform found")

        

    