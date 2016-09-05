import functions as f
from collections import OrderedDict
import unittest

class TestConversionFunctions(unittest.TestCase):
    def setUp(self):
        self.infile = 'test_file.txt'
        self.test_file_content = ['john', 'richard', '  edward','mason']
        self.htmlfile = 'test_file.html'
        self.outfile = 'test_file2.txt'
        self.paragraph = [' testing 234', 'hello?', 'john richard edward mason']
        self.replace_tuples = {'john':'JOHN', 'richard':'RICHARD', '?':'!', 'edward': '<span class=red>edward</span>'}

    def test_reads_file_properly(self):
        expected = self.test_file_content
        self.assertEqual(expected, f.read_file(self.infile))

    def test_write_file_to_html(self):
        f.write_file_to_html(self.infile, '../', self.test_file_content)
        expected = self.test_file_content
        self.assertEqual(expected, f.read_file(self.infile))

    def test_convert_file_type(self):
    	expected = 'test_file.html'
    	actual = f.convert_file_type(self.infile, 'html')
    	self.assertEqual(expected, actual)

    def test_replace_single_in_str(self):
    	expected = [' testing 234', 'hello?', 'JOHN richard edward mason']
    	actual = f.replace_in_str(self.paragraph, {'john':'JOHN'})
    	self.assertEqual(expected, actual)
    
    def test_replace_multiple_in_str(self):
    	expected = [' testing 456', 'hello?', 'JOHN richard edward mason']
    	actual = f.replace_in_str(self.paragraph, {'john':'JOHN', '234':'456'})
    	self.assertEqual(expected, actual)

    def test_replace_multiple_possible_conflicting_strings(self):
        expected = ['robert', 'richard', '  richard', 'mason']
        replace_tuples = OrderedDict((('john','richard'), ('john','robert'), ('edward','richard')))
        actual = f.replace_in_str(self.test_file_content, replace_tuples)
        self.assertEqual(expected, actual)

    def test_convert_tabs_and_newlines(self):
        expected = ['&nbsp;&nbsp;&nbsp;&nbsp;<br>']
        tab_and_line_break = '\t\n'
        self.assertEqual(expected, f.test_convert_tabs_and_newlines(tab_and_line_break))

    def test_add_html_tags_and_stylesheet(self):
        expected = ["<html>\n<head><link rel='stylesheet' href='styles.css'>\n<meta http-equiv='refresh' content='1' >\n</head>\n<body>\n<div class='container'>\n", ' testing 234', 'hello?', 'john richard edward mason', '\n</div>\n</body>\n</html>']
        actual = f.add_html_tags_and_stylesheet(self.paragraph, 'styles.css')
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

