import torch
from IPython.display import Image, clear_output
from roboflow import Roboflow
import yaml
from IPython.core.magic import register_line_cell_magic

print('Setup complete. Using torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))
rf = Roboflow(model_format="yolov5", notebook="roboflow-yolov5")
rf = Roboflow(api_key="bEUJWK2YVV5jd5WeqcFQ")
project = rf.workspace().project("car-plate-location")
dataset = project.version(1).download("yolov5")

with open("./yolov5/Car-plate-location-1/data.yaml", 'r') as stream:
    num_classes = str(yaml.safe_load(stream)['nc'])

