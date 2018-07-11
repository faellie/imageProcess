class BoxList:
    'list of boxes for a image'
    def __init__(self, image_path, boxes):
        self.image_path = image_path;
        self.boxList = boxes;

    'expect a list of boxes as [{\'x1\': 12.12, \'x2\': 56.52,\'y1\': 11.22,\'y2\': 55.88},..]'
    def add(self, box):
        self.boxList.extend(box)
    def clear(self):
        self.boxList = [];

