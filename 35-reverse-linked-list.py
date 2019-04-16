class Node :
    def __init__(self,elem,next=None):
        self.elem = elem
        self.next = next

#非递归实现：
def reverse_list(pHead):
    if not pHead or not pHead.next:
        return pHead

    newHead = None
    while pHead:
        temp = pHead.next
        pHead.next = newHead
        newHead = pHead
        pHead = temp
    return newHead

def insert_node(phead, elem):
    node = Node(elem)
    if phead == None:
        phead = node
    else:
        p = phead
        while p.next:
            p = p.next
        p.next = node
    return phead


if __name__ == '__main__':
    phead = None
    for i in range(10):
        phead = insert_node(phead, i)
    p = phead

    while p:
        print(p.elem, end=" ")
        p = p.next

    phead = reverse_list(phead)
    p = phead
    print("")
    while p:
        print(p.elem, end=" ")
        p = p.next
