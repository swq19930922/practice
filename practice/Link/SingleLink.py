
class Node(object):
    '''单链表节点'''
    def __init__(self, data):
        self.data = data
        self.next = None


class OneWayLink(object):
    '''单链表'''
    def __init__(self):
        self._head = None

    def is_empty(self):
        '''判空'''
        return self._head == None

    def lenth(self):
        '''链表长度'''
        count = 0
        # if self.is_empty():         # 链表为空时返回0
        #     return count
        # else:                       # 链表非空时遍历列表统计节点个数
        cur = self._head        # 设置当前节点为第一个节点
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def add(self, item):
        '''链表头部插入节点'''
        node = Node(item)
        if self.is_empty():         # 链表为空时直接将head指向新节点
            self._head = node
        else:
            node.next = self._head  # 将新节点指向第一个节点
            self._head = node       # 将head指向新节点

    def pop(self):
        '''删除第一个节点'''
        if self.is_empty():
            return None
        else:
            elem = self._head.data
            self._head = self._head.next
        return elem

    def insert(self, item, pos):
        '''任意位置插入'''
        node = Node(item)
        if self.is_empty() or pos == 0:             # 空链表或插到第一个位置
            self.add(item)
        elif pos > self.lenth()-1:                  # 插入位置超出范围
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        elif pos > 0 and pos <= self.lenth()-1:     # 正常插入
            count = 0
            cur = self._head
            while count < pos-1:                    # 当遍历至指定位置之前时将新节点指向当前节点的下一节点并将当前节点指向新节点
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node
        # elif pos < 0 and pos > 1-self.lenth():      # 反向插入
        #     self.insert(item, self.lenth()+1+pos)

    def remove(self, item):
        '''删除'''
        cur = self._head
        if cur is None:
            return
        elif cur.data == item:                  # 当第一个节点即为待删除对象时，将head指向当前节点的下一节点
            self._head = cur.next
        else:
            while cur.next is not None:         # 遍历直到当前节点的下一节点为待删除对象
                if cur.next.data != item:
                    cur = cur.next
                else:
                    cur.next = cur.next.next    # 找到待删除节点时将当前节点的next指向下下节点

    def travel(self):
        '''遍历链表'''
        # if self.is_empty():
        #     return None
        # else:
        lyst = []
        cur = self._head
        while cur is not None:
            lyst.append(cur.data)
            cur = cur.next
        return lyst


if __name__ == '__main__':
    link1 = OneWayLink()
    res1 = link1.travel()
    link1.add(3)
    res2 = link1.travel()
    link1.add(2)
    res3 = link1.travel()
    link1.add(5)
    res4 = link1.travel()
    link1.insert(6, 1)
    res5 = link1.travel()
    link1.remove(5)
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
