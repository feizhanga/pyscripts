from unittest import TestCase
from topy.hello import say_hello

__author__ = 'fzhang'


class TestSayHello(TestCase):

    def setUp(self):
        print "Calling setUp"
        self.obj= say_hello.SayHello()

    def tearDown(self):
        print "Calling tearDown"
        del self.obj

    def test_say(self, himsg="Friend"):
        msg=self.obj.say(himsg)
        self.assertEquals(msg, himsg)
