"""
网络层
分布式部署数据层实例，并通过共识算法同步和分发数据
"""

from Chain import data

class Nodes():
    def __init__(self):
        super().__init__(self)
        self.node_list = []
    
    def register(self, node):
        self.node_list.append()

class Node():
    def __init__(self, nodes: Nodes) -> None:
        super().__init__(self)

        self.chain = data.BlockChain()
        self.address = []

    def push(self):
        raise NotImplementedError
    
    def commit(self):
        raise NotImplementedError
    
    def pull(self):
        raise NotImplementedError
        
#TODO: 接受数据、广播、接受广播
        
