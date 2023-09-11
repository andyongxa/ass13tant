import os
import fire

from mode.Cfg import Cfg
from mode.Code import Code
from mode.Pod import Pod

AK = None
SK = None
binPath = None
codesPath = None


class App:
    def __init__(self):
        self.ak = AK
        self.sk = SK
        self.version = '0.1'
        self.region = 'cn-hangzhou'
        self.cfg = Cfg(self.ak, self.sk, self.region, binPath, codesPath)
        self.__AliHelper__ = self.cfg.__client__
        self.code = Code(self.__AliHelper__, self.cfg)
        self.pod = Pod(self.__AliHelper__, self.cfg,self.code)

    # def cmd(self, term=False):
    #     """运行命令"""
    #     pass


def run():
    global AK
    global SK
    global binPath
    global codesPath
    if ('aliyun_ak' in os.environ) & ('aliyun_sk' in os.environ):
        AK = os.environ['aliyun_ak']
        SK = os.environ['aliyun_sk']
        # 阿里云sessionManager 位置
        binPath = os.getcwd() + '/ali-instance-cli'
        # 激活码存储位置
        codesPath = os.getcwd() + '/data/codes.txt'
        fire.Fire(App)
    else:
        print('错误；参考README.md,配置AK、SK')


if __name__ == "__main__":
    run()
