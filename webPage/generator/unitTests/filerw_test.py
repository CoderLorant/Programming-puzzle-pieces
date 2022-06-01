import os
import sys
import unittest

sys.path.append('..')
from modules import filerw
from modules import htmlBuilder

class FileReadWriterTests(unittest.TestCase):

  def test_fileExists_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.fileExists(file)
    with self.assertRaises(Exception):
      filerw.fileExists("")
    with self.assertRaises(Exception):
      filerw.fileExists()
    with self.assertRaises(Exception):
      filerw.fileExists(None)
    with self.assertRaises(Exception):
      filerw.fileExists(23)
    with self.assertRaises(Exception):
      filerw.fileExists(False)

  def test_fileExists_example(self):
    file = open("./unitTests/temp/testFile.txt", "w")
    file.close()
    self.assertTrue(filerw.fileExists("./unitTests/temp/testFile.txt"))
    os.remove("./unitTests/temp/testFile.txt")
    self.assertFalse(filerw.fileExists("./unitTests/temp/testFile.txt"))

  def test_directoryExists_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.directoryExists(file)
    with self.assertRaises(Exception):
      filerw.directoryExists("")
    with self.assertRaises(Exception):
      filerw.directoryExists()
    with self.assertRaises(Exception):
      filerw.directoryExists(None)
    with self.assertRaises(Exception):
      filerw.directoryExists(23)
    with self.assertRaises(Exception):
      filerw.directoryExists(False)

  def test_directoryExists_example(self):
    self.assertTrue(filerw.directoryExists("./unitTests"))
    self.assertTrue(filerw.directoryExists("unitTests"))
    self.assertTrue(filerw.directoryExists("modules"))
    self.assertFalse(filerw.directoryExists("Xmodules"))
    self.assertFalse(filerw.directoryExists("modulesX"))
    self.assertFalse(filerw.directoryExists("ASfwefSAffASfj"))

  def test_createDirectoryWithParentsIfNotExists_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsIfNotExists(file)
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsIfNotExists("")
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsIfNotExists()
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsIfNotExists(None)
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsIfNotExists(23)
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsIfNotExists(False)

  def test_createDirectoryWithParentsIfNotExists_existingFolder(self):
    os.mkdir("./unitTests/testDir")
    self.assertTrue(filerw.directoryExists("./unitTests/testDir/"))
    filerw.createDirectoryWithParentsIfNotExists("./unitTests/testDir")
    self.assertTrue(filerw.directoryExists("./unitTests/testDir/"))
    os.rmdir("./unitTests/testDir")
    self.assertFalse(filerw.directoryExists("./unitTests/testDir/"))

  def test_createDirectoryWithParentsIfNotExists_nonExistingFolder(self):
    self.assertFalse(filerw.directoryExists("./unitTests/testDir2/"))
    filerw.createDirectoryWithParentsIfNotExists("./unitTests/testDir2")
    self.assertTrue(filerw.directoryExists("./unitTests/testDir2/"))
    os.rmdir("./unitTests/testDir2")
    self.assertFalse(filerw.directoryExists("unitTests/testDir2/"))

  def test_createDirectoryWithParentsIfNotExists_nonExistingNestedFolder(self):
    self.assertFalse(filerw.directoryExists("./unitTests/testDir3/testDir4"))
    self.assertFalse(filerw.directoryExists("./unitTests/testDir3/"))
    filerw.createDirectoryWithParentsIfNotExists("./unitTests/testDir3/testDir4")
    self.assertTrue(filerw.directoryExists("./unitTests/testDir3/testDir4/"))
    os.rmdir("./unitTests/testDir3/testDir4")
    os.rmdir("./unitTests/testDir3")
    self.assertFalse(filerw.directoryExists("unitTests/testDir3/testDir4/"))
    self.assertFalse(filerw.directoryExists("unitTests/testDir3"))

  def test_getLinesByFilePathWithEndingNewLine_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY")
    file.close()
    linesFromFile = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesByFilePathWithEndingNewLine_1line_1emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY\n")
    file.close()
    linesFromFile = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY\n")

  def test_getLinesByFilePathWithEndingNewLine_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    linesFromFile = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear\n")
    self.assertEqual(linesFromFile[1], "this is the tester\n")

  def test_getLinesByFilePath_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY")
    file.close()
    linesFromFile = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesByFilePath_1line_1emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY\n")
    file.close()
    linesFromFile = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesByFilePath_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    linesFromFile = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear")
    self.assertEqual(linesFromFile[1], "this is the tester")

  def test_getLinesWithEndingNewLine_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLinesWithEndingNewLine(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesWithEndingNewLine_1line_1emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY\n")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLinesWithEndingNewLine(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY\n")

  def test_getLinesWithEndingNewLine_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLinesWithEndingNewLine(file)
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear\n")
    self.assertEqual(linesFromFile[1], "this is the tester\n")

  def test_getLines_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLines(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLines_1line_1emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY\n")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLines(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLines_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLines(file)
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear")
    self.assertEqual(linesFromFile[1], "this is the tester")

  def test_writeLinesPrefixedToFile_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile(file, "prefix", "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile(file, "prefix", None)
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile(file, 1, ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile(file, ["prefix"], ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile("./unitTests/temp/test.txt", "prefix", ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile(None, "prefix", ["asd"])

  def test_writeLinesPrefixedToFile_emptyList(self):
    readLines = self.helper_writeLinesPrefixedToFile("== prefix ==", [])
    self.assertEqual(len(readLines), 0)

  def test_writeLinesPrefixedToFile_oneEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFile("== prefix ==", [""])
    self.assertEqual(len(readLines), 1)
    # empty line
    self.assertEqual(readLines[0], "")

  def test_writeLinesPrefixedToFile_twoEmptyStrings(self):
    readLines = self.helper_writeLinesPrefixedToFile("== prefix ==", ["", ""])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFile_oneNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFile("[-]", ["\n"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "")

  def test_writeLinesPrefixedToFile_twoNewLines(self):
    readLines = self.helper_writeLinesPrefixedToFile("-=-", ["\n", "\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFile_NewLineAndEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFile("line: ", ["\n", ""])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFile_emptyStringAndNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFile("text: ", ["", "\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFile_oneString(self):
    readLines = self.helper_writeLinesPrefixedToFile("Greetings: ", ["hey"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "Greetings: hey")

  def test_writeLinesPrefixedToFile_twoStrings(self):
    readLines = self.helper_writeLinesPrefixedToFile("[text] ", ["hey", "Joe"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "[text] hey")
    self.assertEqual(readLines[1], "[text] Joe")

  def test_writeLinesPrefixedToFile_threeStrings(self):
    readLines = self.helper_writeLinesPrefixedToFile("", ["hey", "magnificent", "Joe"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "hey")
    self.assertEqual(readLines[1], "magnificent")
    self.assertEqual(readLines[2], "Joe")

  def test_writeLinesPrefixedToFile_oneStringEndingWithNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFile(".", ["hey\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], ".hey")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFile_twoStringsEndingWithNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFile("# ", ["hey\n", "Joe\n"])
    self.assertEqual(len(readLines), 4)
    self.assertEqual(readLines[0], "# hey")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "# Joe")
    self.assertEqual(readLines[3], "")

  def test_writeLinesPrefixedToFile_stringsAndNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFile(">", ["hey\n", "Joe\n", "\n"])
    self.assertEqual(len(readLines), 5)
    self.assertEqual(readLines[0], ">hey")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], ">Joe")
    self.assertEqual(readLines[3], "")
    self.assertEqual(readLines[4], "")

  def test_writeLinesPrefixedToFile_stringsAndNewLineAndEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFile("\t\t", ["hey\n", "Joe\n", "\n", ""])
    self.assertEqual(len(readLines), 6)
    self.assertEqual(readLines[0], "\t\they")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "\t\tJoe")
    self.assertEqual(readLines[3], "")
    self.assertEqual(readLines[4], "")
    self.assertEqual(readLines[5], "")

  def helper_writeLinesPrefixedToFile(self, prefix, lines):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesPrefixedToFile(file, prefix, lines)
    file.close()
    return filerw.getLinesByFilePath("./unitTests/temp/test.txt")

  def test_writeLinesPrefixedToFileThenAppendNewLine_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine(file, "prefix", "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine(file, "prefix", None)
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine(file, 1, ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine(file, ["prefix"], ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine("./unitTests/temp/test.txt", "prefix", ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine(None, "prefix", ["asd"])

  def test_writeLinesPrefixedToFileThenAppendNewLine_emptyList(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("== prefix ==", [])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "")  # empty line

  def test_writeLinesPrefixedToFileThenAppendNewLine_oneEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("== prefix ==", [""])
    self.assertEqual(len(readLines), 2)
    # empty lines
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_twoEmptyStrings(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("== prefix ==", ["", ""])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_oneNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("[-]", ["\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_twoNewLines(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("-=-", ["\n", "\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_NewLineAndEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("line: ", ["\n", ""])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_emptyStringAndNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("text: ", ["", "\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_oneString(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("Greetings: ", ["hey"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "Greetings: hey")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_twoStrings(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("[text] ", ["hey", "Joe"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "[text] hey")
    self.assertEqual(readLines[1], "[text] Joe")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_threeStrings(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("", ["hey", "magnificent", "Joe"])
    self.assertEqual(len(readLines), 4)
    self.assertEqual(readLines[0], "hey")
    self.assertEqual(readLines[1], "magnificent")
    self.assertEqual(readLines[2], "Joe")
    self.assertEqual(readLines[3], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_oneStringEndingWithNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine(".", ["hey\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], ".hey")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_twoStringsEndingWithNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("# ", ["hey\n", "Joe\n"])
    self.assertEqual(len(readLines), 5)
    self.assertEqual(readLines[0], "# hey")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "# Joe")
    self.assertEqual(readLines[3], "")
    self.assertEqual(readLines[4], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_stringsAndNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine(">", ["hey\n", "Joe\n", "\n"])
    self.assertEqual(len(readLines), 6)
    self.assertEqual(readLines[0], ">hey")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], ">Joe")
    self.assertEqual(readLines[3], "")
    self.assertEqual(readLines[4], "")
    self.assertEqual(readLines[5], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_stringsAndNewLineAndEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("\t\t", ["hey\n", "Joe\n", "\n", ""])
    self.assertEqual(len(readLines), 7)
    self.assertEqual(readLines[0], "\t\they")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "\t\tJoe")
    self.assertEqual(readLines[3], "")
    self.assertEqual(readLines[4], "")
    self.assertEqual(readLines[5], "")
    self.assertEqual(readLines[6], "")

  def helper_writeLinesPrefixedToFileThenAppendNewLine(self, prefix, lines):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesPrefixedToFileThenAppendNewLine(file, prefix, lines)
    file.close()
    return filerw.getLinesByFilePath("./unitTests/temp/test.txt")

  def test_writeStringsPrefixedToFileThenAppendNewLine_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, "prefix", "asd")
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, "prefix", None)
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, 1, ["asd"])
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, ["prefix"], ["asd"])
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine("./unitTests/temp/test.txt", "prefix", ["asd"])
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(None, "prefix", ["asd"])

  def test_writeStringsPrefixedToFileThenAppendNewLine_emptyList(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(1, [])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_oneEmptyString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(2, [""])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_twoEmptyStrings(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["", ""])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_oneNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_twoNewLines(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(5, ["\n", "\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_NewLineAndEmptyString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["\n", ""])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_emptyStringAndNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["", "\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_oneString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(2, ["hey"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\t\they\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_twoStrings(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(1, ["hey", "Joe"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\they\tJoe\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_threeStrings(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(1, ["hey", "magnificent", "Joe"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\they\tmagnificent\tJoe\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_oneStringEndingWithNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["hey\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "\t\t\they\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_twoStringsEndingWithNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(4, ["hey\n", "Joe\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\t\t\t\they\n")
    self.assertEqual(readLines[1], "\t\t\t\tJoe\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_stringsAndNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(4, ["hey\n", "Joe\n", "\n"])
    self.assertEqual(len(readLines), 4)
    self.assertEqual(readLines[0], "\t\t\t\they\n")
    self.assertEqual(readLines[1], "\t\t\t\tJoe\n")
    self.assertEqual(readLines[2], "\n")
    self.assertEqual(readLines[3], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_stringsAndNewLineAndEmptyString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(4, ["hey\n", "Joe\n", "\n", ""])
    self.assertEqual(len(readLines), 5)
    self.assertEqual(readLines[0], "\t\t\t\they\n")
    self.assertEqual(readLines[1], "\t\t\t\tJoe\n")
    self.assertEqual(readLines[2], "\n")
    self.assertEqual(readLines[3], "\n")
    self.assertEqual(readLines[4], "\n")

  def helper_writeStringsIndentedToFileThenAppendNewLine(self, indent, lines):
    file = open("./unitTests/temp/test.txt", "w")
    tabs = htmlBuilder.getEscapedTabs(indent)
    filerw.writeStringsPrefixedToFileThenAppendNewLine(file, tabs, lines)
    file.close()
    return filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")

  def test_writeLinesToFileThenAppendNewLine_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToFileThenAppendNewLine(file, "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToFileThenAppendNewLine(file, 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToFileThenAppendNewLine(file, None)
    with self.assertRaises(Exception):
      filerw.writeLinesToFileThenAppendNewLine("text.txt", ["firstLine"])

  def test_writeLinesToFileThenAppendNewLine_noLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, [])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFileThenAppendNewLine_emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, [""])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\n")

  def test_writeLinesToFileThenAppendNewLine_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["this is me"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me\n")

  def test_writeLinesToFileThenAppendNewLine_1lineEndingWithNewline(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["this is me\n"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeLinesToFileThenAppendNewLine_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["this is me:", "\tJohn Doe, VIP executor"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")

  def test_writeLinesToFileThenAppendNewLine_3lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2], "tel: 0875432123\n")

  def test_writeLinesToFileByFilePathThenAppendNewLine_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile("./unitTests/temp/test.txt", "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile("./unitTests/temp/test.txt", 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile("./unitTests/temp/test.txt", None)
    with self.assertRaises(Exception):
      filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile(file, ["firstLine"])

  def test_writeLinesToFileByFilePathThenAppendNewLine_Noline(self):
    filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile("./unitTests/temp/test.txt", [])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFileByFilePathThenAppendNewLine_emptyLine(self):
    filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile("./unitTests/temp/test.txt", [""])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\n")

  def test_writeLinesToFileByFilePathThenAppendNewLine_emptyLine_afterSomethingElse(self):
    filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile("./unitTests/temp/test.txt",
                                                                   ["first", "second", "third", "fourth"])
    filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile("./unitTests/temp/test.txt", [""])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\n")

  def test_writeLinesToFileByFilePathThenAppendNewLine_1line(self):
    filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile("./unitTests/temp/test.txt", ["this is me"])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me\n")

  def test_writeLinesToFileByFilePathThenAppendNewLine_1lineEndingWithNewline(self):
    filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile("./unitTests/temp/test.txt", ["this is me\n"])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeLinesToFileByFilePathThenAppendNewLine_2lines(self):
    filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile("./unitTests/temp/test.txt",
                                                                   ["this is me:", "\tJohn Doe, VIP executor"])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")

  def test_wwriteLinesToFileByFilePathThenAppendNewLine_3lines(self):
    filerw.writeLinesToFileByFilePathThenAppendNewLineAndCloseFile("./unitTests/temp/test.txt",
                                                                   ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2], "tel: 0875432123\n")

  def test_writeLinesToFile_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToFile(file, "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToFile(file, 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToFile(file, None)
    with self.assertRaises(Exception):
      filerw.writeLinesToFile("text.txt", ["firstLine"])

  def test_writeLinesToFile_Noline(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, [])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFile_emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, [""])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFile_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, ["this is me"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me")

  def test_writeLinesToFile_1lineEndingWithNewline(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, ["this is me\n"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me\n")

  def test_writeLinesToFile_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, ["this is me:", "\tJohn Doe, VIP executor"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor")

  def test_writeLinesToFile_3lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2], "tel: 0875432123")

  def test_writeLinesToFileByFilePath_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToFileByFilePathAndCloseFile("./unitTests/temp/test.txt", "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToFileByFilePathAndCloseFile("./unitTests/temp/test.txt", 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToFileByFilePathAndCloseFile("./unitTests/temp/test.txt", None)
    with self.assertRaises(Exception):
      filerw.writeLinesToFileByFilePathAndCloseFile(file, ["firstLine"])

  def test_writeLinesToFileByFilePath_noLine(self):
    filerw.writeLinesToFileByFilePathAndCloseFile("./unitTests/temp/test.txt", [])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFileByFilePath_noLine_afterSomeLines(self):
    filerw.writeLinesToFileByFilePathAndCloseFile("./unitTests/temp/test.txt", ["hey", "little", "man"])
    filerw.writeLinesToFileByFilePathAndCloseFile("./unitTests/temp/test.txt", [])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFileByFilePath_emptyLine(self):
    filerw.writeLinesToFileByFilePathAndCloseFile("./unitTests/temp/test.txt", [""])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFileByFilePath_1line(self):
    filerw.writeLinesToFileByFilePathAndCloseFile("./unitTests/temp/test.txt", ["this is me"])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me")

  def test_writeLinesToFileByFilePath_1lineEndingWithNewline(self):
    filerw.writeLinesToFileByFilePathAndCloseFile("./unitTests/temp/test.txt", ["this is me\n"])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me\n")

  def test_writeLinesToFileByFilePath_2lines(self):
    filerw.writeLinesToFileByFilePathAndCloseFile("./unitTests/temp/test.txt",
                                                  ["this is me:", "\tJohn Doe, VIP executor"])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor")

  def test_writeLinesToFileByFilePath_3lines(self):
    filerw.writeLinesToFileByFilePathAndCloseFile("./unitTests/temp/test.txt",
                                                  ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2], "tel: 0875432123")

  def test_rTrimNewLines_nonSense(self):
    with self.assertRaises(Exception):
      filerw.rTrimNewLines()
    with self.assertRaises(Exception):
      filerw.rTrimNewLines("hello")
    with self.assertRaises(Exception):
      filerw.rTrimNewLines(None)
    with self.assertRaises(Exception):
      filerw.rTrimNewLines("hey\n")
    with self.assertRaises(Exception):
      filerw.rTrimNewLines(False)
    with self.assertRaises(Exception):
      filerw.rTrimNewLines(["one", None, "three"])

  def test_rTrimNewLines_emptyList(self):
    result = filerw.rTrimNewLines([])
    self.assertEqual(len(result), 0)

  def test_rTrimNewLines_oneElement(self):
    result = filerw.rTrimNewLines(["Hello!"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "Hello!")
    result = filerw.rTrimNewLines(["\n\tHello!"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "\n\tHello!")
    result = filerw.rTrimNewLines(["\n\tHello!\n"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "\n\tHello!")
    result = filerw.rTrimNewLines(["Hello\n\n"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "Hello")
    result = filerw.rTrimNewLines(["Hello\n\n\n\n\n\n\n"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "Hello")

  def test_rTrimNewLines_twoElements(self):
    result = filerw.rTrimNewLines(["Hello", "hey\n"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "hey")
    result = filerw.rTrimNewLines(["hey\n", "Hello\n"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[1], "Hello")
    self.assertEqual(result[0], "hey")
    result = filerw.rTrimNewLines(["Hello", "hey"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "hey")
    result = filerw.rTrimNewLines(["Hello", "\n\n"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "")

  def test_rTrimNewLines_threeElements(self):
    result = filerw.rTrimNewLines(["Hello\n", "hey", "hi\n\n"])
    self.assertEqual(len(result), 3)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "hey")
    self.assertEqual(result[2], "hi")
