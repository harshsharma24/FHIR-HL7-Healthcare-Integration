
from adt_transformations.adt_01 import transform_adt_a01
from adt_transformations.adt_03 import transform_adt_a03

transformers={
    "ADT^A01" : transform_adt_a01,
    "ADT^A03": transform_adt_a03
}

def identify_transform(msg):
    for key, func in transformers.items():
        if key in msg:
            return func
    raise Exception ("No Transform found")

        

    