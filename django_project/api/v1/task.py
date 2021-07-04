import json
from celery import shared_task
from core.models import *

@shared_task
def change_status(json_object):
    item_obj = Item.objects.filter(id=json_object["id"]).first()
    if not item_obj:
        return
    item_obj.status = "completed"
    item_obj.save()
    return item_obj.__dict__