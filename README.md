# python-apollo-openapi
Apollo Openapi Python Client

### Usage

```python

from pyapollo_openapi.client import ApiClient

host = "http://106.54.227.205"
token = "c87301b295193e125284e3bcac896d3ace53e9ed"
appid = "app2022"
create_by = "apollo"
env = "DEV"
client = ApiClient(host, token)

# 获取环境列表、集群列表
ret = client.get_envclusters(appid)
print(ret)

# 获取APP列表
ret = client.get_apps()
print(ret)

# 获取单个集群信息
ret = client.get_cluster(appid)
print(ret)

# 创建集群
ret = client.create_cluster(appid, env, "default3", "apollo")
print(ret)

# 获取集群下所有Namespace列表
ret = client.get_namespaces(appid)
print(ret)

# 获取某个Namespace信息
ret = client.get_namespace(appid)
print(ret)

# 创建Namespace
ret = client.create_namespace(appid, "namespace_test", create_by, )
print(ret)

# 获取某个Namespace当前编辑人接口
ret = client.get_namespace_locked_by(appid)
print(ret)

# 读取指定key的配置值 (注意：这个接口读取到的是最新的值，可能是未发布的配置)
ret = client.get_item(appid, "timeout")
print(ret)

# 新增配置
ret = client.created_item(appid, "req_limit", 1000, "apollo", )
print(ret)

# 修改配置
ret = client.update_item(appid, "timeout", 120, "apollo", )
print(ret)

# 删除配置
ret = client.delete_item(appid, "keepalive", "apollo", )
print(ret)

# 发布配置
ret = client.releases(appid, "releases-2022-09-20 15:25:37", "modify log level", "apollo")
print(ret)

# 获取某个Namespace当前生效的已发布配置
ret = client.get_latest_releases(appid)
print(ret)

# 回滚到指定版本
ret = client.rollback(105842, "apollo")
print(ret)

# 分页获取配置项
ret = client.get_latest_releases_by_page(appid, 1, 20)
print(ret)

```