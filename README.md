```angular2html

1、在PyPi官网注册账号
2、创建pypi文件夹作为根目录，创建toolsbyerazhan文件夹作为创建项目的名称(最后就是pip install toolsbyerazhan)
3、在toolsbyerazhan文件夹中创建__init__.py(可以为空)表示这是一个package，并创建其它自定义文件，例如timetools.py
4、在根目录下编写setup.py文件(参考网址或者自己之前做的)
5、然后执行python setup.py sdist
6、重新手动(不要复制，如果时更新项目则不用再考虑)创建.pypirc文件(查看可用~/.pypirc，参考网址或者自己之前做的)
7、最后执行python setup.py sdist upload 更新为 twine upload dist/erazhan_utils-0.0.1.tar.gz(通过pip install twine安装twine)

注意:在win10上操作时，要用管理员启动cmd，然后进入到根目录文件夹下

.pypirc文件内容
"""
[distutils]
index-servers = pypi

[pypi]
username:自己的pypi用户名
password:自己的pypi密码
"""

官网项目地址
https://pypi.python.org/simple/erazhan-utils
阿里云项目地址(阿里云镜像一般要隔一天才会更新)
http://mirrors.aliyun.com/pypi/simple/erazhan-utils/

使用和更新
pip install erazhan_utils
pip install --upgrade erazhan_utils
pip install --U erazhan_utils

用官网镜像(http -> https)
pip install --U erazhan_utils -i https://pypi.python.org/simple

只加上 -i https://pypi.python.org/simple ## 不需要后面的 --trusted-host pypi.python.org
http://e.pypi.python.org/simple?

用国内镜像
-i http://pypi.douban.com/simple --trusted-host pypi.douban.com

阿里云镜像？
http://mirrors.aliyun.com/pypi/simple/

官网:
https://pypi.org/
参考网址:
https://blog.csdn.net/fengmm521/article/details/79144407
https://www.cnblogs.com/Barrybl/p/12090534.html
https://www.cnblogs.com/smileyes/p/7657591.html
```

### __version__ = 0.0.6改动(2022-06-08)

#### time_utils.py
- 更改`backto_Ndays`，增加参数`data_format(默认='%Y-%m-%d')`
- 增加`backto_Ntoday`，可自定义`data_format(默认='%Y%m%d')`
- 增加`trans_timestamp2str`，时间戳转字符串

####  json_utils.py
- 更改`save_json_file`，增加参数`mode(默认='indent')`，保存时是否展开
   
#### logging_utils.py
- 更改`update_logger`，将参数名`app_version`改为`app_version_name`，增加参数`update_type(默认='day')`

### __version__ = 0.0.7改动(2022-07-20)

#### __init__.py
- 增加`backto_Ntoday`可直接导入，`from erazhan_utils import backto_Ntoday`
- `special_utils.py`中文件均直接导入
- `conn_pg.MysqlConnection`不放到`__init__.py`中，即导入改为`from erazhan_utils.conn_pg import MysqlConnection`

#### conn_pg.py
- 增加数据库读取，除去了文件中的账号密码，包含初始化变量`charset='utf8'`

#### special_utils.py

- 增加`trans_singleQM2doubleQM`，将文本中的单引号替换成双引号
- 增加`sort_dict`，对字典数据进行排序，`sort_index=0，1`分别按key，value进行排序
- 增加`judge_not`，判断否定的疾病/症状，例如"没有便秘"识别到"便秘"，但并没有发生

### __version__ = 0.0.8改动(2023-04-18)
#### logging_utils.py
- 开头增加一行`# coding:utf-8`
- FileLogger类中部分函数增加参数`encoding='utf-8'`

### __version__ = 0.0.9改动(2023-09-20)

#### __init__.py
- 更改版本号
- 注释`sklearn_utils.py`的导入，使用其它文件中的函数时可以忽略`scikit-learn`
- 增加新增文件`judge_utils.py`和`constant.py`相关函数和常量的导入

#### judge_utils.py
- 文件新增加
- 增加函数`judge_suffix`，用于判断文本是否是某种文件类型
- 增加函数`split_name_and_suffix`，分离出文件名中的名称和后缀
- 增加函数`judge_suffix_type`，判断文件名的类型
- 将`judge_not`从`special_utils.py`中移过来，并且重写命令为`judge_negative_entity`，`judge_not`接口保持一致，用于兼容老版本

#### constant.py
- 文件新增加
- 增加常量`SUFFIX_TYPE_DICT`，`EN_PUNCTUATION`，`CN_PUNCTUATION`，`ALL_PUNCTUATION`

#### logging_utils.py
- `writer_logger`增加`debug`类型

### __version__ = 0.0.10改动(2023-09-20)
- 修复上一版本`BUG`，`0.0.9`版本不更新到`github`
- `json_utils.py`开头去除`x`
- `judge_utils.py`中导入`from constants import SUFFIX_TYPE_DICT`改为`from .constants import SUFFIX_TYPE_DICT`


### 备注
- 上传时创建新`branch`和`tag`，不考虑`master`分支