import unittest
from src import App

class TestAppFails(unittest.TestCase):

    def setUp(self):
        self.app = App()
        self.config = self.app.config

    def test_log(self):
        """checks whether _log was recieved"""
        self.assertTrue(self.app._log)

    def test_level(self):
        """checks whether level parameter is defined"""
        self.assertTrue(self.app.level)

    def test_APP_NAME_existance(self):
        """checks whether APP_NAME has a True value"""
        self.assertTrue(APP_NAME)

    def test_config_file_existance(self):
        """checks whether config_file has a True value"""
        self.assertTrue(self.config.config_file)

    def test_config_paths_existance(self):
        """checks whether config_paths has a True value"""
        self.assertTrue(self.config.config_paths)
    
    def test_default_meaning(self):
        """tests default console meaning"""
        level = 'console'
        self.assertEqual(self.app.level, level, 'mismatch with default')
    
    def test_wrong_arg(self):
        """tests whether level variable is str()"""
        level = 1
        self.assertRaises(ValueError, self.app, level)

    def test_too_many_args(self):
        """tests number of incoming parameters"""
        self.assertRaises(TypeError, self.app, ('console_1', 'console_2'))

    def test_logger_level(self):
        with self.assertLogs(self.app._log, level='console') as cm:
            logging.getLogger(self.app._log).info('first message')
            logging.getLogger('logger_2').error('second message')
        self.assertEqual(cm.output, ['INFO:{}:first message'.format(self.app._log),
                                     'ERROR:logger_2:second message'])

if __name__ == '__main__':
    unittest.main()
    
