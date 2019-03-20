from Link.SingleLink import Node, OneWayLink


class TwoWayNode(Node):
    '''双链表节点'''
    def __init__(self, data):
        super(TwoWayNode, self).__init__(data)
        self.prev = None


class TwoWayLink(OneWayLink):
    '''双链表'''
    def add(self, item):
        node = TwoWayNode(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head          # 新节点next指向第一个节点
            self._head = node               # head指向新节点
            node.next.prev = node           # 第一个节点的prev指向新节点

    def pop(self):
        '''弹出第一个节点'''
        if self.is_empty():
            return None
        else:
            cur = self._head
            elem = cur.data
            self._head = cur.next
            cur.next.prev = None
        return elem

    def insert(self,item, pos):
        '''插入节点'''
        if pos not in range(self.lenth()):
            self.add(item)
        else:
            node = TwoWayNode(item)
            count = 0
            cur = self._head
            while count < pos - 1:  # 当遍历至指定位置之前时将新节点指向当前节点的下一节点并将当前节点指向新节点
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next.prev = node
            cur.next = node
            node.prev = cur

    def remove(self, item):
        cur = self._head
        if cur is None:
            return
        while cur.data != item:
            cur = cur.next
        if cur.prev is None:
            self._head = cur.next
        elif cur.next is None:
            cur.prev.next = cur.next
        else:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev


    def travel(self):
        '''遍历链表'''
        if self.is_empty():
            return None
        else:
            lyst = []
            cur = self._head
            while cur is not None:
                lyst.append(cur.data)
                cur = cur.next
            return lyst


if __name__ == '__main__':
    link1 = TwoWayLink()
    res1 = link1.travel()
    link1.add(3)
    res2 = link1.travel()
    link1.add(2)
    res3 = link1.travel()
    link1.add(5)
    res4 = link1.travel()
    link1.insert(6, 1)
    res5 = link1.travel()
    link1.remove(2)
    res6 = link1.travel()
    link1.pop()
    res7 = link1.travel()
    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print(res5)
    print(res6)
    print(res7)
    print(link1.lenth())
