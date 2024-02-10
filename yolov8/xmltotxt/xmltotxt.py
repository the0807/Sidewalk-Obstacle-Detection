from logging import raiseExceptions
import os
import xml.etree.ElementTree as ET

## PASCAL VOC
PASCAL_Class_index = {
    "bicycle": 0,
    "bus": 1,
    "car": 2,
    "carrier": 3,
    "cat": 4,
    "dog": 5,
    "motorcycle": 6,
    "movable_signage": 7,
    "person": 8,
    "scooter": 9,
    "stroller": 10,
    "truck": 11,
    "wheelchair": 12,
    "barricade": 13,
    "bench": 14,
    "bollard": 15,
    "chair": 16,
    "fire_hydrant": 17,
    "kiosk": 18,
    "parking_meter": 19,
    "pole": 20,
    "potted_plant": 21,
    "power_controller": 22,
    "stop": 23,
    "table": 24,
    "traffic_light": 25,
    "traffic_light_controller": 26,
    "traffic_sign": 27,
    "tree_trunk": 28
}

# move xml data to path
XML_DIRECTORY = "./bbox/xml/"
TXT_DIRECTORY = "./bbox/labels/"


def Write_TXT(file_name, width, height, result):
    file_name = file_name[:-3]+"txt"
    file_path = os.path.join(TXT_DIRECTORY, file_name)
    f = open(file_path, 'w')
    for i, data in enumerate(result):
        data = f"{data}\n"
        data = data.replace(",","").replace("[","").replace("]","")
        f.write(data)
    f.close()


def Read_XML(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    width = float(1920)
    height = float(1080)

    for image in root.findall('image'):
        result = list()
        image_attributes = image.attrib
        file_name = image_attributes['name']
        for box in image.findall('box'):
            box_attributes = box.attrib
            label = box_attributes['label']
            class_index = PASCAL_Class_index[label]

            xmin = float(box_attributes['xtl'])
            ymin = float(box_attributes['ytl'])
            xmax = float(box_attributes['xbr'])
            ymax = float(box_attributes['ybr'])

            bnd_width = round((xmax-xmin)/width,6)
            bnd_height = round((ymax-ymin)/height,6)
            x_center = round((xmax+xmin)/2/width,6)
            y_center = round((ymax+ymin)/2/height,6)
            result.append([class_index, x_center, y_center, bnd_width, bnd_height])
        Write_TXT(file_name=file_name, width=width, height=height, result=result)


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def main():
    if not os.path.isdir(XML_DIRECTORY):
        raise Exception("no XML DIr")
    createFolder(TXT_DIRECTORY)
    for (root, directories, files) in os.walk(XML_DIRECTORY):
        for file in files:
            if '.xml' in file:
                file_path = os.path.join(root, file)
                Read_XML(file_path)


if __name__=="__main__":
    main()