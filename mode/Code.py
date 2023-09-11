from alibabacloud_ecs20140526 import models as ECSmodels
from alibabacloud_tea_util import models as util_models

from mode.Utils import res2json, getTb, saveRecord, getRecord


class Code():
    """激活码"""

    def __init__(self, client, cfg):
        self.__aliClient__ = client
        self.__appCfg__ = cfg
        self.__code_ls_simple_keys__ = ['ActivationId', 'code', 'CreationTime', 'TimeToLiveInHours', 'Disabled',
                                        'RegisteredCount']

    def ls(self, mode='simple'):
        """列出激活码"""
        runtime = util_models.RuntimeOptions()
        req = ECSmodels.DescribeActivationsRequest(region_id=self.__appCfg__.region, page_size=50, page_number=1)
        res = self.__aliClient__.describe_activations_with_options(req, runtime)
        if res.status_code == 200:
            data = res2json(res)['ActivationList']
            codes = getRecord(self.__appCfg__.codesPath)
            for i in list(data):
                if i['ActivationId'] in codes:
                    i['code'] = codes[i['ActivationId']]
                else:
                    i['code'] = ''
            tb_key = data[0].keys()
            if mode == 'full':
                return getTb(data, keys=tb_key)
            elif mode == 'simple':
                return '简洁输入(如需完整需要--mode=full):' + '\n' + getTb(data, self.__code_ls_simple_keys__).__str__()
            else:
                return 'mode 参数错误'

    def rm(self, code):
        """删除指定的'未使用'激活码"""
        runtime = util_models.RuntimeOptions()
        req = ECSmodels.DeleteActivationRequest(region_id=self.__appCfg__.region, activation_id=code)
        res = self.__aliClient__.delete_activation_with_options(req, runtime)
        if res.status_code == 200:
            data = res2json(res)['Activation']['ActivationId']
            return f"删除激活码: {data} 成功"

    def off(self, activation_id):
        """禁用激活码"""
        runtime = util_models.RuntimeOptions()
        req = ECSmodels.DisableActivationRequest(region_id=self.__appCfg__.region, activation_id=activation_id)
        res = self.__aliClient__.disable_activation_with_options(req, runtime)
        if res.status_code == 200:
            return f"禁用激活码: {activation_id} 成功"

    def new(self, name='', limit=100, timeout=876576, term=False):
        """新建激活码"""
        if term:
            instance_name = input("默认的实例名称前缀: ")
            description = input("激活码对应的描述: ")
            instance_count = int(input("激活码用于注册托管实例的使用次数上限,如 1-1000: "))
            time_to_live_in_hours = int(input("激活码的有效使用时间,如 4-876576: "))
            ip_address_range = input('允许使用该激活码的主机IP,如 0.0.0.0/0: ')

        else:
            instance_name = name
            description = 'ass13tant'
            instance_count = limit
            time_to_live_in_hours = timeout
            ip_address_range = "0.0.0.0/0"

        runtime = util_models.RuntimeOptions()
        req = ECSmodels.CreateActivationRequest(
            region_id=self.__appCfg__.region,
            instance_name=instance_name,
            description=description,
            instance_count=instance_count,
            time_to_live_in_hours=time_to_live_in_hours,
            ip_address_range=ip_address_range
        )
        res = self.__aliClient__.create_activation_with_options(req, runtime)
        if res.status_code == 200:
            act_id = res2json(res)['ActivationId']
            code = res2json(res)['ActivationCode']
            saveRecord(self.__appCfg__.codesPath, f"{act_id},{code}")
            return f"新建激活码 {act_id} 对应 {code}\n,命令如下:"
