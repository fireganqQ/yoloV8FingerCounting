import os

os.system(fr'yolo task=detect mode=predict model="{os.getcwd()}\bestV1.pt" conf=0.25 source=0')