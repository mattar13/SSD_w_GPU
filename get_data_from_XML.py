import pickle
import json
import numpy as np
import os
from xml.etree import ElementTree

class XML_preprocessor(object):

    def __init__(self, data_path):
        self.path_prefix = data_path
        self.num_classes = 5
        self.data = dict()
        self._preprocess_XML()

    def _preprocess_XML(self):
        filenames = os.listdir(self.path_prefix)
        for filename in filenames:
            tree = ElementTree.parse(self.path_prefix + filename)
            root = tree.getroot()
            bounding_boxes = []
            one_hot_classes = []
            size_tree = root.find('size')
            width = float(size_tree.find('width').text)
            height = float(size_tree.find('height').text)
            for object_tree in root.findall('object'):
                for bounding_box in object_tree.iter('bndbox'):
                    xmin = float(bounding_box.find('xmin').text)/width
                    ymin = float(bounding_box.find('ymin').text)/height
                    xmax = float(bounding_box.find('xmax').text)/width
                    ymax = float(bounding_box.find('ymax').text)/height
                bounding_box = [xmin,ymin,xmax,ymax]
                bounding_boxes.append(bounding_box)
                class_name = object_tree.find('name').text
                one_hot_class = self._to_one_hot(class_name)
                one_hot_classes.append(one_hot_class)
            image_name = root.find('filename').text
            bounding_boxes = np.asarray(bounding_boxes)
            one_hot_classes = np.asarray(one_hot_classes)
            image_data = np.hstack((bounding_boxes, one_hot_classes))
            self.data[image_name] = image_data

    def _to_one_hot(self,name):
        one_hot_vector = [0] * self.num_classes
        if name == 'self':
            one_hot_vector[0] = 1
        elif name == 'Collectible':
            one_hot_vector[1] = 1
        elif name == 'Consumable':
            one_hot_vector[2] = 1
        elif name == 'Interactible':
            one_hot_vector[3] = 1
        elif name == 'Enemy':
            one_hot_vector[4] = 1
        else:
            print('unknown label: %s' %name)

        return one_hot_vector

if __name__ == "__main__":
    with open('config.json') as json_config_file:
        config = json.load(json_config_file)
    
    find = config['annotation_directory']
    write = config['save_label_pickle']
    print("Writing images from directory {} to pickle file at {}".format(find, write))
    data = XML_preprocessor(find).data
    pickle.dump(data,open(write,'wb'))

