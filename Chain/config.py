import toml
import os

CONFIG_PATH = './config.toml'

class Config():
    config_dict = {
        'DIFFICULTY_LEVEL': 3,
        'BLOCK_LEN': 500,
    }
    def __init__(self):
        super().__init__(self)
        self.load()
        self.broadcast()

    def load(self):
        try:
            os.path.exists('./config.toml')
        except Exception:  # TODO: 添加逻辑：如果没有config.toml文件，则把默认设置写入
            with open(CONFIG_PATH) as f:
                toml.dump(config_dict, f)
        prime_dict = toml.load(CONFIG_PATH)

        for key, value in config_dict:
            config_dict[key] = prime_dict[key]
    
    def broadcast(self):
        for key, value in self.config_dict:
            globals()[key] = value

    def __getitem__(self, __key):
        return self.config_dict[__key]

config = Config()
