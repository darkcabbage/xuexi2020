
# 项目说明
接口自动化项目

# 环境准备
- windows
- python==3.6.0

# 先安装requirements.txt依赖包
> pip install -r requirements.txt

# 运行所有用例
> pytest

# 参数配置 pytest.ini
自己标注的内容，加注释
markers = info: Run info module cases

#命令行默认带上的参数
addopts = -s
          -m info
          --alluredir ./report/allure
          