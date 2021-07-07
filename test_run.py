# import time

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
    pytest.main(['-vs','./testcase','--reruns=2'])# import time

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