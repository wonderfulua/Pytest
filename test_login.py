# from os import times
import pytest
# from time import time
class Testrun:
    def test_run(self):
        # time.sleep(3)
        print('right!')
    def test_run1(self):
        # time.sleep(3)
        print('right!')
    def test_run2(self):
        # time.sleep(3)
        print('right!')
        assert 1==2
    def test_run3(self):
        # time.sleep(3)
        print('right!')
    

if __name__ == '__main__':
    # pytest.main(['-vs','-n=2'])
    pytest.main(['-vs','--reruns=2'])