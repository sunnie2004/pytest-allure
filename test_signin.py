##############################################################
#author:sunny,version:1.0, date:4/4/2019
#history:html report, sunny,4/5/2019
#        allure+pytest,sunny,4/8/2019(tired pytest-allure-adaptor,not working)
#        allure+pytest,sunny,4/9/2019(tired new version allure, install Jdk1.8,configure the environment variables)
#function: login in process
##############################################################
#test_signin.py
#coding= utf-8

import pytest
from configuration.conftest import *
from page.signinpage import *
import allure

####################################################################
#fixture(scope=function,params=None,autouse=False,ids=None,name=None)
#module,class call it by pytest.mark.usefixtures(name)
#method call it as parameter input
###################################################################
@allure.feature("sign in model")
class Testlogin(object):
    @allure.story("2 accounts: 1right +1 wrong")
    @pytest.mark.parametrize('emailaddress,password', [("sunnie2004@gmail.com", "1357810Hxq!#"),
                                                       ("sunnie2004@gmail.com", "1357810Hxq!")])
    def test_login(self,get_driver,emailaddress,password):
        with allure.step("firefox open:"):
            login_page = LoginPage(get_driver)

        with allure.step("input email and password:"):
            login_page.login(emailaddress,password)

        assert "Signed in as" in login_page.get_source()

if __name__ =="__main__":
    pytest.main()