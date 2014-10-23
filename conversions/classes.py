class Dimension(object):
    def __init__(self, dimdict, base):
        self.dimdict = dimdict
        self.base = base

    def get_base(self):
        print(self.base)
        return self.base

    def chk_dict(self, key):
        if key in self.dimdict:
            print('True')
            return True
        else:
            print('False')
            return False
