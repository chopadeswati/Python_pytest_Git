class Test_credence_002:
    def test_sub_002(self):
        a = 8
        b = 4
        sub = a-b
        print("Sub of a and b is :" + str(sub))
        if sub == 4:
            assert True
        else:
            assert False