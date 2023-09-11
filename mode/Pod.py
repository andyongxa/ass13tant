import pty

from alibabacloud_ecs20140526 import models as ECSmodels
from alibabacloud_tea_util import models as util_models

from mode.Utils import res2json, getTb


class Pod:
    """托管实例"""

    def __init__(self, client, cfg, code):
        self.__aliClient__ = client
        self.__appCfg__ = cfg
        self.__appcode__ = code
        # 简洁输出控制标签
        self.__pod_ls_simple_keys__ = ['InstanceId', 'OsType', 'Hostname', 'InstanceName', 'InternetIp', 'IntranetIp']

    def ls(self, mode='simple'):
        runtime = util_models.RuntimeOptions()
        req = ECSmodels.DescribeManagedInstancesRequest(region_id=self.__appCfg__.region)
        res = self.__aliClient__.describe_managed_instances_with_options(req, runtime)
        if res.status_code == 200:
            data = res2json(res)['Instances']
            if mode == 'full':
                return getTb(data, keys=data[0].keys())
            elif mode == 'simple':
                return '简洁输入(如需完整需要--mode=full):' + '\n' + getTb(data, self.__pod_ls_simple_keys__).__str__()
            else:
                return 'mode 参数错误'

    def rm(self, instance_id):
        """注销一个托管实例"""
        runtime = util_models.RuntimeOptions()
        req = ECSmodels.DeregisterManagedInstanceRequest(region_id=self.__appCfg__.region, instance_id=instance_id)
        res = self.__aliClient__.deregister_managed_instance_with_options(req, runtime)
        if res.status_code == 200:
            return '删除完成'
        else:
            return '错误'

    def exec(self, instance_id, auto=False):
        runtime = util_models.RuntimeOptions()
        req = ECSmodels.StartTerminalSessionRequest(
            region_id=self.__appCfg__.region,
            instance_id=[
                instance_id
            ])
        res = self.__aliClient__.start_terminal_session_with_options(req, runtime)
        if res.status_code == 200:
            url = res2json(res)['WebSocketUrl']
            if not auto:
                return url
            else:
                pty.spawn(['ali-instance-cli', 'ssh', '-u', f"{url}"])
