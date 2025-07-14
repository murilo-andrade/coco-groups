from ultralytics import YOLO
from translate import pt_br # uncomment this line if you need class names in portuguese
import os
from dotenv import load_dotenv

load_dotenv()

def get_label(cls_id):
    model = YOLO(os.getenv('YOLO_MODEL'))  # I am using nano just to get the class names, no detection is done here

    # Lista das classes COCO
    coco_classes = model.names  # dict {id: nome}
    label = coco_classes[cls_id]
    try:
        pt_br = globals()["pt_br"]
        if isinstance(pt_br, dict):
            label = pt_br.get(coco_classes[cls_id],coco_classes[cls_id])
    except KeyError:
        label = coco_classes[cls_id]
    return label.capitalize()