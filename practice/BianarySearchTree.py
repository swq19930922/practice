
class BSNode(object):
    '''二分搜索树节点'''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    '''二分搜索树'''
    def __init__(self):
        self.root = None

    def is_empty(self):
        '''判空'''
        if self.root is None:
            return True
        else:
            return False

    def depth(self):
        '''树高'''
        pass

    def add(self, data):
        # if self.is_empty():
        #     self.root = BSNode(data)
        # else:
        #     cur = self.root
        pass

