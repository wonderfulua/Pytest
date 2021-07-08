## Pytest

#import time

import pytest


class Testrun:
    def test_run(self):
        # time.sleep(3)
        print('right?')

    def test_run1(self):
        # time.sleep(3)
        print('right1!')

    def test_run2(self):
        # time.sleep(3)
        print('right2!')
        assert 1==2

    def test_run3(self):
        # time.sleep(3)
        print('right3!')

if __name__ == '__main__':
    # pytest.main(['-vs','./testcase','-n=3'])
    pytest.main(['-vs','./testcase','--reruns=2'])


## pytest.ini

[pytest]
addopts = -vs  #命令行参数，用空格分隔
testpaths = ./testcase  #测试用例的路径
python_files = aaa*.py  #模块名的规则
python_classes = Test*  #类名的规则
python_functions = test #方法名的规则
