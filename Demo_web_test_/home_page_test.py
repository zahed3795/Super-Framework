import time

from masterQA.core.string import StringBase
from masterQA.fixtures.base_case import BaseCase
from masterQA.data.settings import environment as env
from masterQA.common import encryption

# Test Information
USER_EMAIL = encryption.decrypt("$^*ENCRYPT=RkVdG1VpaWYoRCc3MksZNQ91e1tCRg==?&#$")
USER_PASSWORD = encryption.decrypt("$^*ENCRYPT=ZWIjSx5uEhVYGwUQ?&#$")


class MyTestClass(BaseCase, StringBase):

    def test_open_browser(self):
        # Write your code here. Example:
        self.Open(env.URL)
        self.Maximize_wendow()
        assert self.Get_page_title() == "FINVIZ.com - Stock Screener"
        self.Click("//a[contains(text(),'Login')]")
        self.Clear_Textbox("//input[@name='email']")
        self.Send_Text("//input[@name='email']", USER_EMAIL)
        self.Clear_Textbox("//input[@name='password']")
        self.Send_Text("//input[@name='password']", USER_PASSWORD)
        self.Submit("//input[@value='Log in']")
        time.sleep(1)
        self.tearDown()

    def test_Scroll_Into_View(self):
        # Write your code here. Example:
        self.Open(env.URL)
        self.Click("//a[contains(text(),'News')]")
        self.Scroll_Into_View("//a[contains(text(),'Do not sell my personal information')]")
        self.Scroll_Into_View("//a[contains(text(),'Screener')]")
        self.Select_by_index(1, "//select[@id='newsView']")
        self.Click("//a[contains(text(),'Crypto')]")
        self.tearDown()

    def test_save_file(self):
        self.Open(env.URL)
        url_link = self.get_unique_links()
        self.save_data_as(url_link, 'myfile.txt')

    def test_string_funtions(self):
        # Write your code here. Example:
        self.convert_to_lower_case('<----ABCD---->')  # Convert string into lower case
        self.convert_to_upper_case('<----abcd---->')  # Convert string into upper case
        self.get_line_count('\n1..a,\n2..a,\n3..a,\n4..a')  # Get line count from string
        self.split_to_lines("\nfirst \n2nd \n3rd", 2)  # Split lines from string as parameter need argument
