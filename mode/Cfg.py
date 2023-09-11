from alibabacloud_ecs20140526 import models as ECSmodels
from alibabacloud_ecs20140526.client import Client as ECSClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models
import os


class Cfg:
    """配置文件"""

    def __init__(self, ak, sk, region, binPath, codesPath=f'{os.getcwd()}/data/codes.txt'):
        self.ak = ak
        self.sk = sk
        self.region = region
        self.binPath = binPath
        self.codesPath = codesPath
        self.__client__ = self.__userInit__()

    def __userInit__(self):
        """初始化配置"""
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=self.ak,
            # 必填，您的 AccessKey Secret,
            access_key_secret=self.sk
        )
        # 值得商榷
        config.endpoint = f'ecs-{self.region}.aliyuncs.com'
        return ECSClient(config)

    def test(self):
        """验证配置"""
        if self.binPath is not None:
            if not os.path.exists(self.binPath):
                return '失败:确保下载ali-instance-cli'
        if (self.sk is not None) & (self.ak is not None):
            client = self.__client__
            runtime = util_models.RuntimeOptions()
            describe_regions_request = ECSmodels.DescribeRegionsRequest()
            res = client.describe_regions_with_options(describe_regions_request, runtime)
            if res.status_code == 200:
                return '成功;测试通过'
        return '失败；确保AK、SK均已正确配置'
