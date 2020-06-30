
# 项目说明
接口自动化项目

# 环境准备
- windows
- python3.6.0
- pytest4.5.0
- allure

# 先安装requirements.txt依赖包
> pip install -r requirements.txt

# 运行用例，生成报告在 ./report
> pytest --allure ./report/allure

# 参数配置 pytest.ini
自己标注的内容，加注释
markers = xxx: Run xxx module cases     

命令行默认带上的参数
addopts = -s --alluredir ./report/allure

