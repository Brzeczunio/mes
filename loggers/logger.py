import os
import glob
import logging

class Logger():
    def __init__(self, logs_save_location, screenshots_save_location):
        logging.basicConfig(level=logging.INFO)
        self.logs_save_location = logs_save_location
        self.make_dir(self.logs_save_location)
        self.screenshots_save_location = screenshots_save_location
        self.make_dir(self.screenshots_save_location)

    def make_dir(self, save_location):
        path = os.path.abspath(save_location)
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            for file in glob.glob('%s/*' % path):
                os.remove(file)

    def take_screenshot(self, driver, name):
        file_name = '%s.png' % name
        full_path = '%s/%s' % (self.screenshots_save_location, file_name)
        driver.get_screenshot_as_file(full_path)

    def save_log(self, name, exception):
        file_name = '%s.txt' % name
        full_path = '%s/%s' % (self.logs_save_location, file_name)
        file_handle = logging.FileHandler(full_path, mode='a')
        logger = logging.getLogger()
        for handle in logger.handlers[:]:
            logger.removeHandler(handle)
        logger.addHandler(file_handle)
        logger.error(exception, exc_info=True)
        raise
