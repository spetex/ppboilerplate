'''Main module of this Example Project'''

class Main:
    '''Basic Example Class'''
    def __init__(self):
        self.message = 'Hello world!'

    def greet(self):
        '''Greetings'''
        print(self.message)
        return self.message

    def set_message(self, msg):
        '''Sets greeting message'''
        self.message = msg
