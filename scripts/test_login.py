import allure
import pytest
class TestLogin:

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login1(self):
        @allure.step(title='输入密码')
        assert 1

    def test_login2(self):
        @allure.step(title='输入用户名')
        assert 1

    def test_login3(self):
        @allure.step(title='点击登录')
        assert 1
