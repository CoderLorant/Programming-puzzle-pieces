import sys
import unittest

sys.path.append('..')

from modules import htmlAttributes as attr

class HtmlAttributesTests(unittest.TestCase):

  def test_getAttributeNameIdx_nonSense(self):
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx("htmlAttribute", 12)
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx("htmlAttribute", None)
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx(None, None)
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx(12, False)
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx(None, "class")
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx(False, "id")

  def test_getAttributeNameIdx_emptyString(self):
    corrupt, idx = attr.getAttributeNameIdx("", "class")
    self.assertFalse(corrupt)
    self.assertEqual(idx, -1)
    corrupt, idx = attr.getAttributeNameIdx("id=\"content\" class=\"clearfix\"", "")
    self.assertFalse(corrupt)
    self.assertEqual(idx, -1)

  def helper_getAttributeNameIdx_checkIfCorrupt(self, htmlAttributes, key):
    corrupt, idx = attr.getAttributeNameIdx(htmlAttributes, key)
    self.assertTrue(corrupt)
    self.assertEqual(idx, -1)

  def test_getAttributeNameIdx_corrupt_keyContainsHtmlDelimiter(self):
    self.helper_getAttributeNameIdx_checkIfCorrupt("selected default", " ")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='cl1 cl2'", "cl1 cl2")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='cl1 cl2'", " cl2")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='cl1 cl2'", "class=")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='myClass'", "'myClass'")

  def test_getAttributeNameIdx_corrupt(self):
    self.helper_getAttributeNameIdx_checkIfCorrupt("value='234'' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value=''234' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value='''234' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value=''''234' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value=''''234' selected'", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value='234''' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value='234'''' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("style''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt(" 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("\t\r\n'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt(" ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("\t\t='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("\" ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'class' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class ='style myClass", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class ='style myClass'\"", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("''' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'''' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("''''' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'''''' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("\"\" ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title =\t= 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = ''style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = 'style''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = ''style''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = style''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = style'''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = style''''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = '''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = ''''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = '''''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = ''''''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = ''''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = 'style' =", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = 'style' '", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = 'style'''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = 'style' \"something", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'title' = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title' = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title'' = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title''' = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title\" = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("\"title\" = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title\"\" = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title\"\"\" = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title='\"style'\"", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title=\"'style\"'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title=\"'hello' my 'style\"'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title=\"'hello' my 'style\"'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title=\"'hello\" my 'style\"'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class=style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class=style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class=custom style red", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='custom style red", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='custom style red\"", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='style red", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='custom style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'class my-class' class='myClass'", "class")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class'myClass' class='myClass'", "class")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'class title=\"heyo\"", "class")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class' title=\"heyo\"", "class")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'class' title=\"heyo\"", "class")

  def test_getAttributeNameIdx_attrNotFound(self):
    idx = attr.getAttributeNameIdx("ax xa", "a")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("aa", "a")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("aaa", "a")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("xacca", "a")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("title=\"'style\"selected", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("title=\"'style\" selected", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("title=\"'style\"", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("title=\"''style\"", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("title=\"''style'\"", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("title=\"''style''\"", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("title=\"'''''style\"", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx('title="My \'fancy\' style"', "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx('title="My style is \'not fancy\'"', "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx('title="My \'fancy\' style is \'not fancy\'"', "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx('title="My \'style\' is hardcore" id="red"', "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx('class="style"id="red"', "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx('class="style"id="style"', "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("class='custom style red'", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("id=\"myId\" class='custom style red'", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("class='custom-style'", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("class='custom-style-red'", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("class='style-custom'", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("class='style'", "style")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("htmlAttribute", "class")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("htmlAttribute no-href", "href")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("htmlAttribute hrefx", "href")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("htmlAttribute hrefhref", "href")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("no-href class='idk'", "href")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("hrefx class='idk'", "href")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("hrefhref class='idk'", "href")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("selected no-href class='idk'", "href")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("selected hrefx class='idk'", "href")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("selected hrefhref class='idk'", "href")
    self.assertEqual(idx, (False, -1))

  def test_getAttributeNameIdx_attrNotFound_equalWithinAttributeValue(self):
    idx = attr.getAttributeNameIdx("title=\"class='myClass'\"", "class")
    self.assertEqual(idx, (False, -1))
    idx = attr.getAttributeNameIdx("title=\"class='class='myClass''\"", "class")
    self.assertEqual(idx, (False, -1))

  def test_getAttributeNameIdx_attrFound(self):
    corrupt, idx = attr.getAttributeNameIdx("a", "a")
    self.assertFalse(corrupt)
    self.assertEqual(idx, 0)
    corrupt, idx = attr.getAttributeNameIdx("selected", "selected")
    self.assertFalse(corrupt)
    self.assertEqual(idx, 0)
    corrupt, idx = attr.getAttributeNameIdx("default='1'", "default")
    self.assertFalse(corrupt)
    self.assertEqual(idx, 0)
    corrupt, idx = attr.getAttributeNameIdx("default=\"1\"", "default")
    self.assertFalse(corrupt)
    self.assertEqual(idx, 0)
    corrupt, idx = attr.getAttributeNameIdx("default=\"1\"selected", "default")
    self.assertFalse(corrupt)
    self.assertEqual(idx, 0)
    string = "value='234' selected"
    corrupt, idx = attr.getAttributeNameIdx(string, "selected")
    self.assertFalse(corrupt)
    self.assertEqual(idx, string.find("selected"))
    corrupt, idx = attr.getAttributeNameIdx("selected class=\"className\"", "selected")
    self.assertFalse(corrupt)
    self.assertEqual(idx, 0)
    corrupt, idx = attr.getAttributeNameIdx("selected greyed-out", "selected")
    self.assertFalse(corrupt)
    self.assertEqual(idx, 0)
    string = "value='234' selected=\"false\""
    corrupt, idx = attr.getAttributeNameIdx(string, "selected")
    self.assertFalse(corrupt)
    self.assertEqual(idx, string.find("selected"))
    corrupt, idx = attr.getAttributeNameIdx("selected=\"false\" class=\"className\"", "selected")
    self.assertFalse(corrupt)
    self.assertEqual(idx, 0)
    corrupt, idx = attr.getAttributeNameIdx("selected=\"false\" greyed-out", "selected")
    self.assertFalse(corrupt)
    self.assertEqual(idx, 0)
    string = "htmlAttribute no-href href"
    corrupt, idx = attr.getAttributeNameIdx(string, "href")
    self.assertFalse(corrupt)
    self.assertEqual(idx, string.find(" href") + 1)
    string = "htmlAttribute hrefx href=\"value\""
    corrupt, idx = attr.getAttributeNameIdx(string, "href")
    self.assertFalse(corrupt)
    self.assertEqual(idx, string.find("href="))
    string = "htmlAttribute hrefhref='value2' href='value3'"
    corrupt, idx = attr.getAttributeNameIdx(string, "href")
    self.assertFalse(corrupt)
    self.assertEqual(idx, string.find("href='value3'"))
    string = "no-href=\"noValue\" href class='idk'"
    corrupt, idx = attr.getAttributeNameIdx(string, "href")
    self.assertFalse(corrupt)
    self.assertEqual(idx, string.find("href class"))
    string = "hrefx href class='idk'"
    corrupt, idx = attr.getAttributeNameIdx(string, "href")
    self.assertFalse(corrupt)
    self.assertEqual(idx, string.find("href class"))

  def test_getAttributeNameIdx_attrFoundMultipleTime(self):
    idx = attr.getAttributeNameIdx("selected selected='false' selected selected", "selected")
    self.assertEqual(idx, (False, 0))
    idx = attr.getAttributeNameIdx("default='1' class=\"myClass\" default", "default")
    self.assertEqual(idx, (False, 0))
    string = "htmlAttribute hrefhref='value2' href='value3' href href='val4'"
    idx = attr.getAttributeNameIdx(string, "href")
    self.assertEqual(idx, (False, string.find("href='value3'")))

  def test_getAttributeNameIdx_attrFound_equalWithinAttributeValue(self):
    idx = attr.getAttributeNameIdx("title=\"class='myClass'\"class='myClass'", "class")
    self.assertEqual(idx, (False, 23))
    idx = attr.getAttributeNameIdx("title=\"class='myClass'\" class='myClass'", "class")
    self.assertEqual(idx, (False, 24))

  def test_extractDifferentValuesFromHtmlAttributesByKey_nonSense(self):
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", "")
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", 123)
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", False)
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", None)
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", ["option"])
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(None, "option")
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(234, "src")
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(123, None)

  def test_extractDifferentValuesFromHtmlAttributesByKey_emptyAttributes(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("", "title")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("", "src")
    self.assertEqual(attributes, (False, None))

  def test_extractDifferentValuesFromHtmlAttributesByKey_attrNotFound(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("htmlAttribute no-href", "href")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                                             "href=\"img/favicon.ico\" type=\"image/x-icon\"", "title")
    self.assertEqual(attributes, (False, None))
    # TODO error - if attributeValue, it is not corrupt
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\""
                                                       "masthead_custom_styles\" is=\"custom-style\" id=\"ext-styles\" "
                                                       "nonce=\"tG2l8WDVY7XYzWdAOVtRzA\"", "style")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                                              "src=\"jsbin/spf.vflset/spf.js\"", "alt")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"anim\"", "id")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"animated bold\"", "id")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"animated bold\" "
                                                                                "selected class=\"active-tab\"", "id")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "upgrade")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "masthead")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "dark")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "shell")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "chunked")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "e")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "disable")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "clas")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "lot")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("_value=\"audi\"", "value")
    self.assertEqual(attributes, (False, None))

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_attrIsNotKeyValue(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi\" selected",
                                                                                         "selected")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi\" selected "
                                                                                       "class=\"myClass\"", "selected")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("selected value=\"audi\"",
                                                                                         "selected")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("selected", "selected")
    self.assertEqual(attributes, (False, None))

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_emptyValue(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"\"", "value")
    self.assertEqual(attributes, (False, []))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"  \"", "value")
    self.assertEqual(attributes, (False, []))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"\t\"", "value")
    self.assertEqual(attributes, (False, []))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\" \r\n \t \"", "value")
    self.assertEqual(attributes, (False, []))

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_corrupt(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class='custom style red",
                                                                                       "style")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"   ", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value= ", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value= \n \t ", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi'", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='audi\"", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value \"audi\"", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value\"audi\"", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value 'audi'", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value'audi'", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("\"class'myclass' "
                                                                                       "class='myclass'", "class")
    self.assertEqual(attributes, (True, None))


  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_quotes(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi\"", "value")
    self.assertEqual(attributes, (False, ["audi"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='audi'", "value")
    self.assertEqual(attributes, (False, ["audi"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi'A3\"", "value")
    self.assertEqual(attributes, (False, ["audi'A3"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi'A3'\"", "value")
    self.assertEqual(attributes, (False, ["audi'A3'"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='audi\"A3'", "value")
    self.assertEqual(attributes, (False, ["audi\"A3"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='\"audi\"A3\"'", "value")
    self.assertEqual(attributes, (False, ["\"audi\"A3\""]))

  def test_extractDifferentValuesFromHtmlAttributesByKey_oneValueFound(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                                             "href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, (False, ["img/favicon.ico"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                                   "href=\"img/favicon.ico\" id='X' type=\"image/x-icon\"", "id")
    self.assertEqual(attributes, (False, ["X"]))
    # I have found these tricky examples while implementing beforeWhitespaceDelimitedFind as an effort to minimize
    # code length
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                            "xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, (False, ["img/favicon.ico"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                          "no-href=\"false\" xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, (False, ["img/favicon.ico"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
        "hrefhref=\"image\" no-href=\"false\" xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, (False, ["img/favicon.ico"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                                            "nonce=\"lix9PsSUHJxW7ghXrU5s0A\"", "nonce")
    self.assertEqual(attributes, (False, ["lix9PsSUHJxW7ghXrU5s0A"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "disable-upgrade")
    self.assertEqual(attributes, (False, ["true"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"preload\" href="
                                "\"https://r3---sn-8vq54voxgv-vu26.googlevideo.com/generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))

  def test_extractDifferentValuesFromHtmlAttributesByKey_whitespaces(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                         "rel =\"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                          "rel = \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                          "rel= \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                    "rel \n\r\t\t\t = \n\r\t\t\t \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                "\n\trel \n\r\t\t\t = \n\r\t\t\t \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
          "\n\trel \n\r\t\t\t = \n\r\t\t\t \"\r\n\t\t preload \t\t\t\n\t  \" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))

  def test_extractDifferentValuesFromHtmlAttributesByKey_multipleValuesFound(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                "method=\"get\" class=\"add_search_params pure-form\" style=\"display:inline-block\"",
                                "class")
    self.assertEqual(attributes, (False, ["add_search_params", "pure-form"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                "method=\"get\" class=\"add_search_params pure-form hide-xs hide-sm hide-md\" "
                                "style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, (False, ["add_search_params", "pure-form", "hide-xs", "hide-sm", "hide-md"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                "method=\"get\" class\n=\n\"add_search_params\tpure-form\r\nhide-xs     hide-sm"
                                "\t\t\t\n\r   \n\r    hide-md\n\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, (False, ["add_search_params", "pure-form", "hide-xs", "hide-sm", "hide-md"]))

  def test_extractDifferentValuesFromHtmlAttributesByKey_multipleDeclarations(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
              "method=\"get\" class=\"add_search_params cl2 cl3\" class=\"pure-form\" style=\"display:inline-block\"",
              "class")
    self.assertEqual(attributes, (False, ["add_search_params", "cl2", "cl3"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
              "method=\"get\" class=\"add_search_params\" class=\"pure-form cl2 cl3\" style=\"display:inline-block\"",
              "class")
    self.assertEqual(attributes, (False, ["add_search_params"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" class "
                              "method=\"get\" class=\"pure-form cl2 cl3\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, (False, None))

  def test_extractDifferentValuesFromHtmlAttributesByKey_valueRepeats(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                            "method=\"get\" class=\"cl1 cl1\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, (False, ["cl1"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                            "method=\"get\" class=\"cl1 cl1 cl2 cl1 cl3 cl2\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, (False, ["cl1", "cl2", "cl3"]))

  def test_getNextHtmlAttribute_nonSense(self):
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("class = 'myClass'", None)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("class = 'myClass'", False)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("class = 'myClass'", "12")
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("class = 'myClass'", -1)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("class = 'myClass'", 488)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("", 0)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute(123, 0)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute(True, 0)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute(None, 0)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute(True, False)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute(None, None)

  def helper_getNextHtmlAttribute_testCorrupt(self, corrupt, attributeName, attributeValue, startIdx, endIdx):
    self.assertTrue(corrupt)
    self.assertEqual(attributeName, None)
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, -1)
    self.assertEqual(endIdx, -1)

  def helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt(self, htmlAttributes):
    *returnValues, = attr.getNextHtmlAttribute(htmlAttributes, 0)
    self.helper_getNextHtmlAttribute_testCorrupt(*returnValues)

  def helper_getNextHtmlAttribute_testAttributeNotFound(self, corrupt, attributeName, attributeValue, startIdx, endIdx):
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, None)
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, -1)
    self.assertEqual(endIdx, -1)

  def helper_getNextHtmlAttribute_checkAttributeNotFound(self, htmlAttributes, startIdx):
    *returnValues, = attr.getNextHtmlAttribute(htmlAttributes, startIdx)
    self.helper_getNextHtmlAttribute_testAttributeNotFound(*returnValues)

  def test_getNextHtmlAttribute_attributeNotFound(self):
    self.helper_getNextHtmlAttribute_checkAttributeNotFound(" ", 0)
    self.helper_getNextHtmlAttribute_checkAttributeNotFound("\t\t", 0)
    self.helper_getNextHtmlAttribute_checkAttributeNotFound("id='content' ", 12)
    self.helper_getNextHtmlAttribute_checkAttributeNotFound("\n  \t\t\t    \r\n", 0)
    self.helper_getNextHtmlAttribute_checkAttributeNotFound("selected id='x'\n  \t\t\t    \r\n", 16)
    self.helper_getNextHtmlAttribute_checkAttributeNotFound("selected id='x'\n  \t\t\t    \r\n", 18)

  def test_getNextHtmlAttribute_corrupt(self):
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("=")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("'\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("\"'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("\"\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("''")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("\"value\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("'value'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("\"\"\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("'''")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("=value")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("='value'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("= 'value'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("\t= 'value'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class= ='myClass'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class=='myClass'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class==='myClass'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class == 'myClass'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class =  = 'myClass'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class=")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class=\t")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class =")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class\t=")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class \t \t =")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class\t=\t")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("class \t\t\t = \t\t \n")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value=\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value=\"   ")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value=\t \"   ")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value=\t   class='bordered'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value=\t \"   class='bordered'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value=\"audi")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value=\"audi\r\n")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value=\"audi\r\n selected")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value=\"audi'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value=\"audi' class='black-bg'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value=\"audi' selected")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value='audi\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value='audi\" selected")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value='audi\" id=\"my-id\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value \"audi\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value  \"audi\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value \t\t\t \"audi\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value\"audi\"")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value 'audi'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value\t\t'audi'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value\t\t'audi' selected")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value 'audi'\n")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value 'audi'\n selected")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value'audi'")
    self.helper_getNextHtmlAttribute_checkHtmlAttributesIsCorrupt("value'audi' selected")

  def test_getNextHtmlAttribute_noAttributeValue(self):
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("x", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "x")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 0)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected class=\"my-class\" "
                                                                                "no-href id='my-id'", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected  \t \n  class=\"my-class\" "
                                                                                "no-href id='my-id'", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected\t\n\t", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected\t animated\nid=\"my-id\"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(" selected", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, 8)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(" selected minimized", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, 8)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(" \t  \r\n  selected", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 8)
    self.assertEqual(endIdx, 15)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(" \t  \r\n  selected class='abc'", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 8)
    self.assertEqual(endIdx, 15)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(" selected ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, 8)
    string = " \t  \r\n  selected\t\t\t\r\n"
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(string, 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 8)
    self.assertEqual(endIdx, string.find("d\t\t"))

  def test_getNextHtmlAttribute_attributeValue(self):
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id='my-id'", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "my-id")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 9)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id=\"my-id\"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "my-id")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 9)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id = 'my-id'", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "my-id")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 11)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id = ' my-id ' ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " my-id ")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 13)
    string = "id \t\n= \n\t' \tmy-id '\n "
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(string, 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " \tmy-id ")
    self.assertEqual(startIdx, 0)
    self.assertTrue(endIdx > startIdx)
    self.assertEqual(endIdx, string.find("'\n "))
    string = "\t\r\n id \t\n= \n\t' \tmy-id '\r\n "
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(string, 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " \tmy-id ")
    self.assertEqual(startIdx, 4)
    self.assertEqual(endIdx, string.find("'\r\n "))
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id = 'id1 id2'", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "id1 id2")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 13)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id = ' id1 id2 id3 '", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " id1 id2 id3 ")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 19)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("\tid = '\r\n id1 id2 id3 \n\t'\t\t", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "\r\n id1 id2 id3 \n\t")
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, 24)
    string = "\tid = '\r\n id1 \t id2 \t id3 \n\t'\t\t"
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(string, 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "\r\n id1 \t id2 \t id3 \n\t")
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, string.find("'\t\t"))
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id = 'id1 id2' id=\"my-other-id\"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "id1 id2")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 13)

  def test_getNextHtmlAttribute_startIdxGreaterThan1(self):
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected", 2)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "lected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 2)
    self.assertEqual(endIdx, 7)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected='False'", 3)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "ected")
    self.assertEqual(attributeValue, "False")
    self.assertEqual(startIdx, 3)
    self.assertEqual(endIdx, 15)
    string = "\nselected\nclass\t=\t\"\tcl1\tcl2\tcl3 \" class id=\"my-id\"\n"
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(string, string.find("class"))
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "class")
    self.assertEqual(attributeValue, "\tcl1\tcl2\tcl3 ")
    self.assertTrue(startIdx > -1)
    self.assertTrue(endIdx > startIdx)
    self.assertEqual(startIdx, string.find("class"))
    self.assertEqual(endIdx, string.find("\" class id=\"my-id\""))

  def test_getListOfHtmlAttributeNames_nonSense(self):
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributeNames(12)
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributeNames(None)
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributeNames(False)
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributeNames([])

  def test_getListOfHtmlAttributeNames_onlyEmptyAndWhiteSpace(self):
    corrupt, attributes = attr.getListOfHtmlAttributeNames("")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])
    corrupt, attributes = attr.getListOfHtmlAttributeNames(" ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("\t")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("\n")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("  \t\t\t\t \r\r  ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("\n      \t   \t        \n")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])

  def helper_getListOfHtmlAttributeNames_checkIfCorrupt(self, attributesString):
    corrupt, attributeNames = attr.getListOfHtmlAttributeNames(attributesString)
    self.assertTrue(corrupt)
    self.assertEqual(attributeNames, [])

  def test_getListOfHtmlAttributeNames_corruptAttributes(self):
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("=")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("=12")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("='value'")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("'value'")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt(" = 'value'")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("\t\t=\t\t\" value \"")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected=")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt(" \t\t selected\n = \t")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected = \"")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected = '")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected = \"value")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected = 'value")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected 'value'")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected'value'")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected=='value'")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected= ='value'")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected == 'value'")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected 'value")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected'value")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected = \"value'")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("selected = 'value\"")
    self.helper_getListOfHtmlAttributeNames_checkIfCorrupt("class=\"example\" selected = 'value\" animated")

  def test_getListOfHtmlAttributeNames_oneAttribute(self):
    corrupt, attributes = attr.getListOfHtmlAttributeNames("a")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["a"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("selected")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["selected"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames(" \n  \t selected \n\r \t ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["selected"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("selected \n\r \t ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["selected"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames(" \n  \t selected")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["selected"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("style=\"float:right;margin:11px 14px 0 0;"
                                                     "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["style"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("style='float:right;margin:11px 14px 0 0;"
                                                     "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98'")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["style"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames(" \n\r style\t\t\t=\n'float:right;margin:11px 14px 0 0;"
                                               "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98' \n\r ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["style"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("style\t\t\t=\n'float:right;margin:11px 14px 0 0;"
                                               "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98' \n\r ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["style"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames(" \n\r style\t\t\t=\n'\t\tfloat:right;margin:11px 14px 0 0;"
                                         "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98\t\t' \n\r ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["style"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("\nproperty\n=\n\"\narticle:published_time\n\"\n")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["property"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("\nproperty\n=\n\"\narticle:published_time\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["property"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("property\n=\n\"\narticle:published_time\n\"\n")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["property"])

  def test_getListOfHtmlAttributeNames_moreAttributes(self):
    corrupt, attributes = attr.getListOfHtmlAttributeNames("selected id=\"logo\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["selected", "id"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("id=\"logo\" selected")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["id", "selected"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("id=\"logo\" selected id=\"otherId\" selected='true'")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["id", "selected"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("\tonclick\t=\t\"\tlocation.reload();\t\" "
          "style\n=\"float:right;"
          "display:inline-block;position:relative;top:15px;right:3px;margin-left:10px;font-size:13px;cursor:pointer\" "
          "title='Exclude inappropriate or explicit images'")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["onclick", "style", "title"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("rel=\"alternate\" type=\"application/rss+xml\" "
                     "title=\"Matematika és Informatika Kar RSS Feed\" href=\"https://www.cs.ubbcluj.ro/hu/feed/\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["rel", "type", "title", "href"])

  def test_getNextHtmlAttributeValueIfExists_nonSense(self):
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists(None, None)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists(False, 0)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists("= 'value'", True)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists("= 'value'", 56)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists("= 'value'", -1)

  def test_getNextHtmlAttributeValueIfExists_emptyString(self):
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists("", 0)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("='value' ", 8)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def test_getNextHtmlAttributeValueIfExists_spaces(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" \t\t\n", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" \t\t \n ", 3)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(self, corrupt, firstQuoteIdx, secondQuoteIdx):
    self.assertTrue(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(self, corrupt, firstQuoteIdx, secondQuoteIdx):
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def test_getNextHtmlAttributeValueIfExists_corrupt(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("==", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=========", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("''", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\"\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("'value'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\"value\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("='\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\"'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= \t \n", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= \n\t value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= value ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\t\t\n = \n\tvalue\n\n\n", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=2", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= 2", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=value\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=value'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\"value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("='value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\"value'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("='value\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= \"value'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= 'value\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=   \"  value  '  ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=  '  value  \"  ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\t\t=   \"  value  '  ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=  '  value  \"  ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)

  def test_getNextHtmlAttributeValueIfExists_noValue(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("X", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("attrName", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("multiple attribute names", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("attrName\t", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\tattrName", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("attrName\t\n", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\tattrName", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("   \t attrName  \t\t  \t", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("selected class='myClass'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(
                                                                                  "\t\tselected\n\nclass='myClass'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)

  def test_getNextHtmlAttributeValueIfExists_emptyValue(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\"\"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 1)
    self.assertEqual(secondQuoteIdx, 2)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" = \"\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 3)
    self.assertEqual(secondQuoteIdx, 4)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t\"\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 8)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t'' ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 8)

  def test_getNextHtmlAttributeValueIfExists_whiteSpaceValue(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\" \"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 1)
    self.assertEqual(secondQuoteIdx, 3)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" = \"\n\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 3)
    self.assertEqual(secondQuoteIdx, 5)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t\"\t\n\t\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 11)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t'\t\n\t' ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 11)

  def test_getNextHtmlAttributeValueIfExists_nonEmptyValue(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\"value\"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 1)
    self.assertEqual(secondQuoteIdx, 7)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" = \"value\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 3)
    self.assertEqual(secondQuoteIdx, 9)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t\"value\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 13)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t'value' ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 13)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t'\t value\n\n' ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 17)

  def test_getNextHtmlAttributeValueIfExists_nonZeroStartIdx(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t'\t value\n\n' ", 2)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 17)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t\"\t\n\t\" ", 3)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 11)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t\"\t\n\t\" ", 4)
    self.assertTrue(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" = \"\" ", 1)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 3)
    self.assertEqual(secondQuoteIdx, 4)

  def test_getNextHtmlAttributeName_nonSense(self):
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeName(None, None)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeName(False, 0)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeName("= 'value'", True)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeName("= 'value'", 56)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeName("= 'value'", -1)

  def test_getNextHtmlAttributeName_emptyString(self):
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeName("", 0)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("='value' ", 8)
    self.assertFalse(corrupt)
    self.assertIsNone(attributeName)
    self.assertEqual(firstCharIdx, -1)
    self.assertEqual(lastCharIdx, -1)

  def helper_getNextHtmlAttributeName_checkIfNoName(self, corrupt, attributeName, firstCharIdx, lastCharIdx):
    self.assertFalse(corrupt)
    self.assertIsNone(attributeName, -1)
    self.assertEqual(firstCharIdx, -1)
    self.assertEqual(lastCharIdx, -1)

  def helper_getNextHtmlAttributeName_checkIfCorrupt(self, corrupt, attributeName, firstCharIdx, lastCharIdx):
    self.assertTrue(corrupt)
    self.assertIsNone(attributeName, -1)
    self.assertEqual(firstCharIdx, -1)
    self.assertEqual(lastCharIdx, -1)

  def test_getNextHtmlAttributeName_spaces(self):
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(" ", 0)
    self.helper_getNextHtmlAttributeName_checkIfNoName(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("\n", 0)
    self.helper_getNextHtmlAttributeName_checkIfNoName(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(" \t\t\n", 0)
    self.helper_getNextHtmlAttributeName_checkIfNoName(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(" \t\t \n ", 3)
    self.helper_getNextHtmlAttributeName_checkIfNoName(corrupt, attributeName, firstCharIdx, lastCharIdx)

  def test_getNextHtmlAttributeName_corrupt(self):
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("=", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("= ", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(" =", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(" = ", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("\t\t=\n\n", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("'", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("''''''''", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("' ", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(" '", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(" ' ", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("\t\t'\n\n", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("\"", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("\" ", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(" \"", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(" \" ", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("\t\t\"\n\n", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("='value'", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(" = ' value ' ", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("=value'", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("class'myClass'", 0)
    self.helper_getNextHtmlAttributeName_checkIfCorrupt(corrupt, attributeName, firstCharIdx, lastCharIdx)

  def test_getNextHtmlAttributeName_attrNameFound(self):
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("X", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "X")
    self.assertEqual(firstCharIdx, 0)
    self.assertEqual(lastCharIdx, 0)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("\t\tX\t\t", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "X")
    self.assertEqual(firstCharIdx, 2)
    self.assertEqual(lastCharIdx, 2)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("\t\tX\t\tY Z", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "X")
    self.assertEqual(firstCharIdx, 2)
    self.assertEqual(lastCharIdx, 2)
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("selected", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(firstCharIdx, 0)
    self.assertEqual(lastCharIdx, len("selected") - 1)
    string = "\t\tselected\n\n"
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(string, 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(string[firstCharIdx], "s")
    self.assertEqual(string[lastCharIdx], "d")
    string = " class='my-Class' \t selected"
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(string, 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "class")
    self.assertEqual(string[firstCharIdx:lastCharIdx + 1], attributeName)
    string = "\n\nclass\t\t=\t\n'   my-Class' \r\n\t selected"
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(string, 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "class")
    self.assertEqual(string[firstCharIdx:lastCharIdx + 1], attributeName)
    string = "multiple words in this string"
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(string, 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "multiple")
    self.assertEqual(string[firstCharIdx:lastCharIdx + 1], attributeName)

  def test_getNextHtmlAttributeName_nonZeroStartIdx(self):
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName("selected", 3)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "ected")
    self.assertEqual(firstCharIdx, 3)
    self.assertEqual(lastCharIdx, len("selected") - 1)
    string = "multiple words in this string"
    corrupt, attributeName, firstCharIdx, lastCharIdx = attr.getNextHtmlAttributeName(string, 22)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "string")
    self.assertEqual(string[firstCharIdx:lastCharIdx + 1], attributeName)

  def test_getHtmlAttributes_nonSense(self):
    with self.assertRaises(Exception):
      attr.getHtmlAttributes(None, 0)
    with self.assertRaises(Exception):
      attr.getHtmlAttributes(123, 0)
    with self.assertRaises(Exception):
      attr.getHtmlAttributes("selected", False)
    with self.assertRaises(Exception):
      attr.getHtmlAttributes("selected", [])
    with self.assertRaises(Exception):
      attr.getHtmlAttributes("selected", -1)
    with self.assertRaises(Exception):
      attr.getHtmlAttributes("selected", 58)

  def test_getHtmlAttributes_emptyString(self):
    with self.assertRaises(Exception):
      attr.getHtmlAttributes("", 0)
    with self.assertRaises(Exception):
      attr.getHtmlAttributes("", 1)

  def helper_getHtmlAttributes_checkIfAttrNotFound(self, corrupt, attributes):
    self.assertFalse(corrupt)
    self.assertEqual(attributes, {})

  def test_getHtmlAttributes_emptyString(self):
    corrupt, attributes = attr.getHtmlAttributes(" ", 0)
    self.helper_getHtmlAttributes_checkIfAttrNotFound(corrupt, attributes)
    corrupt, attributes = attr.getHtmlAttributes("   ", 0)
    self.helper_getHtmlAttributes_checkIfAttrNotFound(corrupt, attributes)
    corrupt, attributes = attr.getHtmlAttributes("\t", 0)
    self.helper_getHtmlAttributes_checkIfAttrNotFound(corrupt, attributes)
    corrupt, attributes = attr.getHtmlAttributes("\r\n", 0)
    self.helper_getHtmlAttributes_checkIfAttrNotFound(corrupt, attributes)
    corrupt, attributes = attr.getHtmlAttributes("\t  \n  \t\r\n", 0)
    self.helper_getHtmlAttributes_checkIfAttrNotFound(corrupt, attributes)

  def helper_getHtmlAttributes_checkIfCorrupt(self, corrupt, attributes):
    self.assertTrue(corrupt)
    self.assertEqual(attributes, {})

  def test_getHtmlAttributes_corrupt(self):
    corrupt, attributes = attr.getHtmlAttributes("'", 0)
    self.helper_getHtmlAttributes_checkIfCorrupt(corrupt, attributes)
    corrupt, attributes = attr.getHtmlAttributes("'''", 0)
    self.helper_getHtmlAttributes_checkIfCorrupt(corrupt, attributes)

  def test_htmlDelimitedFromLeft_nonSense(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft(False, 0)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft("This is a string sample", None)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft(0, "Something")
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft("Something", -1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft("Something", 341)

  def test_htmlDelimitedFromLeft_emptyString(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft("", 0)

  def test_htmlDelimitedFromLeft_indexZero(self):
    self.assertTrue(attr.htmlDelimitedFromLeft("Q", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft(" Q", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("ab", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("a b", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft(" a b ", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("abc", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("'abc'", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("a b c", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft(" a b c ", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("heyho-engineer", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("heyho engineer", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft(" heyho engineer ", 0))

  def test_htmlDelimitedFromLeft_notDelimitated(self):
    self.assertFalse(attr.htmlDelimitedFromLeft("special-table", 8))
    self.assertFalse(attr.htmlDelimitedFromLeft("XtableX", 4))
    self.assertFalse(attr.htmlDelimitedFromLeft("XtableX", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("[table]", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("[ table ]", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft(",'table','span'", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("(table)", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("-table-", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("<table>", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("<a href='img/logo.png'>", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("fa fa-btn fa-lg", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("fa fa-btn fa-lg", 6))

  def test_htmlDelimitedFromLeft_delimitated(self):
    self.assertTrue(attr.htmlDelimitedFromLeft(" my-class", 1))
    self.assertTrue(attr.htmlDelimitedFromLeft("class-1 my-class", 8))
    self.assertTrue(attr.htmlDelimitedFromLeft("class='my-class'", 7))
    self.assertTrue(attr.htmlDelimitedFromLeft('class="my-class"', 7))
    self.assertTrue(attr.htmlDelimitedFromLeft("class='my-class'", 6))
    self.assertTrue(attr.htmlDelimitedFromLeft('class="my-class"', 6))
    self.assertTrue(attr.htmlDelimitedFromLeft("=2", 1))

  def test_htmlDelimitedFromRight_nonSense(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight(False, 0)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight("This is a string sample", None)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight(0, "Something")
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight("Something", -1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight("Something", 341)

  def test_htmlDelimitedFromRight_emptyString(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight("", 0)

  def test_htmlDelimitedFromRight_indexOfLastCharacter(self):
    self.assertTrue(attr.htmlDelimitedFromRight("Q", 0))
    self.assertTrue(attr.htmlDelimitedFromRight(" Q", 1))
    self.assertTrue(attr.htmlDelimitedFromRight("ab", 1))
    self.assertTrue(attr.htmlDelimitedFromRight("a b", 2))
    self.assertTrue(attr.htmlDelimitedFromRight(" a b ", 4))
    self.assertTrue(attr.htmlDelimitedFromRight("abc", 2))
    self.assertTrue(attr.htmlDelimitedFromRight("'abc'", 4))
    self.assertTrue(attr.htmlDelimitedFromRight("a b c", 4))
    self.assertTrue(attr.htmlDelimitedFromRight(" a b c ", 6))
    self.assertTrue(attr.htmlDelimitedFromRight("heyho-engineer", 13))
    self.assertTrue(attr.htmlDelimitedFromRight("heyho engineer", 13))
    self.assertTrue(attr.htmlDelimitedFromRight(" heyho engineer ", 15))

  def test_htmlDelimitedFromRight_notDelimitated(self):
    self.assertFalse(attr.htmlDelimitedFromRight("special-table", 6))
    self.assertFalse(attr.htmlDelimitedFromRight("tableX", 4))
    self.assertFalse(attr.htmlDelimitedFromRight("table_X", 1))
    self.assertFalse(attr.htmlDelimitedFromRight("table@X", 1))
    self.assertFalse(attr.htmlDelimitedFromRight("[table]", 5))
    self.assertFalse(attr.htmlDelimitedFromRight("'table','span'", 6))
    self.assertFalse(attr.htmlDelimitedFromRight("(table)", 5))
    self.assertFalse(attr.htmlDelimitedFromRight("-table-", 5))
    self.assertFalse(attr.htmlDelimitedFromRight("<table>", 5))
    self.assertFalse(attr.htmlDelimitedFromRight("<a xhref='img/logo.png'>", 3))
    self.assertFalse(attr.htmlDelimitedFromRight("fa fa-btn fa-lg", 0))
    self.assertFalse(attr.htmlDelimitedFromRight("fa fa-btn fa-lg", 4))

  def test_htmlDelimitedFromRight_delimitated(self):
    self.assertTrue(attr.htmlDelimitedFromRight("my-class ", 7))
    self.assertTrue(attr.htmlDelimitedFromRight("class-1 my-class", 6))
    self.assertTrue(attr.htmlDelimitedFromRight("class='my-class'", 4))
    self.assertTrue(attr.htmlDelimitedFromRight("class'my-class'", 4))
    self.assertTrue(attr.htmlDelimitedFromRight("class\"my-class\"", 4))
    self.assertTrue(attr.htmlDelimitedFromRight("class='my-class'", 5))
    self.assertTrue(attr.htmlDelimitedFromRight('class="my-class"', 5))
    self.assertTrue(attr.htmlDelimitedFromRight("  class='my-class'", 0))
    self.assertTrue(attr.htmlDelimitedFromRight(" 'my-class'", 0))
    self.assertTrue(attr.htmlDelimitedFromRight(" \"my-class\"", 0))
    self.assertTrue(attr.htmlDelimitedFromRight("class='my-class'", 14))
    self.assertTrue(attr.htmlDelimitedFromRight("class='my-class your-class'", 14))
    self.assertTrue(attr.htmlDelimitedFromRight('class="my-class"', 14))
    self.assertTrue(attr.htmlDelimitedFromRight("=2 ", 1))

  def test_charIsHtmlDelimiter_nonSense(self):
    with self.assertRaises(Exception):
      attr.charIsHtmlDelimiter(None)
    with self.assertRaises(Exception):
      attr.charIsHtmlDelimiter(12)
    with self.assertRaises(Exception):
      attr.charIsHtmlDelimiter(True)
    with self.assertRaises(Exception):
      attr.charIsHtmlDelimiter([])
    with self.assertRaises(Exception):
      attr.charIsHtmlDelimiter("string")

  def test_charIsHtmlDelimiter_delimiter(self):
    self.assertTrue(attr.charIsHtmlDelimiter("="))
    self.assertTrue(attr.charIsHtmlDelimiter("'"))
    self.assertTrue(attr.charIsHtmlDelimiter('"'))
    self.assertTrue(attr.charIsHtmlDelimiter(" "))
    self.assertTrue(attr.charIsHtmlDelimiter("\t"))
    self.assertTrue(attr.charIsHtmlDelimiter("\r"))
    self.assertTrue(attr.charIsHtmlDelimiter("\n"))

  def test_charIsHtmlDelimiter_notDelimiter(self):
    self.assertFalse(attr.charIsHtmlDelimiter("<"))
    self.assertFalse(attr.charIsHtmlDelimiter(">"))
    self.assertFalse(attr.charIsHtmlDelimiter("["))
    self.assertFalse(attr.charIsHtmlDelimiter("]"))
    self.assertFalse(attr.charIsHtmlDelimiter("("))
    self.assertFalse(attr.charIsHtmlDelimiter(")"))
    self.assertFalse(attr.charIsHtmlDelimiter("0"))
    self.assertFalse(attr.charIsHtmlDelimiter("a"))
    self.assertFalse(attr.charIsHtmlDelimiter("Z"))
    self.assertFalse(attr.charIsHtmlDelimiter("_"))
    self.assertFalse(attr.charIsHtmlDelimiter("-"))
    self.assertFalse(attr.charIsHtmlDelimiter("#"))
    self.assertFalse(attr.charIsHtmlDelimiter("."))

  def test_stringIsHtmlDelimited_nonSense(self):
    with self.assertRaises(Exception):
      attr.stringIsHtmlDelimited("string", 0, False)
    with self.assertRaises(Exception):
      attr.stringIsHtmlDelimited("string", True, 2)
    with self.assertRaises(Exception):
      attr.stringIsHtmlDelimited(2341, 0, 2)
    with self.assertRaises(Exception):
      attr.stringIsHtmlDelimited(False, True, False)
    with self.assertRaises(Exception):
      attr.stringIsHtmlDelimited(None, None, None)

  def test_stringIsHtmlDelimited_delimited(self):
    self.assertTrue(attr.stringIsHtmlDelimited("012345678", 0, 9))
    self.assertTrue(attr.stringIsHtmlDelimited("0", 0, 1))
    self.assertTrue(attr.stringIsHtmlDelimited("01", 0, 2))
    self.assertTrue(attr.stringIsHtmlDelimited("012", 0, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc def ghi", 0, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc def ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc def ghi", 8, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc=def=ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("=abc=def=ghi=", 5, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc'def'ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc\"def\"ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc'def\"ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc\"def'ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc\tdef\tghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc\tdef\nghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc'''def'''ghi", 6, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("'abc' 'def' 'ghi'", 7, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("'abc' =def' 'ghi'", 7, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("'abc' 'def= 'ghi'", 7, 3))

  def test_stringIsHtmlDelimited_notDelimited(self):
    self.assertFalse(attr.stringIsHtmlDelimited("012345678", 1, 7))
    self.assertFalse(attr.stringIsHtmlDelimited("012345678", 1, 8))
    self.assertFalse(attr.stringIsHtmlDelimited("012345678", 0, 4))
    self.assertFalse(attr.stringIsHtmlDelimited("qwe_asd_zxc", 4, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("qwe[asd]zxc", 4, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("qwe [asd] zxc", 5, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("qwe <asd> zxc", 4, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("truth:1+1=2", 6, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("truth=1+1<3", 6, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("truth: '1+1>1'", 8, 3))
    self.assertFalse(attr.stringIsHtmlDelimited('truth: "3<1+1>1"', 10, 3))

  def test_thereIsAttributeNameBeforeIdx_nonSense(self):
    with self.assertRaises(Exception):
      attr.thereIsAttributeNameBeforeIdx("text", -1)
    with self.assertRaises(Exception):
      attr.thereIsAttributeNameBeforeIdx("text", 123)
    with self.assertRaises(Exception):
      attr.thereIsAttributeNameBeforeIdx("text", 4)
    with self.assertRaises(Exception):
      attr.thereIsAttributeNameBeforeIdx(12, 123)
    with self.assertRaises(Exception):
      attr.thereIsAttributeNameBeforeIdx(False, 0)
    with self.assertRaises(Exception):
      attr.thereIsAttributeNameBeforeIdx(None, None)

  def test_thereIsAttributeNameBeforeIdx_emptyString(self):
    with self.assertRaises(Exception):
      attr.thereIsAttributeNameBeforeIdx("", 0)

  def test_thereIsAttributeNameBeforeIdx_thereIsNot(self):
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx("text", 0))
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx("this is an another string", 0))
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx("number=2", 7))
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx("number='2'", 8))
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx("number='2'", 7))
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx("number = 2", 9))
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx("number = '2'", 10))
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx("number '2'", 8))
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx('number="2"', 8))
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx('number="2"', 7))
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx('number = "2"', 10))
    self.assertFalse(attr.thereIsAttributeNameBeforeIdx('number "2"', 8))

  def test_thereIsAttributeNameBeforeIdx_thereIs(self):
    self.assertTrue(attr.thereIsAttributeNameBeforeIdx("text", 3))
    self.assertTrue(attr.thereIsAttributeNameBeforeIdx("this is an another string", 11))
    self.assertTrue(attr.thereIsAttributeNameBeforeIdx("this is an another string", 15))
    self.assertTrue(attr.thereIsAttributeNameBeforeIdx("one-two-three", 4))
    self.assertTrue(attr.thereIsAttributeNameBeforeIdx("one-two-three", 1))
    self.assertTrue(attr.thereIsAttributeNameBeforeIdx("value = 'one'", 6))
    self.assertTrue(attr.thereIsAttributeNameBeforeIdx("value= 'one'", 5))
    self.assertTrue(attr.thereIsAttributeNameBeforeIdx("value='one'", 5))

  def test_nextNonWhiteSpaceCharIsHtmlDelimiter_nonSense(self):
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter("string", -1)
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter("string", 523)
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter("string", 6)
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter(False, 0)
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter("string", True)
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter(None, [])

  def test_nextNonWhiteSpaceCharIsHtmlDelimiter_itIsNot(self):
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X ", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("     ", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(" \t \r \n ", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X     ", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X     ", 1))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X\t\r\n", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X\t\r\n", 1))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("abcdefgh", 3))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("0123456789", 9))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("one-two-three", 2))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("one two three", 2))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("one\t\ttwo\t\t\tthree", 2))

  def test_nextNonWhiteSpaceCharIsHtmlDelimiter_itIs(self):
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(" 'value'", 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(" 'value'", 6))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(" \t 'value' ", 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(" \t 'value ' ", 9))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(' "value"', 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(' = "value"', 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter('\t\t\r\n"value"', 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter('\t\t\r\n="value"', 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter('attr\t = "value"', 3))

  def test_isThereAnyQuoteChar_nonSense(self):
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", -1, 3)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", 0, 6)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", -20, 146)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", 2, True)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", "", 4)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", [], {})
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar(None, 0, 0)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar(None, None, None)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar(True, False, True)

  def test_isThereAnyQuoteChar_emptyString(self):
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("", 0, 0)

  def test_isThereAnyQuoteChar_thereIs(self):
    self.assertTrue(attr.isThereAnyQuoteChar("'", 0, 0))
    self.assertTrue(attr.isThereAnyQuoteChar("'''''''''", 0, 8))
    self.assertTrue(attr.isThereAnyQuoteChar("\"\"\"\"'''''", 0, 8))
    self.assertTrue(attr.isThereAnyQuoteChar("\"\"\"\"'''''", 2, 5))
    self.assertTrue(attr.isThereAnyQuoteChar('"', 0, 0))
    self.assertTrue(attr.isThereAnyQuoteChar('"""""""""', 0, 8))
    self.assertTrue(attr.isThereAnyQuoteChar("1'2", 0, 2))
    self.assertTrue(attr.isThereAnyQuoteChar("0123456789'9876543210", 0, 10))
    self.assertTrue(attr.isThereAnyQuoteChar("0123456789'9876543210", 10, 20))
    self.assertTrue(attr.isThereAnyQuoteChar("0123456789'9876543210", 5, 15))
    self.assertTrue(attr.isThereAnyQuoteChar("'one' \" two \"", 0, 12))
    self.assertTrue(attr.isThereAnyQuoteChar("'one' \" two \"", 2, 9))

  def test_isThereAnyQuoteChar_thereIsNot(self):
    self.assertFalse(attr.isThereAnyQuoteChar("Q", 0, 0))
    self.assertFalse(attr.isThereAnyQuoteChar("string", 0, 5))
    self.assertFalse(attr.isThereAnyQuoteChar("string", 1, 4))
    self.assertFalse(attr.isThereAnyQuoteChar("'value'", 1, 5))
    self.assertFalse(attr.isThereAnyQuoteChar("\"value\"", 1, 5))
    self.assertFalse(attr.isThereAnyQuoteChar("'''\"\"TEXT\"''''", 5, 8))
    self.assertFalse(attr.isThereAnyQuoteChar("'''\"\"TEXT\"''''", 6, 7))
    self.assertFalse(attr.isThereAnyQuoteChar("'''\"\"TEXT\"''''", 6, 6))

  def helper_validateAdjacentCharsNearEqualChar_checkIfThrows(self, arg1, arg2):
    with self.assertRaises(Exception):
      attr.validateAdjacentCharsNearEqualChar("string", -1)

  def test_validateAdjacentCharsNearEqualChar_nonSense(self):
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("string", -1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("string", 52)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("string", True)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("string", {})
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("string", [])
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows({}, 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows(None, None)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows(True, False)

  def test_validateAdjacentCharsNearEqualChar_emptyString(self):
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("", 0)

  def helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt(self, htmlString, equalIndex):
    result = attr.validateAdjacentCharsNearEqualChar(htmlString, equalIndex)
    self.assertEqual(result, (True, -1))

  def test_validateAdjacentCharsNearEqualChar_equalNotFound(self):
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("Q", 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("apple", 2)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("ab_cd", 2)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("01", 1)

  def test_validateAdjacentCharsNearEqualChar_corrupt(self):
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("=", 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("= = =", 1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("= 2", 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("= '", 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt(" = '", 1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("= \"", 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt(" = \"", 1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("'='", 1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt('"="', 1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("value = 2", 6)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt('value = \t', 6)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt('value =', 6)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("'field' = 'value'", 8)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("'field' = \"value\"", 8)

  def test_validateAdjacentCharsNearEqualChar_valid(self):
    corrupt, quoteIdx = attr.validateAdjacentCharsNearEqualChar("a='", 1)
    self.assertFalse(corrupt)
    self.assertEqual(quoteIdx, 2)
    corrupt, quoteIdx = attr.validateAdjacentCharsNearEqualChar("a = '", 2)
    self.assertFalse(corrupt)
    self.assertEqual(quoteIdx, 4)
    corrupt, quoteIdx = attr.validateAdjacentCharsNearEqualChar("a\t\n=\t\t\t\"", 3)
    self.assertFalse(corrupt)
    self.assertEqual(quoteIdx, 7)

  def test_getAndValidateClosingQuote_nonSense(self):
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("clas = 'fa-lg2'", -1)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("clas = 'fa-lg2'", 15)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("clas = 'fa-lg2'", 56)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("clas = 'fa-lg2'", True)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("clas = 'fa-lg2'", "")
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote(True, 0)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote(True, True)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote(None, None)

  def test_getAndValidateClosingQuote_emptyString(self):
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("", 0)

  def helper_getAndValidateClosingQuote_checkIfCorrupt(self, stringArg, indexArg):
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote(stringArg, indexArg)
    self.assertTrue(corrupt)
    self.assertEqual(closingQuoteIdx, -1)
    self.assertEqual(quoteChar, "")

  def test_getAndValidateClosingQuote_idxIsNotQuote(self):
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("Q", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("QxQ", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("Lx", 1)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("apple", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("'apple'", 1)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("'apple'", 3)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = \"apple\"", 6)

  def test_getAndValidateClosingQuote_thereIsNoClosingQuote(self):
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("'Q", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("\"Q", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'myClass yourClass", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'myClass\"", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = \"myClass yourClass", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = \"myClass'", 8)

  def test_getAndValidateClosingQuote_thereIsClosingQuoteButCorrupt(self):
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("'Q'=", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("\"Q\"=", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'number = 2'=3", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'number = 2'    =   3", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'number = 2''", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'number = 2'\n\t\t\n' hello", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'number = 2'\n\n' hello'", 8)

  def test_getAndValidateClosingQuote_valid(self):
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote("'apple'", 0)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 6)
    self.assertEqual(quoteChar, "'")
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('"myClass yourClass"', 0)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 18)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('" myClass yourClass "', 0)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 20)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('title = "it\'s a title"', 8)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 21)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('title = "it\'s a title" id = "specialId"', 8)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 21)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('title = "it\'s a title" id = \'specId\'', 8)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 21)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('class = "specialClass" id = "specialId"', 28)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 38)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote("integrity=\"sha512-6PM0qxuIQ==\"", 10)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 29)
    self.assertEqual(quoteChar, '"')

  def test_getQuoteIndexesAfterEqualChar_nonSense(self):
    with self.assertRaises(Exception):
      attr.getQuoteIndexesAfterEqualChar("string", -1)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesAfterEqualChar("string", 42)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesAfterEqualChar("string", 6)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesAfterEqualChar("string", "")
    with self.assertRaises(Exception):
      attr.getQuoteIndexesAfterEqualChar("string", True)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesAfterEqualChar("string", None)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesAfterEqualChar(True, 0)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesAfterEqualChar(2, 0)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesAfterEqualChar(None, None)

  def test_getQuoteIndexesAfterEqualChar_emptyString(self):
    with self.assertRaises(Exception):
      attr.getQuoteIndexesAfterEqualChar("", 0)

  def helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt(self, string, equalCharIdx):
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                            = attr.getQuoteIndexesAfterEqualChar(string, equalCharIdx)
    self.assertTrue(corrupt)
    self.assertEqual(openingQuoteCharIdx, -1)
    self.assertEqual(closingQuoteIdx, -1)
    self.assertEqual(mainQuoteChar, "")

  def test_getQuoteIndexesAfterEqualChar_notEqualChar(self):
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("Q", 0)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("'Q'", 1)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("apple", 4)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("class = 'myClass'", 0)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("class = \"myClass\"", 0)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("class = 'myClass'", 5)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("class = \"myClass\"", 5)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("class = 'myClass'", 7)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("class = \"myClass\"", 7)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("class = 'myClass'", 8)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("class = \"myClass\"", 8)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("class = 'myClass'", 11)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("class = \"myClass\"", 11)

  def test_getQuoteIndexesAfterEqualChar_noQuotes(self):
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("=", 0)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("= 2", 0)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value = 2", 6)

  def test_getQuoteIndexesAfterEqualChar_onlyOneMainQuote(self):
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("= '2", 0)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("= \"2", 0)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("= 2'", 0)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("= 2\"", 0)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value = '", 6)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value ='", 6)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value = \"", 6)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value =\"", 6)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value = 2'", 6)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value = 2\"", 6)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value = '2", 6)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value = \"2", 6)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value = \"2'", 6)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value = '2\"", 6)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value = '2\"\"\"", 6)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("value = \"2'''", 6)

  def test_getQuoteIndexesAfterEqualChar_otherInvalid(self):
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("= '2'", 0)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("\" = '2'", 2)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("\t\t\t = '2'", 4)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("\t\t\t = '2''", 4)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("\t\t\t = '''", 4)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("\t\t\t = ''''", 4)
    self.helper_getQuoteIndexesAfterEqualChar_checkIfCorrupt("\t\t\t = '''''", 4)

  def test_getQuoteIndexesAfterEqualChar_validEmptyValue(self):
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                  = attr.getQuoteIndexesAfterEqualChar("value=''\tdisabled='False'", 5)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (6, 7, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar("value=''", 5)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (6, 7, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar("value =''", 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (7, 8, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar("value = ''", 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 9, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                        = attr.getQuoteIndexesAfterEqualChar("value\n\t=\t\r\n\t''", 7)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (12, 13, "'"))

    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar('value=""', 5)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (6, 7, "\""))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar('value =""', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (7, 8, "\""))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar('value = ""', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 9, "\""))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                        = attr.getQuoteIndexesAfterEqualChar('value\n\t=\t\r\n\t""', 7)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (12, 13, "\""))

  def test_getQuoteIndexesAfterEqualChar_validNonEmptyValue(self):
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar("value=' '", 5)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (6, 8, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar('value=" "', 5)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (6, 8, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar("value =' '", 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (7, 9, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar('value =" "', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (7, 9, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar("value = ' '", 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 10, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesAfterEqualChar('value = " "', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 10, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                    = attr.getQuoteIndexesAfterEqualChar('value = " \t "', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 12, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                    = attr.getQuoteIndexesAfterEqualChar('value = "test"', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 13, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                    = attr.getQuoteIndexesAfterEqualChar('value = "\ttest1 test2 "', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 22, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                    = attr.getQuoteIndexesAfterEqualChar("value = '\ttest1 test2 '", 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 22, "'"))

    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                              = attr.getQuoteIndexesAfterEqualChar("integrity='sha512-6PM0qxuIQ=='", 9)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (10, 29, "'"))

  def test_htmlDelimitedFind_nonSense(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind(None, "findThis", 0, 1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", None, 0, 1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind(0, 12, 0, 1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", None, 1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", 0, None)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", True, False)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", "", "")
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", 3, 3)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", -2, 3)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", 1, 56)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", 10, 4)

  def test_htmlDelimitedFind_emptyStrings(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("", "findThis", 0, 1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("find something in this string", "", 0, 1)

  def helper_htmlDelimitedFind_checkNotFound(self, stringToScan, stringToMatch, startIdx, endIdx):
    found, firstIdx = attr.htmlDelimitedFind(stringToScan, stringToMatch, startIdx, endIdx)
    self.assertFalse(found)
    self.assertEqual(firstIdx, -1)

  def test_htmlDelimitedFind_stringNotFoundAtAll(self):
    self.helper_htmlDelimitedFind_checkNotFound("a", "b", 0, 1)
    self.helper_htmlDelimitedFind_checkNotFound("this is my string", "findMe", 0, 17)
    self.helper_htmlDelimitedFind_checkNotFound("this is my lovely little string", "this", 1, 31)
    self.helper_htmlDelimitedFind_checkNotFound("this is my lovely little string", "string", 0, 27)
    self.helper_htmlDelimitedFind_checkNotFound("this is my lovely little string", "my", 11, 24)
    self.helper_htmlDelimitedFind_checkNotFound("this is my lovely little string", "string", 11, 24)

  def test_htmlDelimitedFind_foundStringIsNotHtmlDelimited(self):
    self.helper_htmlDelimitedFind_checkNotFound("pineapple", "pine", 0, 9)
    self.helper_htmlDelimitedFind_checkNotFound("pineapple", "apple", 0, 9)
    self.helper_htmlDelimitedFind_checkNotFound("pineapple", "neapple", 0, 9)
    self.helper_htmlDelimitedFind_checkNotFound("one-two-three", "one", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one-two-three", "two", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one-two-three", "three", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one;two;three", "one", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one;two;three", "two", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one;two;three", "three", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one,two,three", "one", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one,two,three", "two", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one,two,three", "three", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one, two, three.", "one", 0, 16)
    self.helper_htmlDelimitedFind_checkNotFound("one, two, three.", "two", 0, 16)
    self.helper_htmlDelimitedFind_checkNotFound("one, two, three.", "three", 0, 16)

  def test_htmlDelimitedFind_stringFound(self):
    found, firstIdx = attr.htmlDelimitedFind("one two three", "one", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 0)
    found, firstIdx = attr.htmlDelimitedFind("one two three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one two three", "three", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 8)
    found, firstIdx = attr.htmlDelimitedFind("one=two=three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one'two'three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one\"two\"three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one'two\"three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one\"two'three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one=two'three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("'one'two=three", "two", 0, 14)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 5)
    found, firstIdx = attr.htmlDelimitedFind("a", "a", 0, 1)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 0)
    found, firstIdx = attr.htmlDelimitedFind("abc", "abc", 0, 3)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 0)
    found, firstIdx = attr.htmlDelimitedFind("value=2", "2", 2, 7)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 6)
    found, firstIdx = attr.htmlDelimitedFind("value=2", "value", 0, 7)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 0)
    found, firstIdx = attr.htmlDelimitedFind("hrefx='2' href", "href", 0, 14)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 10)
    found, firstIdx = attr.htmlDelimitedFind("hrefx='2' rel='xhref' href", "href", 0, 26)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 22)
    found, firstIdx = attr.htmlDelimitedFind("hrefx='2' rel='xhref' hrefhrefhref href", "href", 0, 39)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 35)

  def test_indexIsWithinHtmlAttributeValue_nonSense(self):
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue("text", "")
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue(0, 0)
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue(None, None)
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue([], True)
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue("this is a text", -1)
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue("this is a text", 341)
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue("this is a text", 14)

  def test_indexIsWithinHtmlAttributeValue_emptyString(self):
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue("", 0)

  def helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt(self, string, index):
    corrupt, isAttributeValue = attr.indexIsWithinHtmlAttributeValue(string, index)
    self.assertTrue(corrupt)
    self.assertIsNone(isAttributeValue)

  def helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName(self, string, index):
    corrupt, isAttributeValue = attr.indexIsWithinHtmlAttributeValue(string, index)
    self.assertFalse(corrupt)
    self.assertFalse(isAttributeValue)

  def helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue(self, string, index):
    corrupt, isAttributeValue = attr.indexIsWithinHtmlAttributeValue(string, index)
    self.assertFalse(corrupt)
    self.assertTrue(isAttributeValue)

  def test_indexIsWithinHtmlAttributeValue_corrupt_quoteCharButNotEqualFound(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("''", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'''", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("''''", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("''''", 2)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("''''", 3)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("''", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"\"", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"\"", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'apple", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'apple", 4)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("apple'", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("apple'", 3)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("apple'", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("ap'ple", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("ap'ple", 3)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"apple\"", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"apple\"", 2)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'apple'", 2)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'carrot' 'apple'", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'carrot apple'", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'carrot apple'", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'carrot apple'", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot'apple", 3)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot'apple", 6)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot'apple", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot''''''apple", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot''''''apple", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot' 'apple", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot\" 'apple", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot' \"apple", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot\" \"apple", 7)

  def test_indexIsWithinHtmlAttributeValue_corrupt_equalButNotQuoteFound(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("=", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= ", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= ", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= 2", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= 2", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= 2", 2)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 234", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 17)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 20)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 21)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 22)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 28)

  def test_indexIsWithinHtmlAttributeValue_corrupt_quotesAreNotCorrect(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = '2\"", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = \"2'", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = \"2", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = '2", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = '''2", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = '''2'", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = ''''2", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2'", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2''", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2'''", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2\"", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2\"'", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2\"\"'", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2\"''", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2'\"", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2'\"\"", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2''\"", 8)

  def test_indexIsWithinHtmlAttributeValue_corrupt_noAttributeValue(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= 'two'", 4)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\t\t\t=\t'two'", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt(" = 'two'", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= \"two\"", 4)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt(" = \"two\"", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'number' = 'two'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'number' = \"two\"", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"number\" = 'two'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("' = 'two'", 7)

  def test_indexIsWithinHtmlAttributeValue_corrupt_tooMuchQuotes(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = 'two''", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = 'two'''", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = ''two'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = ''two''", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = '''two'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = '''two''", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = '''two'''", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = ''two'''", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = 'two'''", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = 'two''", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = 'two''", 11)

  def test_indexIsWithinHtmlAttributeValue_corrupt_tooMuchEqual(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number == 'two'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = = 'two'", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number ='two'=", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number =\t'two'\t=", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number =\t'two'\t==", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number =\t'two'\t= '2'", 11)

  def test_indexIsWithinHtmlAttributeValue_attributeName(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName(" ", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("a", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("ab", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("ab", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("one two three", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("one two three", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("one two three", 3)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("one two three", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("one two three", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("one two three", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("one two three", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("class='myClass'", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("class='myClass'", 2)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("class='myClass'", 4)

  def test_indexIsWithinHtmlAttributeValue_attributeValue(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' '", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = \" \"", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' 'notEmpty=\"value\"", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' 'notEmpty='value'", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' 'notEmpty='value'", 21)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = \" \" class = 'myClass'", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' ' class = 'myClass'", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' ' class = 'myClass'", 24)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("id\t\t\t=\n\n'mainContent\t\n\tanyContent'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("id\t\t\t=\n\n'mainContent\t\n\tanyContent'", 20)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("id\t\t\t=\n\n'mainContent\t\n\tanyContent'", 21)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("id\t\t\t=\n\n'mainContent\t\n\tanyContent'", 22)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("id\t\t\t=\n\n'mainContent\t\n\tanyContent'", 25)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class = 'cl1 cl2'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class = 'cl1\"cl2'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class = \"cl1 cl2\"", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class = \"cl1'cl2\"", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class='cl1 cl2'", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class='cl1\"cl2'", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class=\"cl1 cl2\"", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class=\"cl1'cl2\"", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the title'\"", 14)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the title'\"", 15)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the title'\"", 16)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the title'\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the title'\"", 25)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the'title'\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the'title'\"", 25)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the=title'\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the=title'\"", 25)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is =the=title=\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is =the=title=\"", 25)

  def test_indexIsWithinHtmlAttributeValue_equalInAttributeValue(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title='='", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title='==='", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title='==='", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title='==='", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=two\"", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=two\"", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=two\"", 14)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number='two'\"", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number='two'\"", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number='two'\"", 14)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number='two'\"", 16)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 14)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 15)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 16)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 15)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 17)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 18)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 21)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 22)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 23)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input=number=two\"", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input=number=two\"", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input=number=two\"", 15)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input=number=two\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input=number=two\"", 20)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 20)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 21)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 22)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 25)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 26)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"class='myClass'\"class='myClass'", 30)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"class='myClass'\"class='myClass'", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"class='myClass'\"class='myClass'", 16)

  def test_indexIsWithinHtmlAttributeValue_equalMainCharAndBetween(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("class='myClass'", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("class='myClass'", 6)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("class='myClass'", 14)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("class = 'myClass'", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeName("class = 'myClass'", 7)

  def test_stringContainsHtmlDelimiter_nonSense(self):
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", 0, 67)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", 0, 7)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", 0, None)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", 0, True)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", -1, 4)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", 5, 2)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", None, 2)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", None, None)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter(None, 0, 2)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter(0, 0, 0)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter(None, None, None)

  def test_stringContainsHtmlDelimiter_true(self):
    result = attr.stringContainsHtmlDelimiter(" ", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("=", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("'", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("\"", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("\t", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("\n", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter(" '='= \"\" ", 0, 9)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("hello world!", 0, 12)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("hello world!", 5, 12)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("hello world!", 0, 6)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("hello world!", 2, 8)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("class='myClass'", 0, 15)
    self.assertTrue(result)

  def test_stringContainsHtmlDelimiter_false(self):
    result = attr.stringContainsHtmlDelimiter("Q", 0, 1)
    self.assertFalse(result)
    result = attr.stringContainsHtmlDelimiter("apple", 0, 5)
    self.assertFalse(result)
    result = attr.stringContainsHtmlDelimiter("'apple'", 1, 6)
    self.assertFalse(result)
    result = attr.stringContainsHtmlDelimiter("true != false", 0, 4)
    self.assertFalse(result)
    result = attr.stringContainsHtmlDelimiter("true != false", 8, 13)
    self.assertFalse(result)
