import sys
import unittest

sys.path.append('..')

from modules import htmlAttributes as attr

class HtmlAttributesTests(unittest.TestCase):

  def helper_getAttributeNameIdx_checkIfCorrupt(self, htmlAttributes, key):
    corrupt, keyFound, idx = attr.getAttributeNameIdx(htmlAttributes, key)
    self.assertTrue(corrupt)
    self.assertIsNone(keyFound)
    self.assertEqual(idx, -1)

  def helper_getAttributeNameIdx_checkIfNotFound(self, htmlAttributes, key):
    corrupt, keyFound, idx = attr.getAttributeNameIdx(htmlAttributes, key)
    self.assertFalse(corrupt)
    self.assertFalse(keyFound)
    self.assertEqual(idx, -1)

  def helper_getAttributeNameIdx_checkIfFoundAtIdx(self, htmlAttributes, key, foundAt):
    corrupt, keyFound, idx = attr.getAttributeNameIdx(htmlAttributes, key)
    self.assertFalse(corrupt)
    self.assertTrue(keyFound)
    self.assertEqual(idx, foundAt)

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
    self.helper_getAttributeNameIdx_checkIfNotFound("", "class")
    self.helper_getAttributeNameIdx_checkIfNotFound("id=\"content\" class=\"clearfix\"", "")

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
    self.helper_getAttributeNameIdx_checkIfCorrupt("b = 'a=\"2\"", "a")

  def test_getAttributeNameIdx_attrNotFound(self):
    self.helper_getAttributeNameIdx_checkIfNotFound("ax xa", "a")
    self.helper_getAttributeNameIdx_checkIfNotFound("aa", "a")
    self.helper_getAttributeNameIdx_checkIfNotFound("aaa", "a")
    self.helper_getAttributeNameIdx_checkIfNotFound("xacca", "a")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"'style\"selected", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"'style\" selected", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"'style\"", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"''style\"", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"''style'\"", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"''style''\"", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"'''''style\"", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('title="My \'fancy\' style"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('title="My style is \'not fancy\'"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('title="My \'fancy\' style is \'not fancy\'"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('title="My \'style\' is hardcore" id="red"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('class="style"id="red"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('class="style"id="style"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("class='custom style red'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("id=\"myId\" class='custom style red'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("class='custom-style'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("class='custom-style-red'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("class='style-custom'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("class='style'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("htmlAttribute", "class")
    self.helper_getAttributeNameIdx_checkIfNotFound("htmlAttribute no-href", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("htmlAttribute hrefx", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("htmlAttribute hrefhref", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("no-href class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("hrefx class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("hrefhref class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("selected no-href class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("selected hrefx class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("selected hrefhref class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("b = 'a=\"2\"'", "a")

  def test_getAttributeNameIdx_attrNotFound_cornerCase(self):
    self.helper_getAttributeNameIdx_checkIfNotFound("b = 'a=\"2\"", "class")
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("b = 'a=\"2\"", "b", foundAt=0)

  def test_getAttributeNameIdx_attrNotFound_equalWithinAttributeValue(self):
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"class='myClass'\"", "class")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"class='class='myClass''\"", "class")

  def test_getAttributeNameIdx_attrFound(self):
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("a", "a", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected", "selected", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("default='1'", "default", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("default=\"1\"", "default", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("default=\"1\"selected", "default", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("default=\"1\"selected", "selected", foundAt = 11)
    string = "value='234' selected"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "selected", foundAt = string.find("selected"))
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected class=\"className\"", "selected", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected greyed-out", "selected", foundAt = 0)
    string = "value='234' selected=\"false\""
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "selected", foundAt = string.find("selected"))
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected=\"false\" class=\"className\"", "selected", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected=\"false\" greyed-out", "selected", foundAt = 0)
    string = "htmlAttribute no-href href"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find(" href") + 1)
    string = "htmlAttribute hrefx href=\"value\""
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find("href="))
    string = "htmlAttribute hrefhref='value2' href='value3'"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find("href='value3'"))
    string = "no-href=\"noValue\" href class='idk'"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find("href class"))
    string = "hrefx href class='idk'"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find("href class"))

  def test_getAttributeNameIdx_attrFoundMultipleTime(self):
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected selected='false' selected selected", "selected",
                                                      foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("default='1' class=\"myClass\" default", "default", foundAt = 0)
    string = "htmlAttribute hrefhref='value2' href='value3' href href='val4'"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find("href='value3'"))

  def test_getAttributeNameIdx_attrFound_equalWithinAttributeValue(self):
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("title=\"class='myClass'\"class='myClass'", "class", foundAt = 23)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("title=\"class='myClass'\" class='myClass'", "class", foundAt=24)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("title=\"class='myClass'\"\t\t\tclass\n\t=\t\t'myClass'", "class",
                                                      foundAt = 26)

  def test_extractDifferentValuesByKey_nonSense(self):
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesByKey("option='audi' value='A'", "")
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesByKey("option='audi' value='A'", 123)
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesByKey("option='audi' value='A'", False)
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesByKey("option='audi' value='A'", None)
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesByKey("option='audi' value='A'", ["option"])
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesByKey(None, "option")
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesByKey(234, "src")
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesByKey(123, None)

  def test_extractDifferentValuesByKey_emptyAttributes(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("", "title")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("", "src")
    self.assertEqual(attributes, (False, None))

  def test_extractDifferentValuesByKey_attrNotFound(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("htmlAttribute no-href", "href")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("rel=\"shortcut icon\" "
                                                             "href=\"img/favicon.ico\" type=\"image/x-icon\"", "title")
    self.assertEqual(attributes, (False, None))
    # TODO error - if attributeValue, it is not corrupt
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("class=\""
                                                       "masthead_custom_styles\" is=\"custom-style\" id=\"ext-styles\" "
                                                       "nonce=\"tG2l8WDVY7XYzWdAOVtRzA\"", "style")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey(
                                                                              "src=\"jsbin/spf.vflset/spf.js\"", "alt")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("class=\"anim\"", "id")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("class=\"animated bold\"", "id")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("class=\"animated bold\" "
                                                                                "selected class=\"active-tab\"", "id")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "upgrade")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "masthead")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "dark")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "shell")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "chunked")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "e")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "disable")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "clas")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "lot")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("_value=\"audi\"", "value")
    self.assertEqual(attributes, (False, None))

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_attrDoesNotHaveValue(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"audi\" selected", "selected")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"audi\" selected class=\"myClass\"",
                                                                     "selected")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("selected value=\"audi\"", "selected")
    self.assertEqual(attributes, (False, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("selected", "selected")
    self.assertEqual(attributes, (False, None))

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_emptyValue(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"\"", "value")
    self.assertEqual(attributes, (False, []))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"  \"", "value")
    self.assertEqual(attributes, (False, []))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"\t\"", "value")
    self.assertEqual(attributes, (False, []))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\" \r\n \t \"", "value")
    self.assertEqual(attributes, (False, []))

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_corrupt(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("class='custom style red",
                                                                                       "style")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"   ", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value= ", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value= \n \t ", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"audi", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"audi'", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value='audi\"", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value \"audi\"", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value\"audi\"", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value 'audi'", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value'audi'", "value")
    self.assertEqual(attributes, (True, None))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("\"class'myclass' "
                                                                                       "class='myclass'", "class")
    self.assertEqual(attributes, (True, None))

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_quotes(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"audi\"", "value")
    self.assertEqual(attributes, (False, ["audi"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value='audi'", "value")
    self.assertEqual(attributes, (False, ["audi"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"audi'A3\"", "value")
    self.assertEqual(attributes, (False, ["audi'A3"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value=\"audi'A3'\"", "value")
    self.assertEqual(attributes, (False, ["audi'A3'"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value='audi\"A3'", "value")
    self.assertEqual(attributes, (False, ["audi\"A3"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("value='\"audi\"A3\"'", "value")
    self.assertEqual(attributes, (False, ["\"audi\"A3\""]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("class='myClass'title='titled title=\"title\"'",
                                                                     "title")
    self.assertEqual(attributes, (False, ["titled", "title=\"title\""]))

  def test_extractDifferentValuesFromHtmlAttributesByKey_oneValueFound(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("rel=\"shortcut icon\" "
                                                             "href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, (False, ["img/favicon.ico"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("rel=\"shortcut icon\" "
                                                   "href=\"img/favicon.ico\" id='X' type=\"image/x-icon\"", "id")
    self.assertEqual(attributes, (False, ["X"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("rel=\"shortcut icon\" "
                                            "xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, (False, ["img/favicon.ico"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("rel=\"shortcut icon\" "
                          "no-href=\"false\" xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, (False, ["img/favicon.ico"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("rel=\"shortcut icon\" "
        "hrefhref=\"image\" no-href=\"false\" xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, (False, ["img/favicon.ico"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey(
                                                                            "nonce=\"lix9PsSUHJxW7ghXrU5s0A\"", "nonce")
    self.assertEqual(attributes, (False, ["lix9PsSUHJxW7ghXrU5s0A"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "disable-upgrade")
    self.assertEqual(attributes, (False, ["true"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("rel=\"preload\" href="
                                "\"https://r3---sn-8vq54voxgv-vu26.googlevideo.com/generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))

  def test_extractDifferentValuesFromHtmlAttributesByKey_whitespaces(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey(
                                                         "rel =\"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey(
                                                          "rel = \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey(
                                                          "rel= \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey(
                                    "rel \n\r\t\t\t = \n\r\t\t\t \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey(
                                "\n\trel \n\r\t\t\t = \n\r\t\t\t \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey(
          "\n\trel \n\r\t\t\t = \n\r\t\t\t \"\r\n\t\t preload \t\t\t\n\t  \" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, (False, ["preload"]))

  def test_extractDifferentValuesFromHtmlAttributesByKey_multipleValuesFound(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("action=\".\" "
                                "method=\"get\" class=\"add_search_params pure-form\" style=\"display:inline-block\"",
                                "class")
    self.assertEqual(attributes, (False, ["add_search_params", "pure-form"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("action=\".\" "
                                "method=\"get\" class=\"add_search_params pure-form hide-xs hide-sm hide-md\" "
                                "style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, (False, ["add_search_params", "pure-form", "hide-xs", "hide-sm", "hide-md"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("action=\".\" "
                                "method=\"get\" class\n=\n\"add_search_params\tpure-form\r\nhide-xs     hide-sm"
                                "\t\t\t\n\r   \n\r    hide-md\n\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, (False, ["add_search_params", "pure-form", "hide-xs", "hide-sm", "hide-md"]))

  def test_extractDifferentValuesFromHtmlAttributesByKey_multipleDeclarations(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("action=\".\" "
              "method=\"get\" class=\"add_search_params cl2 cl3\" class=\"pure-form\" style=\"display:inline-block\"",
              "class")
    self.assertEqual(attributes, (False, ["add_search_params", "cl2", "cl3"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("action=\".\" "
              "method=\"get\" class=\"add_search_params\" class=\"pure-form cl2 cl3\" style=\"display:inline-block\"",
              "class")
    self.assertEqual(attributes, (False, ["add_search_params"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("action=\".\" class "
                              "method=\"get\" class=\"pure-form cl2 cl3\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, (False, None))

  def test_extractDifferentValuesFromHtmlAttributesByKey_valueRepeats(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("action=\".\" "
                                            "method=\"get\" class=\"cl1 cl1\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, (False, ["cl1"]))
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesByKey("action=\".\" "
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
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("title=\"class='myClass'\"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "title")
    self.assertEqual(attributeValue, "class='myClass'")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 22)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("title=\"class='myClass'\""
                                                                                         "selected", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "title")
    self.assertEqual(attributeValue, "class='myClass'")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 22)

    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("title=\"===>A'B'C<===\""
                                                                                         "selected", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "title")
    self.assertEqual(attributeValue, "===>A'B'C<===")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 20)

  def test_getNextHtmlAttribute_indexPointsWithinAttributeName(self):
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected", 2)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected='False'", 3)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, "False")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 15)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected='False'", 7)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, "False")
    self.assertEqual(startIdx, 0)
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
    corrupt, attributes = attr.getListOfHtmlAttributeNames("title=\"class='myClass'\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["title"])
    corrupt, attributes = attr.getListOfHtmlAttributeNames("title=\"<=== A'B'C ===>\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["title"])

  def test_getListOfHtmlAttributeNames_moreAttributes(self):
    corrupt, attributes = attr.getListOfHtmlAttributeNames("title=\"class='myClass'\"id='myId'\t\nselected")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["title", "id", "selected"])
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

  def helper_getCurrentValue_checkIfCorrupt(self, attributesString, startIdx):
    corrupt, found, firstQuoteIdx, secondQuoteIdx = attr.getCurrentValue(attributesString, startIdx)
    self.assertTrue(corrupt)
    self.assertFalse(found)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def helper_getCurrentValue_checkIfNotFound(self, attributesString, startIdx):
    corrupt, found, firstQuoteIdx, secondQuoteIdx = attr.getCurrentValue(attributesString, startIdx)
    self.assertFalse(corrupt)
    self.assertFalse(found)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def helper_getCurrentValue_checkIfFound(self, attributesString, startIdx, startsAt, endsAt):
    corrupt, found, firstQuoteIdx, secondQuoteIdx = attr.getCurrentValue(attributesString, startIdx)
    self.assertFalse(corrupt)
    self.assertTrue(found)
    self.assertEqual(firstQuoteIdx, startsAt)
    self.assertEqual(secondQuoteIdx, endsAt)

  def test_getCurrentValue_nonSense(self):
    with self.assertRaises(Exception):
      attr.getCurrentValue(None, None)
    with self.assertRaises(Exception):
      attr.getCurrentValue(False, 0)
    with self.assertRaises(Exception):
      attr.getCurrentValue("= 'value'", True)
    with self.assertRaises(Exception):
      attr.getCurrentValue("= 'value'", 56)
    with self.assertRaises(Exception):
      attr.getCurrentValue("= 'value'", -1)

  def test_getCurrentValue_emptyString(self):
    with self.assertRaises(Exception):
      attr.getCurrentValue("", 0)

  def test_getCurrentValue_spaces(self):
    self.helper_getCurrentValue_checkIfNotFound(" ", 0)
    self.helper_getCurrentValue_checkIfNotFound("\n", 0)
    self.helper_getCurrentValue_checkIfNotFound(" \t\t\n", 0)
    self.helper_getCurrentValue_checkIfNotFound(" \t\t \n ", 0)

  def test_getCurrentValue_corrupt(self):
    self.helper_getCurrentValue_checkIfCorrupt("=", 0)
    self.helper_getCurrentValue_checkIfCorrupt("==", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=========", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= ", 0)
    self.helper_getCurrentValue_checkIfCorrupt("='\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=\"'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= \t \n", 0)
    self.helper_getCurrentValue_checkIfCorrupt("'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("''", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\"\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("'value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\"value\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=value", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= value", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= \n\t value", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= value ", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\t\t\n = \n\tvalue\n\n\n", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=2", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= 2", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=value\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=\"value", 0)
    self.helper_getCurrentValue_checkIfCorrupt("='value", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=\"value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("='value\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= \"value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= 'value\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=   \"  value  '  ", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=  '  value  \"  ", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\t\t=   \"  value  '  ", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\n\n\n=  '  value  \"  ", 0)

  def test_getCurrentValue_corrupt_noAttributeNameBeforeEqual(self):
    self.helper_getCurrentValue_checkIfCorrupt("=\"\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("='value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= 'value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt(" = 'value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("='value' ", 8)
    self.helper_getCurrentValue_checkIfCorrupt("= \"\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt(" = \"\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\t=\t\"\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=\t\t\t\"\"", 0)

  def test_getCurrentValue_notFound(self):
    self.helper_getCurrentValue_checkIfNotFound("X", 0)
    self.helper_getCurrentValue_checkIfNotFound("attrName", 0)
    self.helper_getCurrentValue_checkIfNotFound("multiple attribute names", 0)
    self.helper_getCurrentValue_checkIfNotFound("attrName\t", 0)
    self.helper_getCurrentValue_checkIfNotFound("\tattrName", 0)
    self.helper_getCurrentValue_checkIfNotFound("attrName\t\n", 0)
    self.helper_getCurrentValue_checkIfNotFound("\n\tattrName", 0)
    self.helper_getCurrentValue_checkIfNotFound("   \t attrName  \t\t  \t", 0)
    self.helper_getCurrentValue_checkIfNotFound("selected class='myClass'", 0)
    self.helper_getCurrentValue_checkIfNotFound("selected class='myClass'", 3)
    self.helper_getCurrentValue_checkIfNotFound("\t\tselected\n\nclass='myClass'", 0)

  def test_getCurrentValue_emptyValue(self):
    self.helper_getCurrentValue_checkIfFound("a=\"\"", 0, startsAt=2, endsAt=3)
    self.helper_getCurrentValue_checkIfFound("a=\"\"", 1, startsAt=2, endsAt=3)
    self.helper_getCurrentValue_checkIfFound("abc = \"\" ", 0, startsAt=6, endsAt=7)
    self.helper_getCurrentValue_checkIfFound("abc = \"\" ", 1, startsAt=6, endsAt=7)
    self.helper_getCurrentValue_checkIfFound("abc = \"\" ", 2, startsAt=6, endsAt=7)
    self.helper_getCurrentValue_checkIfFound("abc = \"\" ", 3, startsAt=6, endsAt=7)
    self.helper_getCurrentValue_checkIfFound("abc = \"\" ", 4, startsAt=6, endsAt=7)
    self.helper_getCurrentValue_checkIfFound("abc = \"\" ", 5, startsAt=6, endsAt=7)
    self.helper_getCurrentValue_checkIfFound("abc = \t\"\" ", 6, startsAt=7, endsAt=8)
    self.helper_getCurrentValue_checkIfFound("abc = \t\r\n\"\" ", 7, startsAt=9, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("abc = \t\r\n\"\" ", 8, startsAt=9, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("aabd\n\n\n=\t\t\t\"\" ", 4, startsAt=11, endsAt=12)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t'' ", 0, startsAt=8, endsAt=9)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t'' ", 1, startsAt=8, endsAt=9)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t''\n\t", 1, startsAt=8, endsAt=9)

  def test_getCurrentValue_whiteSpaceValue(self):
    self.helper_getCurrentValue_checkIfFound("a=\" \"", 0, startsAt=2, endsAt=4)
    self.helper_getCurrentValue_checkIfFound("a=\" \"", 1, startsAt=2, endsAt=4)
    self.helper_getCurrentValue_checkIfFound("abc=\" \"", 0, startsAt=4, endsAt=6)
    self.helper_getCurrentValue_checkIfFound("a = \"\n\" ", 1, startsAt=4, endsAt=6)
    self.helper_getCurrentValue_checkIfFound("a = \"\n\" ", 2, startsAt=4, endsAt=6)
    self.helper_getCurrentValue_checkIfFound("abc = \"\n\" ", 0, startsAt=6, endsAt=8)
    self.helper_getCurrentValue_checkIfFound("abc = \"\n\" ", 1, startsAt=6, endsAt=8)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t\"\t\n\t\" ", 0, startsAt=8, endsAt=12)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t\"\t\n\t\" ", 1, startsAt=8, endsAt=12)
    self.helper_getCurrentValue_checkIfFound("Q\n\n\n=\t\t\t'\t\n\t' ", 0, startsAt=8, endsAt=12)
    self.helper_getCurrentValue_checkIfFound("Q\n\n\n=\t\t\t'\t\n\t' ", 1, startsAt=8, endsAt=12)

  def test_getCurrentValue_nonEmptyValue(self):
    self.helper_getCurrentValue_checkIfFound("x=\"value\"", 1, startsAt=2, endsAt=8)
    self.helper_getCurrentValue_checkIfFound("a = \"value\" ", 0, startsAt=4, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("a = \"value\" ", 1, startsAt=4, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("a = \"value\" ", 2, startsAt=4, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t\"value\" ", 1, startsAt=8, endsAt=14)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t'value' ", 1, startsAt=8, endsAt=14)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t'\t value\n\n' ", 1, startsAt=8, endsAt=18)
    self.helper_getCurrentValue_checkIfFound("class=\"class='myClass'\"", 5, startsAt=6, endsAt=22)
    self.helper_getCurrentValue_checkIfFound("id=\"class='myClass'\"selected", 2, startsAt=3, endsAt=19)

  def test_getCurrentValue_indexPointsToValue(self):
    self.helper_getCurrentValue_checkIfFound("x = 'value'", 4, startsAt=4, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("x = 'value'", 7, startsAt=4, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("x = 'value'", 9, startsAt=4, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("x = 'value'", 10, startsAt=4, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 4, startsAt=4, endsAt=25)
    self.helper_getCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 5, startsAt=4, endsAt=25)
    self.helper_getCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 6, startsAt=4, endsAt=25)
    self.helper_getCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 7, startsAt=4, endsAt=25)
    self.helper_getCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 8, startsAt=4, endsAt=25)
    self.helper_getCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 9, startsAt=4, endsAt=25)
    self.helper_getCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 10, startsAt=4, endsAt=25)
    self.helper_getCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 11, startsAt=4, endsAt=25)

  def helper_getCurrentOrNextName_checkIfNotFound(self, string, startIdx):
    corrupt, found, attributeName, firstCharIdx, lastCharIdx = attr.getCurrentOrNextName(string, startIdx)
    self.assertFalse(corrupt)
    self.assertFalse(found)
    self.assertIsNone(attributeName, -1)
    self.assertEqual(firstCharIdx, -1)
    self.assertEqual(lastCharIdx, -1)

  def helper_getCurrentOrNextName_checkIfFound(self, string, startIdx, startsAt, endsAt):
    corrupt, found, attributeName, firstCharIdx, lastCharIdx = attr.getCurrentOrNextName(string, startIdx)
    self.assertFalse(corrupt)
    self.assertTrue(found)
    self.assertEqual(firstCharIdx, startsAt)
    self.assertEqual(lastCharIdx, endsAt)
    self.assertEqual(attributeName, string[startsAt:endsAt + 1])

  def helper_getCurrentOrNextName_checkIfCorrupt(self, string, startIdx):
    corrupt, found, attributeName, firstCharIdx, lastCharIdx = attr.getCurrentOrNextName(string, startIdx)
    self.assertTrue(corrupt)
    self.assertFalse(found)
    self.assertIsNone(attributeName, -1)
    self.assertEqual(firstCharIdx, -1)
    self.assertEqual(lastCharIdx, -1)

  def test_getCurrentOrNextName_nonSense(self):
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName(None, None)
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName(False, 0)
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName("= 'value'", True)
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName("= 'value'", 56)
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName("= 'value'", -1)

  def test_getCurrentOrNextName_emptyString(self):
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName("", 0)
    self.helper_getCurrentOrNextName_checkIfNotFound("a='value' ", 9)

  def test_getCurrentOrNextName_spaces(self):
    self.helper_getCurrentOrNextName_checkIfNotFound(" ", 0)
    self.helper_getCurrentOrNextName_checkIfNotFound("\n", 0)
    self.helper_getCurrentOrNextName_checkIfNotFound(" \t\t\n", 0)
    self.helper_getCurrentOrNextName_checkIfNotFound(" \t\t\n", 1)
    self.helper_getCurrentOrNextName_checkIfNotFound(" \t\t\n", 2)
    self.helper_getCurrentOrNextName_checkIfNotFound(" \t\r\n", 0)
    self.helper_getCurrentOrNextName_checkIfNotFound(" \t\t \n ", 3)

  def test_getCurrentOrNextName_corrupt(self):
    self.helper_getCurrentOrNextName_checkIfCorrupt("=", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("= ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" =", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("\t\t=\n\n", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("'", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("''''''''", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("' ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" '", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" ' ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("\t\t'\n\n", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("\"", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("\" ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" \"", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" \" ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("\t\t\"\n\n", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("='value'", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("=value'", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("class'myClass'", 0)

  def test_getCurrentOrNextName_notFound(self):
    self.helper_getCurrentOrNextName_checkIfNotFound("class ", 5)
    self.helper_getCurrentOrNextName_checkIfNotFound("class \r\n", 5)
    self.helper_getCurrentOrNextName_checkIfNotFound("class \r\n", 6)
    self.helper_getCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' ", 21)
    self.helper_getCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' \t\t", 21)
    self.helper_getCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' \t\t", 22)

  def test_getCurrentOrNextName_indexPointsAtTheFirstNameCharIdx(self):
    self.helper_getCurrentOrNextName_checkIfFound("X", 0, startsAt=0, endsAt=0)
    self.helper_getCurrentOrNextName_checkIfFound("X=''", 0, startsAt=0, endsAt=0)
    self.helper_getCurrentOrNextName_checkIfFound("\t\tX\t\t", 0, startsAt=2, endsAt=2)
    self.helper_getCurrentOrNextName_checkIfFound("\t\tX\t\tY Z", 0, startsAt=2, endsAt=2)
    self.helper_getCurrentOrNextName_checkIfFound("selected", 0, startsAt=0, endsAt=7)
    self.helper_getCurrentOrNextName_checkIfFound("\t\tselected\n\n", 0, startsAt=2, endsAt=9)
    self.helper_getCurrentOrNextName_checkIfFound(" class='my-Class' \t selected", 0, startsAt=1, endsAt=5)
    self.helper_getCurrentOrNextName_checkIfFound("\n\nclass\t\t=\t\n'   my-Class' \r\n\t selected", 0,
                                                  startsAt=2, endsAt=6)
    self.helper_getCurrentOrNextName_checkIfFound("multiple words in this string", 0, startsAt=0, endsAt=7)
    self.helper_getCurrentOrNextName_checkIfFound("title=\"class='myClass'==\"", 0, startsAt=0, endsAt=4)

  def test_getCurrentOrNextName_indexPointsWithinName(self):
    self.helper_getCurrentOrNextName_checkIfFound("selected", 3, startsAt=0, endsAt=7)
    self.helper_getCurrentOrNextName_checkIfFound("multiple words in this string", 3, startsAt=0, endsAt=7)
    self.helper_getCurrentOrNextName_checkIfFound("multiple words in this string", 13, startsAt=9, endsAt=13)

  def test_getCurrentOrNextName_indexPointsAroundValue(self):
    self.helper_getCurrentOrNextName_checkIfFound("class='myClass'", 5, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class='myClass'", 6, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class='myClass'", 7, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class='myClass'", 9, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class='myClass'", 14, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 5, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 6, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 7, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 8, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 5, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 6, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 7, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 8, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 9, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 10, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 11, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("a=''", 1, startsAt=0, endsAt=0)
    self.helper_getCurrentOrNextName_checkIfFound("a = ''", 1, startsAt=0, endsAt=0)
    self.helper_getCurrentOrNextName_checkIfFound("a = ''", 2, startsAt=0, endsAt=0)
    self.helper_getCurrentOrNextName_checkIfFound("a = ''", 3, startsAt=0, endsAt=0)
    self.helper_getCurrentOrNextName_checkIfFound("title=\"class='myClass'\"", 12, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("title=\"'class'='myClass'\"", 14, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("title=\"'class' = 'myClass'\"", 15, startsAt=0, endsAt=4)

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

  def test_getHtmlAttributes_space(self):
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

  def test_isThereNonDelimiterCharBeforeIdx_nonSense(self):
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx("text", -1)
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx("text", 123)
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx("text", 4)
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx(12, 123)
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx(False, 0)
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx(None, None)

  def test_isThereNonDelimiterCharBeforeIdx_emptyString(self):
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx("", 0)

  def test_isThereNonDelimiterCharBeforeIdx_thereIsNot(self):
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("text", 0))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("this is an another string", 0))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number=2", 7))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number='2'", 8))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number='2'", 7))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number = 2", 9))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number = '2'", 10))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number '2'", 8))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx('number="2"', 8))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx('number="2"', 7))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx('number = "2"', 10))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx('number "2"', 8))

  def test_isThereNonDelimiterCharBeforeIdx_thereIs(self):
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("text", 3))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("this is an another string", 11))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("this is an another string", 15))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("one-two-three", 4))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("one-two-three", 1))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("value = 'one'", 6))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("value= 'one'", 5))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("value='one'", 5))

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

  def helper_indexIsWithinHtmlAttributeValue_checkIfNotValue(self, string, index):
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
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue(" ", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("a", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("ab", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("ab", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 3)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 2)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 4)

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
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 6)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 14)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class = 'myClass'", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class = 'myClass'", 7)

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

  def helper_getFirstHtmlDelimiter_exceptionRaised(self, string, inclusiveStartIdx, exclusiveEndIdx):
    with self.assertRaises(Exception):
      attr.getFirstHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)

  def helper_getFirstHtmlDelimiter_notFound(self, string, inclusiveStartIdx, exclusiveEndIdx):
    found, idx = attr.getFirstHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertFalse(found)
    self.assertEqual(idx, -1)

  def helper_getFirstHtmlDelimiter_found(self, string, inclusiveStartIdx, exclusiveEndIdx, foundAt):
    found, idx = attr.getFirstHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertTrue(found)
    self.assertEqual(idx, foundAt)

  def test_getFirstHtmlDelimiter_nonSense(self):
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, 345)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, 7)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, None)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, True)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, [])
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, "")
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", -1, 2)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", -1, 45)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 5, 3)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", None, 3)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", True, 3)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", True, False)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", None, None)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", "", "")
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 2, 2)
    self.helper_getFirstHtmlDelimiter_exceptionRaised(None, 0, 3)
    self.helper_getFirstHtmlDelimiter_exceptionRaised([], 0, 3)
    self.helper_getFirstHtmlDelimiter_exceptionRaised(None, None, None)
    self.helper_getFirstHtmlDelimiter_exceptionRaised(0, 0, 0)

  def test_getFirstHtmlDelimiter_emptyString(self):
    self.helper_getFirstHtmlDelimiter_exceptionRaised("", 0, 0)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("", 0, 1)

  def test_getFirstHtmlDelimiter_notFound(self):
    self.helper_getFirstHtmlDelimiter_notFound("Q", 0, 1)
    self.helper_getFirstHtmlDelimiter_notFound("one-two-three", 0, 13)
    self.helper_getFirstHtmlDelimiter_notFound("=Hello=", 1, 6)
    self.helper_getFirstHtmlDelimiter_notFound("\n'greeting'\t= \"Hello\" ", 2, 10)
    self.helper_getFirstHtmlDelimiter_notFound("\n'greeting'\t= \"Hello\" ", 15, 20)

  def test_getFirstHtmlDelimiter_found(self):
    self.helper_getFirstHtmlDelimiter_found(" ", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("\t", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("\n", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("'", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("\"", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("=", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("'=='", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("key = 'value'", 0, 11, foundAt = 3)
    self.helper_getFirstHtmlDelimiter_found("key='value'", 0, 11, foundAt = 3)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 0, 17, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 0, 4, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 1, 17, foundAt = 1)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 1, 3, foundAt = 1)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 2, 17, foundAt = 5)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 5, 17, foundAt = 5)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 6, 17, foundAt = 6)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 8, 17, foundAt = 8)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 11, 17, foundAt = 16)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 3, 11, foundAt = 5)

  def helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised(self, string, inclusiveStartIdx, exclusiveEndIdx):
    with self.assertRaises(Exception):
      attr.getFirstHtmlDelimiterThenSkipWhiteSpaces(string, inclusiveStartIdx, exclusiveEndIdx)

  def helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound(self, string, inclusiveStartIdx, exclusiveEndIdx):
    found, idx = attr.getFirstHtmlDelimiterThenSkipWhiteSpaces(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertFalse(found)
    self.assertEqual(idx, -1)

  def helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound(self, string, inclusiveStartIdx,
                                                                   exclusiveEndIdx, foundAt):
    found, idx = attr.getFirstHtmlDelimiterThenSkipWhiteSpaces(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertTrue(found)
    self.assertEqual(idx, foundAt)

  def test_getFirstHtmlDelimiterThenSkipWhiteSpaces_nonSense(self):
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, 345)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, 7)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, None)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, True)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, [])
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, "")
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", -1, 2)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", -1, 45)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 5, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", None, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", True, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", True, False)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", None, None)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", "", "")
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 2, 2)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised(None, 0, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised([], 0, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised(None, None, None)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised(0, 0, 0)

  def test_getFirstHtmlDelimiterThenSkipWhiteSpaces_emptyString(self):
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("", 0, 1)

  def test_getFirstHtmlDelimiterThenSkipWhiteSpaces_notFound(self):
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("Q", 0, 1)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound(" ", 0, 1)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("string", 0, 6)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two three", 0, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two three", 4, 7)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two three", 8, 13)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("<one-two-three>", 0, 15)

  def test_getFirstHtmlDelimiterThenSkipWhiteSpaces_LastIdxIsWhiteSpace(self):
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two three", 0, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one\ttwo three", 0, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two three", 4, 8)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two\nthree", 4, 8)

  def test_getFirstHtmlDelimiterThenSkipWhiteSpaces_found(self):
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("=", 0, 1, foundAt=0)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("'", 0, 1, foundAt=0)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("\"", 0, 1, foundAt=0)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("one two three", 0, 13, foundAt=4)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("one two three", 4, 13, foundAt=8)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("one two=three", 4, 13, foundAt=7)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("key\r\n\t = value", 1, 14, foundAt=7)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("key\r\n\t 'value'", 1, 14, foundAt=7)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("key\r\n\t \"value\"", 1, 14, foundAt=7)

  def helper_getLastValueByFoundEquals_exceptionRaised(self, string, inclStartIdx, inclEndIdx):
    with self.assertRaises(Exception):
      attr.getLastValueByFoundEquals(string, inclStartIdx, inclEndIdx)

  def helper_getLastValueByFoundEquals_checkIfCorrupt(self, string, inclStartIdx, inclEndIdx):
    corrupt, found, equalIdx, openingQuoteIdx, ClosingQuoteIdx \
                                                      = attr.getLastValueByFoundEquals(string, inclStartIdx, inclEndIdx)
    self.assertTrue(corrupt)
    self.assertFalse(found)
    self.assertEqual(equalIdx, -1)
    self.assertEqual(openingQuoteIdx, -1)
    self.assertEqual(ClosingQuoteIdx, -1)

  def helper_getLastValueByFoundEquals_checkIfNotFound(self, string, inclStartIdx, inclEndIdx):
    corrupt, found, equalIdx, openingQuoteIdx, ClosingQuoteIdx \
                                                      = attr.getLastValueByFoundEquals(string, inclStartIdx, inclEndIdx)
    self.assertFalse(corrupt)
    self.assertFalse(found)
    self.assertEqual(equalIdx, -1)
    self.assertEqual(openingQuoteIdx, -1)
    self.assertEqual(ClosingQuoteIdx, -1)

  def helper_getLastValueByFoundEquals_checkIfFound(self, string, inclStartIdx, inclEndIdx, equalIdxAt,
                                                    openingQuoteIdxAt, closingQuoteIdxAt):
    corrupt, found, equalIdx, openingQuoteIdx, closingQuoteIdx \
                                                      = attr.getLastValueByFoundEquals(string, inclStartIdx, inclEndIdx)
    self.assertFalse(corrupt)
    self.assertTrue(found)
    self.assertEqual(equalIdx, equalIdxAt)
    self.assertEqual(openingQuoteIdx, openingQuoteIdxAt)
    self.assertEqual(closingQuoteIdx, closingQuoteIdxAt)

  def test_getLastValueByFoundEquals_nonSense(self):
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", -1, 2)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 6, 8)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 36, 75)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 5, 2)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 1, None)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 1, "")
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 1, True)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", None, 4)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", "", 4)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", True, 4)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", True, True)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", None, None)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", "string", "string")
    self.helper_getLastValueByFoundEquals_exceptionRaised([], 0, 0)
    self.helper_getLastValueByFoundEquals_exceptionRaised(True, True, True)
    self.helper_getLastValueByFoundEquals_exceptionRaised(None, None, None)

  def test_getLastValueByFoundEquals_emptyString(self):
    self.helper_getLastValueByFoundEquals_exceptionRaised("", 0, 0)

  def test_getLastValueByFoundEquals_corrupt_onlyEqual(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("=", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= ", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = ", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = ", 0, 2)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = ", 1, 2)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = ", 1, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = ", 1, 2)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = = ", 1, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" == ", 1, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 0, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 0, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 1, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 1, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 2, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 2, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n = \t \t", 0, 7)

  def test_getLastValueByFoundEquals_corrupt_onlyQuotes(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\"", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("''", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("''", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("''", 1, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt('""', 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt('""', 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" ' ", 0, 2)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\n\t'\t\n", 0, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("''''", 0, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'\"'\"", 0, 3)

  def test_getLastValueByFoundEquals_corrupt_noQuotes(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("=2", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("=2", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= 2", 0, 2)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("=\t\t2", 0, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2", 0, 5)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2", 1, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2", 1, 5)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a = 4", 0, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number = one two", 0, 14)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number = one two", 0, 10)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number = one two", 0, 7)

  def test_getLastValueByFoundEquals_corrupt_noEqual(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'myClass'", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'myClass' id = 'myId'", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number 'one' two", 0, 9)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'number one two'", 0, 9)

  def test_getLastValueByFoundEquals_corrupt_mixedQuotes(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t '2", 0, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t \"2", 1, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2'", 0, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2'", 1, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2\"", 0, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2\"", 1, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t '2\"", 0, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t \"2'", 0, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a\t=\t\t \"0'", 0, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a = \"0'", 0, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a = \"0''", 0, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a = \"0'''", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a = \"0' selected", 0, 15)

  def test_getLastValueByFoundEquals_corrupt_noAttributeName(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= ''", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= ''", 0, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = 'myClass'", 0, 11)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t\r\n = 'myClass'", 0, 14)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t\r\n = 'myClass'", 3, 14)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = '' selected", 0, 10)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= '' selected", 0, 9)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("='' selected", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("=''selected", 0, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= 'a=\"2\"'", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= 'a=\"2\"'", 3, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= ' back a=\"2\" href'", 9, 17)

  def test_getLastValueByFoundEquals_corrupt_other(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'number one two", 0, 9)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'number one two\"", 0, 9)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'number one two\"", 1, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\"number one two\"", 0, 9)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number one two'", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number one two\"", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number 'one two", 0, 14)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number \"one two", 0, 14)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("b = 'a=\"2\"", 3, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("b = 'a=\"2\"", 1, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("b = ' checked a=\"2\" selected", 14, 25)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("b = ' checked a=\"2\" selected", 24, 25)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("class='myClass' b = ' checked a=\"2\" selected", 16, 42)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("class='myClass' b = ' checked a=\"2\" selected", 24, 42)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("class='myClass' b = ' checked a=\"2\" selected", 36, 43)

# TODO review tests below
  def test_getLastValueByFoundEquals_valueNotFound(self):
    self.helper_getLastValueByFoundEquals_checkIfNotFound(" ", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\t", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\r", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\n", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\r\n", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("Q", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("ab", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("abc", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("abc", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("abc", 0, 2)
    self.helper_getLastValueByFoundEquals_checkIfNotFound(" a ", 0, 2)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("a\t=\t\t \"0'", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\none\ttwo three\r\n", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\none\ttwo three\r\n", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\none\ttwo three\r\n", 0, 6)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\none\ttwo three\r\n", 0, 15)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("selected number='two'", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("selected number='two'", 0, 4)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("a ='2'", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("b = 'a=\"2\"'", 3, 7)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'checked a=\"2\"' selected'", 21, 42)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'checked a=\"2\"' selected'", 32, 42)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'checked a=\"2\"' selected'", 36, 42)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 36, 38)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 28, 38)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 32, 38)

  def test_getLastValueByFoundEquals_valueFound(self):
    self.helper_getLastValueByFoundEquals_checkIfFound("a\t=\t\t '0'", 0, 2, equalIdxAt=2,
                                                       openingQuoteIdxAt=6, closingQuoteIdxAt=8)
    self.helper_getLastValueByFoundEquals_checkIfFound("a = '' selected", 0, 11, equalIdxAt=2,
                                                       openingQuoteIdxAt=4, closingQuoteIdxAt=5)
    self.helper_getLastValueByFoundEquals_checkIfFound("a = '' selected", 0, 7, equalIdxAt=2,
                                                       openingQuoteIdxAt=4, closingQuoteIdxAt=5)
    self.helper_getLastValueByFoundEquals_checkIfFound("a = '' selected", 0, 14, equalIdxAt=2,
                                                       openingQuoteIdxAt=4, closingQuoteIdxAt=5)
    self.helper_getLastValueByFoundEquals_checkIfFound("a = \"\" selected", 0, 14, equalIdxAt=2,
                                                       openingQuoteIdxAt=4, closingQuoteIdxAt=5)
    self.helper_getLastValueByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 0, 42,
                                                       equalIdxAt=24, openingQuoteIdxAt=29, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 0, 33,
                                                       equalIdxAt=24, openingQuoteIdxAt=29, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 0, 30,
                                                       equalIdxAt=24, openingQuoteIdxAt=29, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 0, 29,
                                                       equalIdxAt=24, openingQuoteIdxAt=29, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n \" myClass \" selected", 0, 29,
                                                       equalIdxAt=24, openingQuoteIdxAt=29, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("title = \"class='myClass'\"", 0, 18,
                                                       equalIdxAt=6, openingQuoteIdxAt=8, closingQuoteIdxAt=24)
    self.helper_getLastValueByFoundEquals_checkIfFound("title = \"=class='myClass'=\"", 0, 19,
                                                       equalIdxAt=6, openingQuoteIdxAt=8, closingQuoteIdxAt=26)
    self.helper_getLastValueByFoundEquals_checkIfFound("title\t=\n\"===class='myClass'===\"", 0, 21,
                                                       equalIdxAt=6, openingQuoteIdxAt=8, closingQuoteIdxAt=30)
    self.helper_getLastValueByFoundEquals_checkIfFound("id='myId'title\t=\n\"===class='myClass'===\"", 0, 30,
                                                       equalIdxAt=15, openingQuoteIdxAt=17, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("id='myId' title\t=\n\"===class='myClass'===\"", 0, 31,
                                                       equalIdxAt=16, openingQuoteIdxAt=18, closingQuoteIdxAt=40)

    self.helper_getLastValueByFoundEquals_checkIfFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel' checked", 8, 38,
                                                       equalIdxAt=18, openingQuoteIdxAt=20, closingQuoteIdxAt=38)

  def helper_getLastHtmlDelimiter_exceptionRaised(self, string, inclusiveStartIdx, exclusiveEndIdx):
    with self.assertRaises(Exception):
      attr.getLastHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)

  def helper_getLastHtmlDelimiter_notFound(self, string, inclusiveStartIdx, exclusiveEndIdx):
    found, idx = attr.getLastHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertFalse(found)
    self.assertEqual(idx, -1)

  def helper_getLastHtmlDelimiter_found(self, string, inclusiveStartIdx, exclusiveEndIdx, foundAt):
    found, idx = attr.getLastHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertTrue(found)
    self.assertEqual(idx, foundAt)

  def test_getLastHtmlDelimiter_nonSense(self):
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, 345)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, 7)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, None)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, True)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, [])
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, "")
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", -1, 2)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", -1, 45)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 5, 3)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", None, 3)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", True, 3)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", True, False)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", None, None)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", "", "")
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 2, 2)
    self.helper_getLastHtmlDelimiter_exceptionRaised(None, 0, 3)
    self.helper_getLastHtmlDelimiter_exceptionRaised([], 0, 3)
    self.helper_getLastHtmlDelimiter_exceptionRaised(None, None, None)
    self.helper_getLastHtmlDelimiter_exceptionRaised(0, 0, 0)

  def test_getLastHtmlDelimiter_emptyString(self):
    self.helper_getLastHtmlDelimiter_exceptionRaised("", 0, 0)
    self.helper_getLastHtmlDelimiter_exceptionRaised("", 0, 1)

  def test_getLastHtmlDelimiter_notFound(self):
    self.helper_getLastHtmlDelimiter_notFound("Q", 0, 1)
    self.helper_getLastHtmlDelimiter_notFound("one-two-three", 0, 13)
    self.helper_getLastHtmlDelimiter_notFound("=Hello=", 1, 6)
    self.helper_getLastHtmlDelimiter_notFound("\n'greeting'\t= \"Hello\" ", 2, 10)
    self.helper_getLastHtmlDelimiter_notFound("\n'greeting'\t= \"Hello\" ", 15, 20)

  def test_getLastHtmlDelimiter_found(self):
    self.helper_getLastHtmlDelimiter_found(" ", 0, 1, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("\t", 0, 1, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("\n", 0, 1, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("'", 0, 1, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("\"", 0, 1, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("=", 0, 1, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("'=='", 0, 1, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("key = 'value'", 0, 11, foundAt = 6)
    self.helper_getLastHtmlDelimiter_found("key='value'", 0, 11, foundAt = 10)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 0, 17, foundAt = 16)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 0, 4, foundAt = 1)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 1, 16, foundAt = 10)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 1, 3, foundAt = 1)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 6, 17, foundAt = 16)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 11, 17, foundAt = 16)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 3, 9, foundAt = 8)

  def helper_getLastIdxFromCurrentNameBeforeEqual_checkException(self, string, equalIdx):
    with self.assertRaises(Exception):
      attr.getLastIdxFromCurrentNameBeforeEqual(string, equalIdx)

  def helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt(self, string, equalIdx):
    corrupt, idx = attr.getLastIdxFromCurrentNameBeforeEqual(string, equalIdx)
    self.assertTrue(corrupt)
    self.assertEqual(idx, -1)

  def helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound(self, string, equalIdx, foundAt):
    corrupt, idx = attr.getLastIdxFromCurrentNameBeforeEqual(string, equalIdx)
    self.assertFalse(corrupt)
    self.assertEqual(idx, foundAt)

  def test_getLastIdxFromCurrentNameBeforeEqual_nonSense(self):
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkException("string", -1)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkException("string", 51)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkException("string", 6)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkException("string", False)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkException("string", None)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkException(0, 0)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkException([], 0)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkException(None, None)

  def test_getLastIdxFromCurrentNameBeforeEqual_emptyString(self):
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkException("", 0)

  def test_getLastIdxFromCurrentNameBeforeEqual_corrupt(self):
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("X", 0)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("abc", 1)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("=", 0)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("==", 1)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("'=", 1)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt(" =", 1)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("\t=", 1)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("\n=", 1)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("\r=", 1)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("\"=", 1)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("= =", 2)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("' =", 2)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("'key' =", 6)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("   =", 3)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfCorrupt("\r\n\t =", 4)

  def test_getLastIdxFromCurrentNameBeforeEqual_found(self):
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound("a=", 1, foundAt=0)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound("a =", 2, foundAt=0)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound("a\t=", 2, foundAt=0)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound("a\r=", 2, foundAt=0)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound("a\n=", 2, foundAt=0)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound("a\t\r\n   =", 7, foundAt=0)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound("ab=", 2, foundAt=1)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound("abdsfsdasfgg=", 12, foundAt=11)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound("class='myClass' id = 'myId' href='link.com'", 19,
                                                                  foundAt=17)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound("class='myClass' id = 'myId' href='link.com'", 5,
                                                                  foundAt=4)
    self.helper_getLastIdxFromCurrentNameBeforeEqual_checkIfFound("class='myClass' id = 'myId'href\t\t\t=\n'link.com'",
                                                                  34, foundAt=30)

  def helper_getAllValuesByFoundEquals_exceptionRaised(self, attributeString, inclusiveStartIdx, inclusiveEndIdx):
    with self.assertRaises(Exception):
      attr.getAllValuesByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)

  def helper_getAllValuesByFoundEquals_corrupt(self, attributeString, inclusiveStartIdx, inclusiveEndIdx):
    corrupt, values = attr.getAllValuesByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)
    self.assertTrue(corrupt)
    self.assertEqual(values, [])

  def helper_getAllValuesByFoundEquals_notFound(self, attributeString, inclusiveStartIdx, inclusiveEndIdx):
    corrupt, values = attr.getAllValuesByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)
    self.assertFalse(corrupt)
    self.assertEqual(values, [])

  def helper_getAllValuesByFoundEquals_checkIfFound(self, attributeString, inclusiveStartIdx, inclusiveEndIdx,
                                                    foundValues):
    corrupt, values = attr.getAllValuesByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)
    self.assertFalse(corrupt)
    self.assertEqual(values, foundValues)

  def test_getAllValuesByFoundEquals_nonSense(self):
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", -1, 2)
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", 6, 8)
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", 36, 75)
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", 5, 2)
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", 1, None)
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", 1, "")
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", 1, True)
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", None, 4)
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", "", 4)
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", True, 4)
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", True, True)
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", None, None)
    self.helper_getAllValuesByFoundEquals_exceptionRaised("string", "string", "string")
    self.helper_getAllValuesByFoundEquals_exceptionRaised([], 0, 0)
    self.helper_getAllValuesByFoundEquals_exceptionRaised(True, True, True)
    self.helper_getAllValuesByFoundEquals_exceptionRaised(None, None, None)

  def test_getAllValuesByFoundEquals_emptyString(self):
    self.helper_getAllValuesByFoundEquals_exceptionRaised("", 0, 0)

  def test_getAllValuesByFoundEquals_corrupt_onlyEqual(self):
    self.helper_getAllValuesByFoundEquals_corrupt("=", 0, 0)
    self.helper_getAllValuesByFoundEquals_corrupt("= ", 0, 1)
    self.helper_getAllValuesByFoundEquals_corrupt(" = ", 0, 1)
    self.helper_getAllValuesByFoundEquals_corrupt(" = ", 0, 2)
    self.helper_getAllValuesByFoundEquals_corrupt(" = ", 1, 2)
    self.helper_getAllValuesByFoundEquals_corrupt(" = ", 1, 1)
    self.helper_getAllValuesByFoundEquals_corrupt(" = ", 1, 2)
    self.helper_getAllValuesByFoundEquals_corrupt(" = = ", 1, 4)
    self.helper_getAllValuesByFoundEquals_corrupt(" == ", 1, 3)
    self.helper_getAllValuesByFoundEquals_corrupt("\r\n=\t\t", 0, 4)
    self.helper_getAllValuesByFoundEquals_corrupt("\r\n=\t\t", 0, 3)
    self.helper_getAllValuesByFoundEquals_corrupt("\r\n=\t\t", 1, 3)
    self.helper_getAllValuesByFoundEquals_corrupt("\r\n=\t\t", 1, 4)
    self.helper_getAllValuesByFoundEquals_corrupt("\r\n=\t\t", 2, 4)
    self.helper_getAllValuesByFoundEquals_corrupt("\r\n=\t\t", 2, 3)
    self.helper_getAllValuesByFoundEquals_corrupt("\r\n = \t \t", 0, 7)

  def test_getAllValuesByFoundEquals_corrupt_onlyQuotes(self):
    self.helper_getAllValuesByFoundEquals_corrupt("'", 0, 0)
    self.helper_getAllValuesByFoundEquals_corrupt("\"", 0, 0)
    self.helper_getAllValuesByFoundEquals_corrupt("''", 0, 0)
    self.helper_getAllValuesByFoundEquals_corrupt("''", 0, 1)
    self.helper_getAllValuesByFoundEquals_corrupt("''", 1, 1)
    self.helper_getAllValuesByFoundEquals_corrupt('""', 0, 0)
    self.helper_getAllValuesByFoundEquals_corrupt('""', 0, 1)
    self.helper_getAllValuesByFoundEquals_corrupt(" ' ", 0, 2)
    self.helper_getAllValuesByFoundEquals_corrupt("\n\t'\t\n", 0, 4)
    self.helper_getAllValuesByFoundEquals_corrupt("''''", 0, 3)
    self.helper_getAllValuesByFoundEquals_corrupt("'\"'\"", 0, 3)

  def test_getAllValuesByFoundEquals_corrupt_noQuotes(self):
    self.helper_getAllValuesByFoundEquals_corrupt("=2", 0, 0)
    self.helper_getAllValuesByFoundEquals_corrupt("=2", 0, 1)
    self.helper_getAllValuesByFoundEquals_corrupt("= 2", 0, 2)
    self.helper_getAllValuesByFoundEquals_corrupt("=\t\t2", 0, 3)
    self.helper_getAllValuesByFoundEquals_corrupt("\t=\t\t 2", 0, 5)
    self.helper_getAllValuesByFoundEquals_corrupt("\t=\t\t 2", 1, 4)
    self.helper_getAllValuesByFoundEquals_corrupt("\t=\t\t 2", 1, 5)
    self.helper_getAllValuesByFoundEquals_corrupt("a = 4", 0, 4)
    self.helper_getAllValuesByFoundEquals_corrupt("number = one two", 0, 14)
    self.helper_getAllValuesByFoundEquals_corrupt("number = one two", 0, 10)
    self.helper_getAllValuesByFoundEquals_corrupt("number = one two", 0, 7)

  def test_getAllValuesByFoundEquals_corrupt_noEqual(self):
    self.helper_getAllValuesByFoundEquals_corrupt("'myClass'", 0, 8)
    self.helper_getAllValuesByFoundEquals_corrupt("'myClass' id = 'myId'", 0, 8)
    self.helper_getAllValuesByFoundEquals_corrupt("number 'one' two", 0, 9)
    self.helper_getAllValuesByFoundEquals_corrupt("'number one two'", 0, 9)
    self.helper_getAllValuesByFoundEquals_corrupt("'number one two", 0, 9)
    self.helper_getAllValuesByFoundEquals_corrupt("'number one two\"", 0, 9)
    self.helper_getAllValuesByFoundEquals_corrupt("'number one two\"", 1, 4)
    self.helper_getAllValuesByFoundEquals_corrupt("\"number one two\"", 0, 9)
    self.helper_getAllValuesByFoundEquals_corrupt("number one two'", 0, 8)
    self.helper_getAllValuesByFoundEquals_corrupt("number one two\"", 0, 8)
    self.helper_getAllValuesByFoundEquals_corrupt("number 'one two", 0, 14)
    self.helper_getAllValuesByFoundEquals_corrupt("number ' one two", 0, 14)
    self.helper_getAllValuesByFoundEquals_corrupt("number \"one two", 0, 14)

  def test_getAllValuesByFoundEquals_corrupt_mixedQuotes(self):
    self.helper_getAllValuesByFoundEquals_corrupt("\t=\t\t '2", 0, 6)
    self.helper_getAllValuesByFoundEquals_corrupt("\t=\t\t \"2", 1, 6)
    self.helper_getAllValuesByFoundEquals_corrupt("\t=\t\t 2'", 0, 6)
    self.helper_getAllValuesByFoundEquals_corrupt("\t=\t\t 2'", 1, 6)
    self.helper_getAllValuesByFoundEquals_corrupt("\t=\t\t 2\"", 0, 6)
    self.helper_getAllValuesByFoundEquals_corrupt("\t=\t\t 2\"", 1, 6)
    self.helper_getAllValuesByFoundEquals_corrupt("\t=\t\t '2\"", 0, 7)
    self.helper_getAllValuesByFoundEquals_corrupt("\t=\t\t \"2'", 0, 7)
    self.helper_getAllValuesByFoundEquals_corrupt("a\t=\t\t \"0'", 0, 7)
    self.helper_getAllValuesByFoundEquals_corrupt("a = \"0'", 0, 6)
    self.helper_getAllValuesByFoundEquals_corrupt("a = \"0''", 0, 7)
    self.helper_getAllValuesByFoundEquals_corrupt("a = \"0'''", 0, 8)
    self.helper_getAllValuesByFoundEquals_corrupt("a = \"0' selected", 0, 15)

  def test_getAllValuesByFoundEquals_corrupt_noAttributeName(self):
    self.helper_getAllValuesByFoundEquals_corrupt("= ''", 0, 0)
    self.helper_getAllValuesByFoundEquals_corrupt("= ''", 0, 3)
    self.helper_getAllValuesByFoundEquals_corrupt(" = 'myClass'", 0, 11)
    self.helper_getAllValuesByFoundEquals_corrupt("\t\r\n = 'myClass'", 0, 14)
    self.helper_getAllValuesByFoundEquals_corrupt("\t\r\n = 'myClass'", 3, 14)
    self.helper_getAllValuesByFoundEquals_corrupt(" = '' selected", 0, 10)
    self.helper_getAllValuesByFoundEquals_corrupt("= '' selected", 0, 9)
    self.helper_getAllValuesByFoundEquals_corrupt("='' selected", 0, 8)
    self.helper_getAllValuesByFoundEquals_corrupt("=''selected", 0, 7)
    self.helper_getAllValuesByFoundEquals_corrupt("= 'a=\"2\"'", 0, 8)
    self.helper_getAllValuesByFoundEquals_corrupt("= 'a=\"2\"'", 3, 8)
    self.helper_getAllValuesByFoundEquals_corrupt("= ' back a=\"2\" href'", 9, 17)

  def test_getAllValuesByFoundEquals_corrupt_other(self):
    self.helper_getAllValuesByFoundEquals_corrupt("b = 'a=\"2\"", 3, 7)
    self.helper_getAllValuesByFoundEquals_corrupt("b = 'a=\"2\"", 1, 3)
    self.helper_getAllValuesByFoundEquals_corrupt("b = ' checked a=\"2\" selected", 14, 25)
    self.helper_getAllValuesByFoundEquals_corrupt("b = ' checked a=\"2\" selected", 24, 25)
    self.helper_getAllValuesByFoundEquals_corrupt("class='myClass' b = ' checked a=\"2\" selected", 16, 42)
    self.helper_getAllValuesByFoundEquals_corrupt("class='myClass' b = ' checked a=\"2\" selected", 24, 42)
    self.helper_getAllValuesByFoundEquals_corrupt("class='myClass' b = ' checked a=\"2\" selected", 36, 43)

  def test_getAllValuesByFoundEquals_valueNotFound(self):
    self.helper_getAllValuesByFoundEquals_notFound(" ", 0, 0)
    self.helper_getAllValuesByFoundEquals_notFound("\t", 0, 0)
    self.helper_getAllValuesByFoundEquals_notFound("\r", 0, 0)
    self.helper_getAllValuesByFoundEquals_notFound("\n", 0, 0)
    self.helper_getAllValuesByFoundEquals_notFound("\r\n", 0, 0)
    self.helper_getAllValuesByFoundEquals_notFound("Q", 0, 0)
    self.helper_getAllValuesByFoundEquals_notFound("ab", 0, 1)
    self.helper_getAllValuesByFoundEquals_notFound("abc", 0, 0)
    self.helper_getAllValuesByFoundEquals_notFound("abc", 0, 1)
    self.helper_getAllValuesByFoundEquals_notFound("abc", 0, 2)
    self.helper_getAllValuesByFoundEquals_notFound(" a ", 0, 2)
    self.helper_getAllValuesByFoundEquals_notFound("a\t=\t\t \"0'", 0, 0)
    self.helper_getAllValuesByFoundEquals_notFound("\none\ttwo three\r\n", 0, 0)
    self.helper_getAllValuesByFoundEquals_notFound("\none\ttwo three\r\n", 0, 1)
    self.helper_getAllValuesByFoundEquals_notFound("\none\ttwo three\r\n", 0, 6)
    self.helper_getAllValuesByFoundEquals_notFound("\none\ttwo three\r\n", 0, 15)
    self.helper_getAllValuesByFoundEquals_notFound("selected number='two'", 0, 0)
    self.helper_getAllValuesByFoundEquals_notFound("selected number='two'", 0, 4)
    self.helper_getAllValuesByFoundEquals_notFound("a ='2'", 0, 0)
    self.helper_getAllValuesByFoundEquals_notFound("b = 'a=\"2\"'", 3, 7)
    self.helper_getAllValuesByFoundEquals_notFound("class='myClass' b = 'checked a=\"2\"' selected'", 21, 42)
    self.helper_getAllValuesByFoundEquals_notFound("class='myClass' b = 'checked a=\"2\"' selected'", 32, 42)
    self.helper_getAllValuesByFoundEquals_notFound("class='myClass' b = 'checked a=\"2\"' selected'", 36, 42)
    self.helper_getAllValuesByFoundEquals_notFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 36, 38)
    self.helper_getAllValuesByFoundEquals_notFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 28, 38)
    self.helper_getAllValuesByFoundEquals_notFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 32, 38)

  # review these tests
  def test_getAllValuesByFoundEquals_valueFound(self):
    self.helper_getAllValuesByFoundEquals_checkIfFound("a\t=\t\t '0'", 0, 2, foundValues = [(2, 6, 8)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("a = '' selected", 0, 11, foundValues = [(2, 4, 5)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("a = '' selected", 0, 7, foundValues = [(2, 4, 5)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("a = '' selected", 0, 14, foundValues = [(2, 4, 5)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("a = \"\" selected", 0, 14, foundValues = [(2, 4, 5)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 0, 42,
                                                       foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 2, 33,
                                                       foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 4, 26,
                                                       foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 6, 24,
                                                       foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 7, 24,
                                                       foundValues=[(24, 29, 39)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 2, 23,
                                                       foundValues=[(6, 8, 16)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n \" myClass \" selected", 0, 29,
                                                       foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("title = \"class='myClass'\"", 0, 18, foundValues=[(6, 8, 24)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("title = \"=class='myClass'=\"", 0, 19, foundValues=[(6, 8, 26)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("title\t=\n\"===class='myClass'===\"", 0, 21,
                                                       foundValues=[(6, 8, 30)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("id='myId'title\t=\n\"===class='myClass'===\"", 0, 30,
                                                       foundValues=[(2, 3, 8), (15, 17, 39)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("id='myId' title\t=\n\"===class='myClass'===\"", 0, 31,
                                                       foundValues=[(2, 3, 8), (16, 18, 40)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel' checked", 18, 38,
                                                       foundValues=[(18, 20, 38)])
    self.helper_getAllValuesByFoundEquals_checkIfFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel' checked", 5, 18,
                                                       foundValues=[(5, 6, 14), (18, 20, 38)])
