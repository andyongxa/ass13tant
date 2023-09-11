# README 
## 准备
创建一个阿里云AK/SK，工具目前需要以下权限，可以通过aliyun RAM访问控制/权限策略/创建权限策略
https://ram.console.aliyun.com/policies/new
```json
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:DescribeActivations",
        "ecs:DescribeManagedInstances",
        "ecs:RunCommand",
        "ecs:ModifyCommand",
        "ecs:InvokeCommand",
        "ecs:DeleteCommand",
        "ecs:CreateCommand",
        "ecs:DescribeCommands",
        "ecs:DescribeInvocationResults",
        "ecs:DeleteActivation",
        "ecs:DeregisterManagedInstance",
        "ecs:CreateActivation",
        "ecs:DisableActivation"
      ],
      "Resource": "*"
    }
  ]
}
```
工具从环境变量中读取`aliyun_ak`和 `aliyun_sk`

需要下载阿里云提供的 `ali-instance-cli`，参考这个链接
https://help.aliyun.com/zh/ecs/user-guide/connect-to-an-instance-over-ssh-by-using-ali-instance-cli
默认与此项目同一路径

## 使用
```
git clone  https://github.com/andyongxa/ass13ant
pip install -r  requirement.txt
export aliyun_ak=[你的AK] aliyun_sk=[你的SK]
python3 main.py code new
# 通过code 注册你的机器
python3 main.py pod ls
python3 main.py pod exec [instance_id] --auto
```


