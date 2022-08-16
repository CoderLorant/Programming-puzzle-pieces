from modules import checks
from modules import stringUtil

def getAttributeIdx(htmlAttributes, key):
  """Returns -1 if attribute not found and for empty string \n
   Does not check for corrupt <htmlAttributes>, e.g.: \"key "invalid, no '=' before"\"\n
   Only the first declaration is taken (if there are multiple) as stated by the standard:
   https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html
   """
  checks.checkIfString(htmlAttributes, 0, 3000)
  checks.checkIfString(key, 0, 60)
  if not htmlAttributes or not key:
    return -1
  # TODO delimitedFind(string, key,  before=[whitespace, "<"], after=[whitespace, "="], 0, len(string))
  firstIdx = stringUtil.beforeWhitespaceDelimitedFind(htmlAttributes, key, 0, len(htmlAttributes))
  while firstIdx != -1 and firstIdx + len(key) < len(htmlAttributes) \
          and not htmlAttributes[firstIdx + len(key)].isspace() and htmlAttributes[firstIdx + len(key)] != "=":
    firstIdx = stringUtil.beforeWhitespaceDelimitedFind(htmlAttributes, key, firstIdx + 1, len(htmlAttributes))
  return firstIdx

def extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(htmlAttributes, key):
  """Does not raise error if htmlAttributes is corrupt, it returns **None**\n
  Returns **None** if there is no attribute value, and an **empty list** if the value is empty or has only whitespaces\n
  Only the first declaration is taken (if there are multiple) as stated by the standard:
  https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html"""
  checks.checkIfString(htmlAttributes, 0, 800)
  checks.checkIfString(key, 1, 30)
  result = []
  firstIdx = getAttributeIdx(htmlAttributes, key)
  if firstIdx == -1:
    return None
  attributeName, attributeValue, startIdx, endIdx = getNextHtmlAttribute(htmlAttributes, firstIdx)
  if attributeValue is None:
    return None
  # TODO getSplitUniqueElements(Char::WHITESPACE)
  values = attributeValue.split()
  for value in values:
    if value not in result:
      result.append(value)
  return result

# TODO this function is too long, make it shorter
def getNextHtmlAttribute(attributesString, startIdx):
  """ Raises exception if <startIdx> is not valid. This means that <attributesString> cannot be an empty string as
there is no first index. \n
<attributesString> can be considered corrupt only within the context of the first attribute \n
<startIdx>-1 is not accessed for full word check
\n Return values:
* <attributeName>, <attributeValue> : **None** if no attribute was found or <attributesString> is corrupt
* <attrStartIdx>, <attrEndIdx> : inclusive, **-1** if no attribute was found or attributesString is corrupt"""
  checks.checkIfString(attributesString, 0, 1000)
  checks.checkIntIsBetween(startIdx, 0, len(attributesString) - 1)
  attrStartIdx = -1
  currentIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, startIdx, len(attributesString))
  if currentIdx == -1:
    return None, None, -1, -1
  currentAttribute = ""
  lastEndIdx = -1
  while currentIdx < len(attributesString):
    currentChar = attributesString[currentIdx]
    # Equal
    if currentChar == "=":
      if not currentAttribute:
        return None, None, -1, -1
      corrupt, firstQuoteIdx, secondQuoteIdx = getNextHtmlAttributeValueIfExists(attributesString, currentIdx)
      if corrupt:
        return None, None, -1, -1
      return currentAttribute, attributesString[firstQuoteIdx + 1:secondQuoteIdx], attrStartIdx, secondQuoteIdx
    # Apostrophe
    elif currentChar == "'" or currentChar == "\"":
      return None, None, -1, -1
    # First space
    elif currentChar.isspace() and not attributesString[currentIdx - 1].isspace():
      lastEndIdx = currentIdx - 1
    # Not equal, not apostrophe and not space
    elif not currentChar.isspace():
      if lastEndIdx > 0:
        return currentAttribute, None, attrStartIdx, lastEndIdx
      if not currentAttribute:
        attrStartIdx = currentIdx
      currentAttribute += currentChar
    currentIdx += 1
  if lastEndIdx > 0:
    return currentAttribute, None, attrStartIdx, lastEndIdx
  return currentAttribute, None, attrStartIdx, len(attributesString) - 1

def getListOfHtmlAttributeNames(attributesString):
  """Returns empty list if attribute not found, for empty string and if **<attributesString>** is corrupt \n
     Only the first declaration is taken (if there are multiple) as stated by the standard:
     https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html"""
  checks.checkIfString(attributesString, 0, 1000)
  result = []
  idx = 0
  while idx < len(attributesString):
    attributeName, attributeValue, startIdx, endIdx = getNextHtmlAttribute(attributesString, idx)
    if attributeName is None:
      nextNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, idx, len(attributesString))
      if nextNonSpaceCharIdx != -1:
        return []
      break
    if attributeName not in result:
      result.append(attributeName)
    idx = endIdx + 1
    continue
  return result

# isInvalid, openingApostropheIdx, closingApostropheCharIdx
def getNextHtmlAttributeValueIfExists(attributesString, startIdx):
  """Raises error at empty string because <startIdx> cannot be set properly\n
You DO NOT want to call this before checking for an attribute name first\n
Return values:\n
* corrupt : True | False
* firstQuoteIdx, secondQuoteIdx: **-1** if corrupt or there is no attribute value """
  checks.checkIfString(attributesString, 0, 1000)
  checks.checkIntIsBetween(startIdx, 0, len(attributesString) - 1)
  firstNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, startIdx, len(attributesString))
  if firstNonSpaceCharIdx == -1:
    return False, -1, -1
  firstNonSpaceChar = attributesString[firstNonSpaceCharIdx]
  if firstNonSpaceChar != "=":
    isCorrupt = firstNonSpaceChar == "'" or firstNonSpaceChar == "\""
    return isCorrupt, -1, -1
  if firstNonSpaceCharIdx == len(attributesString) - 1:
    return True, -1, -1
  nonSpaceCharIdxAfterEq = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, firstNonSpaceCharIdx + 1,
                                                                   len(attributesString))
  quoteChar = attributesString[nonSpaceCharIdxAfterEq]
  if quoteChar != "'" and quoteChar != "\"":
    return True, -1, -1
  secondQuoteIdx = attributesString.find(quoteChar, nonSpaceCharIdxAfterEq + 1)
  if secondQuoteIdx == -1:
    return True, -1, -1
  return False, nonSpaceCharIdxAfterEq, secondQuoteIdx
