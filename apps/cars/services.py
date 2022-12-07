import os.path
from uuid import uuid1


def upload_photo(instance, file: str) -> str:
    ext = file.split('.')[-1]
    # return os.path.join(instance.name,'photo', f'{uuid1()}.{ext}')
    return os.path.join(f'{instance.name+"_id_"+str(instance.id)}','photo', f'{uuid1()}.{ext}')

