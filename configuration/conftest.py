##########################################################################
#author:sunny,version:1.0, date:3/30/2019
#history: date 4/2/2019  add window_size, and timer by sunny
#         add close window function, sunny, 4/10/2019
#function: public funcitons configuration,
#note: file name fixed by conftest.py,same package with test case calls it
###########################################################################
#conftest.py
#coding= utf-8

import pytest
from selenium import webdriver

####################################################################
#fixture(scope=function,params=None,autouse=False,ids=None,name=None)
#module,class call it by pytest.mark.usefixtures(name)
#method call it as parameter input
###################################################################
@pytest.fixture()
def get_driver(request):

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    # return driver
    def fin():
        driver.quit()
    request.addfinalizer(fin)
    return driver