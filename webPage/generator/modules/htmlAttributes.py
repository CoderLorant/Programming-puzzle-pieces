from modules import checks
from modules import stringUtil

# TODO test key = ' = "myClass" '  <-- corrupt by key because it contains html delimiters
# TODO this function looks ugly, clean code it
def getAttributeIdx(htmlAttributes, key):
  """Only the first declaration is taken (if there are multiple) as stated by the standard:
https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html
\n Return values:
* corrupt: True | False *(does not validate the attached attribute value and the rest of string out of key context)*
* firstIdx: **-1** if attribute not found or corrupt """
  checks.checkIfString(htmlAttributes, 0, 3000)
  checks.checkIfString(key, 0, 60)
  notFoundResult = (False, -1)
  corruptResult = (True, -1)
  if not htmlAttributes or not key:
    return notFoundResult
  firstIdx = htmlAttributes.find(key, 0, len(htmlAttributes))
  while firstIdx != -1:
    # continue if not a full word
    if not stringIsHtmlDelimited(htmlAttributes, firstIdx, len(key)):
      firstIdx = htmlAttributes.find(key, firstIdx + 1, len(htmlAttributes))
      continue

    # Check if seems to be part of attribute value from right
    firstEqualIdxAfterKey = htmlAttributes.find("=", firstIdx + len(key))
    referenceIdxFromRight = firstEqualIdxAfterKey
    if referenceIdxFromRight == -1:
      referenceIdxFromRight = len(htmlAttributes) - 1
    nrOfSimpleQuotesAfter = htmlAttributes.count("'", firstIdx + len(key), referenceIdxFromRight + 1)
    nrOfDoubleQuotesAfter = htmlAttributes.count('"', firstIdx + len(key), referenceIdxFromRight + 1)
    seemsToBeAttributeValueFromRight = nrOfSimpleQuotesAfter + nrOfDoubleQuotesAfter > 0

    # Check if seems to be part of attribute value from left
    referenceIdxFromLeft = htmlAttributes.rfind("=", 0, firstIdx)
    if referenceIdxFromLeft == 0:
      return corruptResult
    equalFoundBefore = referenceIdxFromLeft > 0
    if referenceIdxFromLeft == -1:
      referenceIdxFromLeft = 0
    # check if there is attribute name before equal
    if equalFoundBefore and not thereIsAttributeNameBeforeIdx(htmlAttributes, referenceIdxFromLeft):
      return corruptResult
    # another check
    nrOfMainQuotesBefore = 0
    nrOfMainQuotesAfter = 0
    endingQuoteIdx = -1
    if equalFoundBefore:
      mainQuoteCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlAttributes, referenceIdxFromLeft + 1,
                                                                            len(htmlAttributes))
      firstNonSpaceCharAfterEqual = htmlAttributes[mainQuoteCharIdx]
      if firstNonSpaceCharAfterEqual != "'" and firstNonSpaceCharAfterEqual != '"':
        return corruptResult
      nrOfMainQuotesBefore = htmlAttributes.count(firstNonSpaceCharAfterEqual, referenceIdxFromLeft, firstIdx)
      nrOfMainQuotesAfter = htmlAttributes.count(firstNonSpaceCharAfterEqual, firstIdx + len(key),
                                                 referenceIdxFromRight + 1)
      endingQuoteIdx = htmlAttributes.find(firstNonSpaceCharAfterEqual, mainQuoteCharIdx + 1, referenceIdxFromRight + 1)
    nrOfSimpleQuotesBefore = htmlAttributes.count("'", referenceIdxFromLeft, firstIdx)
    nrOfDoubleQuotesBefore = htmlAttributes.count('"', referenceIdxFromLeft, firstIdx)
    seemsToBeAttributeValueFromLeft = nrOfMainQuotesBefore == 1

    if not equalFoundBefore and (nrOfSimpleQuotesBefore + nrOfDoubleQuotesBefore > 0):
      return corruptResult

    if not seemsToBeAttributeValueFromLeft and (seemsToBeAttributeValueFromRight
                                                or nrOfMainQuotesBefore > 2):
      return corruptResult

    if seemsToBeAttributeValueFromLeft and (not equalFoundBefore
                                            or nrOfMainQuotesAfter != 1
                                            or nextNonWhiteSpaceCharIsHtmlDelimiter(htmlAttributes, endingQuoteIdx)):
      return corruptResult

    if seemsToBeAttributeValueFromLeft:
      firstIdx = htmlAttributes.find(key, firstIdx + 1, len(htmlAttributes))
      continue

    return False, firstIdx
  return notFoundResult

# TODO test 'class="note"id="red"' below functions, it is valid HTML even if there is no space in ' note"id '

def extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(htmlAttributes, key):
  """Only the first declaration is taken (if there are multiple) as stated by the standard:
https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html
\n Return values:
* <corrupt>: True | False
* <values>: **None** if corrupt or attribute name not found, empty list if the value is empty or whitspace"""
  checks.checkIfString(htmlAttributes, 0, 800)
  checks.checkIfString(key, 1, 30)
  result = []
  notFoundResult = (False, None)
  corruptResult = (True, None)
  corrupt, firstIdx = getAttributeIdx(htmlAttributes, key)
  if corrupt:
    return corruptResult
  if firstIdx == -1:
    return notFoundResult
  corrupt, attributeName, attributeValue, startIdx, endIdx = getNextHtmlAttribute(htmlAttributes, firstIdx)
  if corrupt:
    return corruptResult
  if attributeValue is None:
    return notFoundResult
  # TODO getSplitUniqueElements(Char::WHITESPACE)
  values = attributeValue.split()
  for value in values:
    if value not in result:
      result.append(value)
  return False, result

def getListOfHtmlAttributeNames(attributesString):
  """ Only the first declaration is taken per each attribute name (if there are multiple) as stated by the standard:
https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html\n
\n Return values:
* <corrupt>: True | False
* <attributeNames>: empty list if corrupt or attribute not found"""
  checks.checkIfString(attributesString, 0, 1000)
  result = []
  corruptResult = (True, [])
  idx = 0
  while idx < len(attributesString):
    corrupt, attributeName, attributeValue, startIdx, endIdx = getNextHtmlAttribute(attributesString, idx)
    if corrupt:
      return corruptResult
    if attributeName is None:
      nextNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, idx, len(attributesString))
      if nextNonSpaceCharIdx != -1:
        return False, []
      break
    if attributeName not in result:
      result.append(attributeName)
    idx = endIdx + 1
    continue
  return False, result


def getNextHtmlAttribute(attributesString, startIdx):
  """ Raises exception if <startIdx> is not valid. This means that <attributesString> cannot be an empty string as
there is no first index. \n
Only the first attribute is taken and validated \n
\n Return values:
* <corrupt>: True | False
* <attributeName>, <attributeValue> : **None** if no attribute was found or <attributesString> is corrupt
* <attrStartIdx>, <attrEndIdx> : inclusive, **-1** if no attribute was found or attributesString is corrupt"""
  noAttributeResult = (False, None, None, -1, -1)
  corruptResult = (True, None, None, -1, -1)
  corrupt, attributeName, firstCharIdx, lastCharIdx = getNextHtmlAttributeName(attributesString, startIdx)
  if corrupt:
    return corruptResult
  if firstCharIdx == -1:
    return noAttributeResult
  if lastCharIdx == len(attributesString) - 1:
    return False, attributeName, None, firstCharIdx, lastCharIdx
  corrupt, firstQuoteIdx, secondQuoteIdx = getNextHtmlAttributeValueIfExists(attributesString, lastCharIdx + 1)
  if corrupt:
    return corruptResult
  if firstQuoteIdx == -1:
    return False, attributeName, None, firstCharIdx, lastCharIdx
  return False, attributeName, attributesString[firstQuoteIdx + 1:secondQuoteIdx], firstCharIdx, secondQuoteIdx

# TODO see if you can make it prettier
# TODO use corruptResult as for the other functions
def getNextHtmlAttributeValueIfExists(attributesString, startIdx):
  """Raises error at empty string because <startIdx> cannot be set properly\n
You DO NOT want to call this before checking for an attribute name first, e.g. calling *getNextHtmlAttributeName()*\n
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

# TODO see if you can make it look prettier
def getNextHtmlAttributeName(attributesString, startIdx):
  """Raises error at empty string because <startIdx> cannot be set properly\n
Return values:\n
* corrupt : True | False *(does not validate the attribute value)*
* attributeName: **None** if corrupt or there is no attribute
* firstCharIdx, lastCharIdx: **-1** if corrupt or there is no attribute """
  checks.checkIfString(attributesString, 0, 1000)
  checks.checkIntIsBetween(startIdx, 0, len(attributesString) - 1)
  corruptResult = (True, None, -1, -1)
  firstNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, startIdx, len(attributesString))
  if firstNonSpaceCharIdx == -1:
    return False, None, -1, -1
  firstNonSpaceChar = attributesString[firstNonSpaceCharIdx]
  if firstNonSpaceChar == "=" or firstNonSpaceChar == "'" or firstNonSpaceChar == "\"":
    return corruptResult
  currentIdx = firstNonSpaceCharIdx
  attributeName = ""
  while currentIdx < len(attributesString):
    currentChar = attributesString[currentIdx]
    if currentChar.isspace() or currentChar == "=":
      return False, attributeName, firstNonSpaceCharIdx, currentIdx-1
    if currentChar == "'" or currentChar == '"':
      return corruptResult
    attributeName += currentChar
    currentIdx += 1
  return False, attributeName, firstNonSpaceCharIdx, len(attributesString) - 1

def thereIsAttributeNameBeforeIdx(htmString, idx):
  checks.checkIfString(htmString, 0, 4000)
  checks.checkIntIsBetween(idx, 0, len(htmString) - 1)
  if idx == 0:
    return False
  idx -= 1
  while idx >= 0:
    currentChar = htmString[idx]
    if currentChar == "'" or currentChar == '"' or currentChar == "=":
      return False
    if not currentChar.isspace():
      return True
    idx -= 1
  return False

def nextNonWhiteSpaceCharIsHtmlDelimiter(htmlString, index):
  """Raises exception for empty string because the index cannot be set properly."""
  checks.checkIfString(htmlString, 0, 4000)
  checks.checkIntIsBetween(index, 0, len(htmlString) - 1)
  if index == len(htmlString) - 1:
    return False
  idx = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlString, index + 1, len(htmlString))
  return idx != -1 and charIsHtmlDelimiter(htmlString[idx])

def stringIsHtmlDelimited(htmlString, firstCharIdx, lengthOfString):
  """Intended for full word check in case of HTML attribute names and values. \n
Raises exception for empty string because the index cannot be set properly."""
  return htmlDelimitedFromLeft(htmlString, firstCharIdx) and \
         htmlDelimitedFromRight(htmlString, firstCharIdx + lengthOfString - 1)

def htmlDelimitedFromLeft(htmlString, index):
  """Intended for full word check in case of HTML attribute names and values. \n
Raises exception for empty string because the index cannot be set properly."""
  previousChar = stringUtil.getPreviousChar(htmlString, index)
  return previousChar is None or charIsHtmlDelimiter(previousChar)

def htmlDelimitedFromRight(htmlString, index):
  """Intended for full word check in case of HTML attribute names and values. \n
Raises exception for empty string because the index cannot be set properly."""
  nextChar = stringUtil.getNextChar(htmlString, index)
  return nextChar is None or charIsHtmlDelimiter(nextChar)

def charIsHtmlDelimiter(ch):
  """HTML attribute delimiters: Whitespace, equal, single-quote, double-quote"""
  checks.checkIfChar(ch)
  return ch.isspace() or ch == "=" or ch == '"' or ch == "'"
