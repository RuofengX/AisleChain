"""
网络层
分布式部署数据层实例，并通过共识算法同步和分发数据
"""
import socket
from Chain import data

class Nodes():
    def __init__(self):
        super().__init__(self)
        self.node_list = []
    
    def register(self, node):
        self.node_list.append()
class BaseNode():
    def __init__(self) -> None:
        super().__init__(self)

        self.address = []

class Node(BaseNode):
    def __init__(self, nodes: Nodes) -> None:
        super().__init__(self)

        self.chain = data.BlockChain()

    def get_ip_address(self, ipv6: bool=False):
        if ipv6:
            s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
            s.connect(("2001:4860:4860:8888", 80))
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        self.address.append(ip)

    # 利用MQTT的频道实现多实例通信
    def push(self):
        raise NotImplementedError
    
    def commit(self):
        raise NotImplementedError
    
    def pull(self):
        raise NotImplementedError

class ManagerNode(BaseNode):
    def __init__(self, ip_list):
        super().__init__(self)

        self.address = ip_list

    def regist(self, node: dict)
    # TODO




class LocalNode(Node):
    def __init__(self):
        super().__init__()

        self.address.append()        
        
#TODO: 接受数据、广播、接受广播
        
