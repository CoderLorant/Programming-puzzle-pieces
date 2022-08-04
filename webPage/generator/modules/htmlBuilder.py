from modules import checks
from modules import filerw
from modules import stringUtil

# TODO create a new file for HTML attributes

# <html><head> [headWriter] </head><body> [bodyWriter] </body></html>
def buildIndexHtmlFile(indexHtmlHeadWriterFunction, indexHtmlBodyWriterFunction, settings):
  htmlFile = settings.htmlOutputFile
  settings.indentDepth = 2
  htmlFile.write("<html>\n")
  htmlFile.write("\t<head>\n")
  indexHtmlHeadWriterFunction(settings)
  htmlFile.write("\t</head>\n")
  htmlFile.write("\t<body>\n")
  indexHtmlBodyWriterFunction(settings)
  htmlFile.write("\t</body>\n")
  htmlFile.write("</html>\n")

# file1 += file2
def includeFileThenAppendNewLine(htmlFile, includeFilePath, indentDepth):
  lines = filerw.getLinesByPathWithEndingNewLine(includeFilePath)
  tabs = getEscapedTabs(indentDepth)
  filerw.writeStringsPrefixedToFileThenAppendNewLine(htmlFile, tabs, lines)

# file1 += <htmlTag> file2 </htmlTag>
def includeFileSurroundedByHtmlTagThenAppendNewLine(htmlFile, includeFilePath, htmlTag, htmlTagOption, indentDepth):
  tabs = getEscapedTabs(indentDepth)
  htmlFile.write(tabs + getOpenedHtmlTag(htmlTag, htmlTagOption) + "\n")
  fileLines = filerw.getLinesByPath(includeFilePath)
  filerw.writeLinesPrefixedToFile(htmlFile, tabs + "\t", fileLines)
  htmlFile.write(tabs + getClosedHtmlTag(htmlTag) + "\n")

# <script src=".js" />   ->  file
def addJsScriptSrcToHtmlOutputFile(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  lines = getJsScriptSrc(indentDepth, url, integrity, crossorigin, referrerpolicy)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, lines)

# <link href=".css" />   ->  file
def addCssLinkHrefToHtmlOutputFile(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  lines = getCssLinkHref(indentDepth, url, integrity, crossorigin, referrerpolicy)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, lines)

# <br\> <br\> <br\>  ->  file
def addHtmlNewLineToFile(htmlFile, indentDepth, nrOfNewLines=1):
  newLinesString = getHtmlNewLines(indentDepth, nrOfNewLines)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, [newLinesString])

# <title> Page title </title>  ->  file
def addTitleToHtmlOutputFile(htmlFile, titleString, indentDepth):
  htmlTitle = getHtmlTitle(titleString, indentDepth)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, [htmlTitle])

# <link rel="icon" href="favicon.png">  ->  file
def addFaviconToHtmlOutputFile(htmlFile, faviconPath, indentDepth):
  htmlFavicon = getHtmlFavicon(faviconPath, indentDepth)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, [htmlFavicon])

# <meta name="viewport" content="width=device-width, initial-scale=1.0"/>  ->  file
def addMetaScreenOptimizedForMobileToHtmlOutputFile(htmlFile, indentDepth):
  metaTag = getMetaScreenOptimizedForMobile(indentDepth)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, [metaTag])

# <script src=".js" />
def getJsScriptSrc(indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  # "a.io/s.js" -> length 9
  checks.checkIfString(url, 9, 500)
  checks.checkIfAllNoneOrString([integrity, crossorigin, referrerpolicy], 5, 200)
  tabs = getEscapedTabs(indentDepth)
  result = [tabs + "<script src=\"" + url + "\""]
  if integrity is None:
    result[0] += "></script>"
    return result
  tabs += "\t"
  # integrity deserves its own line because usually it is a long string
  result.append(tabs + "integrity=\"" + integrity + "\"")
  result.append(tabs + "crossorigin=\"" + crossorigin + "\" referrerpolicy=\"" + referrerpolicy + "\"></script>")
  return result

# <link href=".css" />
def getCssLinkHref(indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  # "a.io/s.css" -> length 10
  checks.checkIfString(url, 10, 500)
  checks.checkIfAllNoneOrString([integrity, crossorigin, referrerpolicy], 5, 200)
  tabs = getEscapedTabs(indentDepth)
  result = [tabs + "<link href=\"" + url + "\""]
  tabs += "\t"
  if integrity is None:
    if len(url) > 95:
      result.append(tabs + "rel=\"stylesheet\" />")
    else:
      result[0] += " rel=\"stylesheet\" />"
    return result
  # integrity deserves its own line because usually it is a long string
  result.append(tabs + "integrity=\"" + integrity + "\"")
  result.append(tabs + "rel=\"stylesheet\" crossorigin=\"" + crossorigin
                + "\" referrerpolicy=\"" + referrerpolicy + "\" />")
  return result

# <link rel="icon" href="favicon.png">
def getHtmlFavicon(faviconPath, indentDepth):
  checks.checkIntIsBetween(indentDepth, 1, 150)
  checks.checkIfString(faviconPath, 3, 300)
  result = getEscapedTabs(indentDepth)
  result += "<link rel=\"icon\" href=\"" + faviconPath + "\">"
  return result

# <title> page title </title>
def getHtmlTitle(titleString, indentDepth):
  checks.checkIntIsBetween(indentDepth, 1, 150)
  checks.checkIfString(titleString, 2, 300)
  result = getEscapedTabs(indentDepth)
  result += "<title>" + titleString + "</title>"
  return result

# <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
def getMetaScreenOptimizedForMobile(indentDepth):
  tabs = getEscapedTabs(indentDepth)
  metaTag = tabs + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>"
  return metaTag

# <br\> <br\> <br\>
def getHtmlNewLines(indentDepth, nrOfNewLines=1):
  checks.checkIntIsBetween(nrOfNewLines, 1, 50)
  result = getEscapedTabs(indentDepth)
  for i in range(nrOfNewLines):
    result += "<br\\>"
    if i != nrOfNewLines - 1:
      result += " "
  return result

def filterJqueryLikeHtmlSelector(specialHtmlTag):
  classes, ids = stringUtil.doubleSplit(specialHtmlTag, ".", "#")
  checks.checkIfNonEmptyList(classes)
  htmlTag = classes[0]
  classes = classes[1:]
  checks.checkIfStringIsAlphaNumerical(htmlTag)
  checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(classes)
  checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(ids)
  idString = stringUtil.stringListToString(ids, prefix="", suffix="", delimiter=" ")
  classString = stringUtil.stringListToString(classes, prefix="", suffix="", delimiter=" ")
  htmlOptions = ""
  if idString:
    htmlOptions += "id=\"" + idString + "\""
    if classString:
      htmlOptions += " "
  if classString:
    htmlOptions += "class=\"" + classString + "\""
  return htmlTag, htmlOptions

# TODO this function is too long, make it shorter
def extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(htmlAttributes, key):
  """Does not raise error if htmlAttributes is corrupt, it returns an empty list\n
  Only the first declaration is taken (if there are multiple) as stated by the standard:
  https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html"""
  checks.checkIfString(htmlAttributes, 0, 800)
  checks.checkIfString(key, 1, 30)
  result = []
  firstIdx = getAttributeIdx(htmlAttributes, key)
  if firstIdx == -1:
    return result
  startIdx = firstIdx + len(key)
  if startIdx >= len(htmlAttributes):
    return result
  nonSpaceIdxAfterKey = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlAttributes, startIdx, len(htmlAttributes))
  if nonSpaceIdxAfterKey == -1:
    return result
  firstCharAfterAttribute = htmlAttributes[nonSpaceIdxAfterKey]
  if firstCharAfterAttribute != '=':
    return result
  startIdx = nonSpaceIdxAfterKey + 1
  if len(htmlAttributes) == startIdx:
    return result
  firstNonSpaceIdxAfterEqual = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlAttributes, startIdx, len(htmlAttributes))
  if firstNonSpaceIdxAfterEqual == -1:
    return result
  firstCharAfterEqual = htmlAttributes[firstNonSpaceIdxAfterEqual]
  if firstCharAfterEqual != "'" and firstCharAfterEqual != "\"":
    return result
  startingQuoteIdx = firstNonSpaceIdxAfterEqual
  quoteCharUsed = firstCharAfterEqual
  startIdx = firstNonSpaceIdxAfterEqual + 1
  if len(htmlAttributes) == startIdx:
    return result
  closingQuotePos = htmlAttributes.find(quoteCharUsed, startIdx)
  if closingQuotePos == -1:
    return result
  if closingQuotePos == startIdx:
    return result
  valueIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlAttributes, startIdx, closingQuotePos)
  if valueIdx == -1:
    return result
  # TODO getFirstWhiteSpaceCharIdx
  # TODO getFirstCharIdx(string, skip=[WhiteSpace, ","], find=[AnyChar, "="])
  attrValues = htmlAttributes[startingQuoteIdx + 1 : closingQuotePos]
  values = attrValues.split()
  for value in values:
    if value not in result:
      result.append(value)
  return result

def getAttributeIdx(htmlAttributes, key):
  """Returns -1 if attribute not found and for empty string \n
   Only the first declaration is taken (if there are multiple) as stated by the standard:
   https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html"""
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

def getListOfHtmlAttributes(attributesString):
  """Returns empty list if attribute not found, for empty string and if **<attributesString>** is corrupt \n
     Only the first declaration is taken (if there are multiple) as stated by the standard:
     https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html"""
  checks.checkIfString(attributesString, 0, 1000)
  result = []
  currentAttribute = ""
  idx = 0
  while idx < len(attributesString):
    currentChar = attributesString[idx]
    if currentChar.isspace() or currentChar == "=":
      if currentAttribute and currentChar.isspace():
        if idx + 1 == len(attributesString) or \
            (not attributesString[idx + 1].isspace() and attributesString[idx + 1] != "="):
          result.append(currentAttribute)
          currentAttribute = ""
        idx += 1
        continue
      elif currentAttribute and currentChar == "=":
        nextNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, idx + 1, len(attributesString))
        if nextNonSpaceCharIdx == -1:
          return []
        nextNonSpaceChar = attributesString[nextNonSpaceCharIdx]
        if nextNonSpaceChar != "\"" and nextNonSpaceChar != "'":
          return []
        quoteCharUsed = nextNonSpaceChar
        closingQuoteIdx = attributesString.find(quoteCharUsed, nextNonSpaceCharIdx + 1)
        if closingQuoteIdx == -1:
          return []
        result.append(currentAttribute)
        currentAttribute = ""
        idx = closingQuoteIdx + 1
        continue
      elif not currentAttribute and currentChar.isspace():
        idx += 1
        continue
      return []
    else:
      currentAttribute += currentChar
      idx += 1
      continue
  if currentAttribute:
    result.append(currentAttribute)
  return result

# <htmlTag options>
def getOpenedHtmlTag(htmlTag, options=""):
  checks.checkIfString(htmlTag, 1, 100)
  checks.checkIfString(options, 0, 500)
  checks.checkIfStringIsAlphaNumerical(htmlTag)
  result = "<" + htmlTag
  if options:
    result += " " + options
  result += ">"
  return result

def getClosedHtmlTag(htmlTag):
  checks.checkIfString(htmlTag, 1, 100)
  checks.checkIfStringIsAlphaNumerical(htmlTag)
  return "</" + htmlTag + ">"

# \t\t\t
def getEscapedTabs(indentDepth):
  checks.checkIntIsBetween(indentDepth, 1, 50)
  ans = ""
  for i in range(indentDepth):
    ans += "\t"
  return ans
