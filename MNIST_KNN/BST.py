# -*- coding: utf-8 -*-
"""
author:  LeeJiangLee
contact: ljllili23@gmail.com

19/9/2018 4:41 PM
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def search(self,node,parent,data):
        if node is None:
            return False,node,parent
        if node.data == data:
            return True, node, parent
        if node.data> data:
            return self.search(node.lchild,node,data)
        if node.data< data:
            return self.search(node.rchild,node,data)

    def insert(self,data):
        flag,node,parent = self.search(self.root,self.root,data)
        if not flag:
            newNode = Node(data)
            if data>parent.data:
                parent.rchild = newNode
            else:
                parent.lchild = newNode

