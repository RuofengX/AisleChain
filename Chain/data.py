"""
数据层
"""
from hashlib import sha256
import json
from typing import Deque

class DifficultyMixin():
    """
    工作难度Mixin
    """
    def __init__(self) -> None:
        super().__init__()

        self.difficulty: int = 3

    def difficulty_validate(self, hash_string):
        target_head = [0] * self.difficulty
        return hash_string[:self.difficulty] == target_head

    @staticmethod
    def validate(block: 'Block'):
        if block.sign() == block.hash_string:
            return True
        else:
            return False

class LastBlockError(Exception):
    pass

class Block(DifficultyMixin):
    """
    区块对象
    传入参数;
        property:区块要存放的数据
        last_block:上一个区块
    属性：
        property:数据
        pow:工作证明
        hash_string:当前区块签名
    """
    def __init__(self, property: dict, last_block: Block, pow:int, ChainClass) -> None:
        super().__init__()
        
        if not last_block.validate():
            raise LastBlockError

        self.property = {}  # 数据
        self.hash_string = ''  # 区块签名
        self.pow: int  # 工作证明

        self.sign()

    def sign(self):
        """
        使用对象字典进行自签名尝试
        """
        
        #TODO: 使用Log模块
        print(self.__dict__.keys)

        while True:
            self.hash_string = sha256(json.dumps(self.__dict__))
            if self.difficulty_validate(self.hash_string):
                break
            self.pow += 1
        
    
class BlockChain():
    def __init__(self) -> None:
        self.chain = []
        self.unchained_data = []
    
    
        
        

