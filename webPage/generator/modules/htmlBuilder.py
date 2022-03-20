from modules import checks

# include
def includeFileToHtmlOutputFile(htmlFile, includeFilePath, indentDepth):
  lines = getLinesFromFileWithEndingNewLine(includeFilePath)
  tabs = getIndentedTab(indentDepth)
  for line in lines:
    if (line and line != "\n"):
      htmlFile.write(tabs + line)
    else:
      htmlFile.write("\n")
  htmlFile.write("\n")

# <script src=".js" />
def addJsFileAsLink(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  tabs = getIndentedTab(indentDepth)
  htmlFile.write(tabs + "<script src=\"" + url + "\"")
  if (integrity is None or crossorigin is None or referrerpolicy is None):
    if (integrity is not None or crossorigin is not None or referrerpolicy is not None):
      raise Exception("integrity, crossorigin and referrerpolicy must be all set or None")
    htmlFile.write("></script>\n")
    return
  tabs += "\t"
  htmlFile.write("\n" + tabs + "integrity=\"" + integrity + "\"\n")
  htmlFile.write(tabs + "crossorigin=\"" + crossorigin + "\" referrerpolicy=\"" + referrerpolicy + "\"></script>\n")

# <link href=".css" />
def addCssFileAsLink(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  tabs = getIndentedTab(indentDepth)
  htmlFile.write(tabs + "<link href=\"" + url + "\"")
  if (integrity is None or crossorigin is None or referrerpolicy is None):
    if (integrity is not None or crossorigin is not None or referrerpolicy is not None):
      raise Exception("integrity, crossorigin and referrerpolicy must be all set or None")
    if len(url) > 95:
      htmlFile.write("\n" + tabs + "\t")
    else:
      htmlFile.write(" ")
    htmlFile.write("rel=\"stylesheet\" />\n")
    return
  tabs += "\t"
  htmlFile.write("\n" + tabs + "integrity=\"" + integrity + "\"\n")
  htmlFile.write(tabs + "rel=\"stylesheet\" crossorigin=\"" + crossorigin + "\" referrerpolicy=\"" + referrerpolicy + "\" />\n")

# <link href=".css" />
def getCssLinkHref(indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  tabs = getIndentedTab(indentDepth)
  #htmlFile.write(tabs + "<link href=\"" + url + "\"")
  if (integrity is None or crossorigin is None or referrerpolicy is None):
    if (integrity is not None or crossorigin is not None or referrerpolicy is not None):
      raise Exception("integrity, crossorigin and referrerpolicy must be all set or None")
    #if len(url) > 95:
      #htmlFile.write("\n" + tabs + "\t")
    #else:
      #htmlFile.write(" ")
    #htmlFile.write("rel=\"stylesheet\" />\n")
    return
  tabs += "\t"
  #htmlFile.write("\n" + tabs + "integrity=\"" + integrity + "\"\n")
  #htmlFile.write(tabs + "rel=\"stylesheet\" crossorigin=\"" + crossorigin + "\" referrerpolicy=\"" + referrerpolicy + "\" />\n")

# <br\> <br\> <br\>  ->  file
def addNewLineToHtmlOutputFile(htmlFile, indentDepth, nrOfNewLines = 1):
  tabs = getIndentedTab(indentDepth)
  newLinesString = getHtmlNewLines(indentDepth, nrOfNewLines)
  writeLinesToFileThenAppendNewLine(htmlFile, [newLinesString])

# <br\> <br\> <br\>
def getHtmlNewLines(indentDepth, nrOfNewLines = 1):
  checks.checkIntIsBetween(nrOfNewLines, 1, 50)
  result = getIndentedTab(indentDepth)
  for i in range(nrOfNewLines):
    result += "<br\>"
    if i != nrOfNewLines - 1:
      result += " "
  return result

# \t\t\t
def getIndentedTab(indentDepth):
  checks.checkIntIsBetween(indentDepth, 1, 50)
  ans=""; 
  for i in range(indentDepth):
    ans += "\t"
  return ans;

def getLinesFromFileWithEndingNewLine(filePath):
  f = open(filePath, "r")
  return f.readlines()

def writeLinesToFileThenAppendNewLine(file, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  if len(lines) == 0:
    return
  for line in lines:
    file.write(line)
    file.write("\n")