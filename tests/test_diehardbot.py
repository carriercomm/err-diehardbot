# coding=utf-8
from errbot.backends.test import FullStackTest


class TestCommands(FullStackTest):
    @classmethod
    def setUpClass(cls, extra=None):
        super(TestCommands, cls).setUpClass(__file__)

    def test_mcclane(self):
        self.assertCommand('(mcclane) would have said...', '(mcclane)')
