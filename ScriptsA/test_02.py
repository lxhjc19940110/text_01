class Test_Bcd:
    def setup_class(self):
        print("---->setup_class")

    def teardown_class(self):
        print("---->teardown_class")

    def test_abc_01(self):
        print("--->test_abc_01")
        assert True

    def test_abc_02(self):
        print("--->test_abc_02")
        assert True
