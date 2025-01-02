import os
from uuid import uuid1

def upload_pizza_photo(instance, filename:str)->str:
    ext = filename.split('.')[-1]
    return os.path.join(instance.pizza_shop.name, f'{uuid1()}.{ext}')
