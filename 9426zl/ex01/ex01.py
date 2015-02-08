import uuid

class Application(object):

    def ID_Generate(self):
        self.id_box = []
        for i in range(0, 200):
            self.id_box.append(uuid.uuid4())

    def ID_Display(self):
        for i in range(0, 200):
            print self.id_box[i]


if __name__ == '__main__':
    t = Application()
    t.ID_Generate()
    t.ID_Display()
