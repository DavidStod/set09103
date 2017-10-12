#change line above to whats commented to get different result
import unittest
import fail_test
#import pass_test

class TestingTest(unittest.TestCase):
    def test_root(self):
        self.app = fail_test.app.test_client()
        #self.app = pass_test.app.test_client()
        out = self.app.get('/')
        assert '200 OK' in out.status
        assert 'charset=utf-8' in out.content_type
        assert 'text/html' in out.content_type

if __name__ == "__main__":
    unittest.main()
