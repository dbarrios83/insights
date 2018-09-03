
import csv

from camera import Camera
from accident import Accident

def get_cameras(filename):
    cameras = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row)
            cameras.append(Camera(row['ID'], row['DIRECCION'], row['VELOCIDAD Max. KMH'], float(row['POINT_X']), float(row['POINT_Y'])))

    return cameras

def get_accidents(filename):
    accidents = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print(next(reader))
        print(next(reader))
        for row in reader:
            try:
                # print(row)
                accidents.append(Accident(row['OBJECTID'], float(row['latitud']), float(row['longitud'])))
            except:
                print('error reading accident...')
                print(row)

    return accidents
