# from os import times
import pytest
# from time import time
class Testrun:
    def test_run(self):
        # time.sleep(3)
        print('right!')
    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_run1(self):
        # time.sleep(3)
        print('right!')
    def test_run2(self):
        # time.sleep(3)
        print('right!')
        # assert 1==2
    
    @pytest.mark.usermanager
    def test_run3(self):
        # time.sleep(3)
        print('right!')