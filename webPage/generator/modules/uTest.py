import io
import sys
import unittest

from defTypes import appDecisionType

from modules import checks
from modules import filerw

def runAndEvaluateUnitTestsUsingTempFolder(relativeDirPath, filePattern, tempFolderName, outputStream = None):
  checks.checkIfStringDoesNotContainAnySubstringFromList(tempFolderName, 1, 200, ['/'])
  if relativeDirPath[-1] != "/":
    relativeDirPath += "/"
  pathToTempFolder = relativeDirPath + tempFolderName
  filerw.createDirectoryWithParentsIfNotExists(pathToTempFolder)
  result, lines = runAndEvaluateUnitTests(relativeDirPath, filePattern, outputStream)
  filerw.deleteNonEmptyDirectoryIfExists(pathToTempFolder)
  return result, lines

def runAndEvaluateUnitTests(relativeDirPath, filePattern, outputStream = None):
  lines = []
  unitTestsResult = collectAndRunUnitTestsByFilePattern(relativeDirPath, filePattern, outputStream)
  if unitTestsResult.wasSuccessful():
    lines.append(' - ALL UNIT TESTS PASSED -\n')
    return appDecisionType.AppDecisionType.CONTINUE_RUNNING, lines
  lines.append('\n ======= UNIT TEST FAILED ======= ')
  lines.append('\n [!] No operation can be done until all tests pass!')
  return appDecisionType.AppDecisionType.STOP_APP, lines

def collectAndRunUnitTestsByFilePattern(relativeDirPath, filePattern, outputStream = None):
  checks.checkIfString(relativeDirPath, 2, 300)
  checks.checkIfString(filePattern, 1, 300)
  if outputStream is not None:
    checks.checkIfType(outputStream, io.TextIOWrapper)
  suites = unittest.TestSuite()
  loader = unittest.TestLoader()
  runner = unittest.TextTestRunner(stream = outputStream, verbosity = 0)
  # suites.addTest(loader.loadTestsFromName('unitTests.unitTestsRunner_test'))
  suites.addTest(loader.discover(relativeDirPath, pattern = filePattern))
  result = runner.run(suites)
  if result.testsRun == 0:
    raise Exception('No tests found to run!')
  return result
