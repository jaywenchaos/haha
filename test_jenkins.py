import allure, pytest

class TestJenkins:

    # 添加严重级别
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="test01执行步骤")
    def test01(self):
        # 添加描述信息,生成txt文件,test01为txt文件名,描述写在txt文件内
        allure.attach("test01", "test01描述")
        print("test01")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="test02执行步骤")
    def test02(self):
        allure.attach("test02", "test02描述")
        print("test02")
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="test03执行步骤")
    def test03(self):
        allure.attach("test03", "test03描述")
        print("test03")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="test04执行步骤")
    def test04(self):
        allure.attach("test04", "test04描述")
        print("test04")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="test05执行步骤")
    def test05(self):
        allure.attach("test05", "test05描述")
        print("test05")
        assert True
