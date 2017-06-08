from ppboilerplate.main import Main

class TestMain:
    def setup(self):
        print('setup')

    def test_running(self):
        '''Test that pytest is setup correctly'''
        assert True

    def test_greet(self):
        main = Main()
        '''Test that pytest is setup correctly'''
        assert main.greet() == "Hello world!"
