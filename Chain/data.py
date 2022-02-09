"""
数据层
"""
from hashlib import sha256
import json
import time

class DifficultyMixin():
    """
    工作难度Mixin
    使得区块链仅接收固定范围内的哈希值
    提高difficulty的数值将会增大伪造区块链的难度，但也会相应的增加写入数据的成本。
    """
    def __init__(self) -> None:
        super().__init__(self)

        self.difficulty: int = 3

    def difficulty_validate(self, hash_string):
        """
        验证生成哈希是否为难度*0开头
        :params hash_string: str需要验证的哈希
        :return: Bool
        """
        target_head = [0] * self.difficulty
        return hash_string[:self.difficulty] == target_head

    @staticmethod
    def validate(block: 'Block'):
        if sha256(json.dumps(block.__dict__)) == block.hash_string:
            return True
        else:
            return False

class LastBlockError(Exception):
    pass

class Block(DifficultyMixin):
    """
    区块对象
    传入参数;
        property: 区块要存放的数据
        last_block_hash: 上一个区块签名
    属性：
        time: 时间
        last_hash_string: 上一个区块签名
        property: 数据
        pow: 工作证明
        hash_string: 当前区块签名

    """
    def __init__(self, property: list, last_block_hash: str) -> None:
        super().__init__(self)

        self.time = time.time()  # 创建时间

        # 处理初始区块
        if last_block_hash is None:
            self.last_hash_string = ''
        else:
            self.last_hash_string = last_block_hash
            

        self.property = property  # 数据列表
        self.hash = ''  # 区块签名
        self.pow: int  # 工作证明

        self.sign()

    def sign(self):
        """
        使用对象字典进行自签名尝试
        """
        
        #TODO: 使用Log模块
        print(self.__dict__.keys)

        #TODO:需要多进程
        while True:
            self.hash = sha256(json.dumps(self.__dict__))
            if self.difficulty_validate(self.hash):
                break
            self.pow += 1
    
        
class Data(dict):
    """
    可自定义的数据单元
    """
    def __init__(self, author, content: dict):
        super().__init__(self)
        self = {
            'author': '',
            'content': content
        }   


class BlockChain():
    #TODO: 需要进一步对多实例部署进行改造
    """
    区块链对象
    属性：
        chain: 主链
        unchained_data: 还未保存到链中的数据
    """
    def __init__(self, block_len:int = 100) -> None:
        self.block_len = chain_len
        self.chain = []
        self.unchained_data = []
        self.__genesis()
    
    def __genesis(self):
        """生成初始区块"""
        neon_genesis_block = Block(
            property=[],
            last_block=None
        )
        self.chain.append(neon_genesis_block)

    def __new_block(self):
        """将暂存的数据保存到区块并写入到链
        
        不使用挖矿的模式，而是自我写入
        
        """
        if not self.unchained_data() == []:
            new_block = Block(
                property=self.unchained_data,
                last_block_hash=self.last_block.hash
            )
            self.chain.append(new_block)
            self.unchained_data.clear()
            return True
        else:
            return False
        
    def write_data(self, data: Data):
        """暂存数据"""
        self.unchained_data.append(data)

        # 当暂存的数据数量超过设定的长度时：
        if len(self.unchained_data) >= self.block_len:
            self.__new_block()
                    
    @property
    def last_block(self) -> Block:
        return self.chain[-1]

