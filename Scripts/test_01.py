import allure

def test_a():
    print("---->test_a")
    assert 2>1
@allure.step(title="我是test测试步骤名称")
def test_b():
    print("---->test_b")
    assert  False

# if __name__ == '__main__':
#     pytest.main(["test_01.py"])
