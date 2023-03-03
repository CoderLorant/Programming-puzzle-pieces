import sys

sys.path.append('../..')

from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.sourceInspector.functionInspector import FunctionInspector
from unitTests4unitTests import similarFunctions as func

class FunctionInspectorTests(AutoUnitTest):

  def setUp(self):
    self.hash = 2

  def test_ctor_wrongType(self):
    self.assertRaises(Exception, FunctionInspector, print)
    self.assertRaises(Exception, FunctionInspector, None)
    self.assertRaises(Exception, FunctionInspector, [])
    self.assertRaises(Exception, FunctionInspector, {})
    self.assertRaises(Exception, FunctionInspector, 2)
    self.assertRaises(Exception, FunctionInspector, sys.path.copy)
    self.assertRaises(Exception, FunctionInspector, AutoUnitTest)

  def test_getFunctionName_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc")
    inspector = FunctionInspector(func.simpleFunc2)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc2")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc_sameImpl_differentSignature")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc_sameImpl_differentSignature_decorated")
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc")
    inspector = FunctionInspector(func.simpleFunc10)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc10")
    inspector = FunctionInspector(func.simpleFunc11)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc11")
    inspector = FunctionInspector(func.simpleFunc12)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc12")

  def test_getFunctionName_getMultipleTimes(self):
    inspector = FunctionInspector(func.simpleFunc)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc")
    self.assertEqual(inspector.getFunctionName(), "simpleFunc")
    self.assertEqual(inspector.getFunctionName(), "simpleFunc")

  def test_getFunctionSignature_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    self.assertEqual(inspector.getFunctionSignature(), "()")
    inspector = FunctionInspector(func.simpleFunc2)
    self.assertEqual(inspector.getFunctionSignature(), "()")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature)
    self.assertEqual(inspector.getFunctionSignature(), "(arg1, arg2)")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated)
    self.assertEqual(inspector.getFunctionSignature(), "(arg1, arg2)")
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    self.assertEqual(inspector.getFunctionSignature(), "(self)")
    inspector = FunctionInspector(func.simpleFunc21)
    self.assertEqual(inspector.getFunctionSignature(), "(str='2:1', d={'one': 1})")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated_annotated)
    self.assertEqual(inspector.getFunctionSignature(), "(arg1: int, arg2: str) -> bool")

  def test_getFunctionSignature_getMultipleTimes(self):
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated_annotated)
    self.assertEqual(inspector.getFunctionSignature(), "(arg1: int, arg2: str) -> bool")
    self.assertEqual(inspector.getFunctionSignature(), "(arg1: int, arg2: str) -> bool")
    self.assertEqual(inspector.getFunctionSignature(), "(arg1: int, arg2: str) -> bool")
    self.assertEqual(inspector.getFunctionSignature(), "(arg1: int, arg2: str) -> bool")

  def test_getFullSource_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    self.assertEqual(inspector.getFullSource(), "def simpleFunc():\n  a = 2\n  b = 3\n"
                                                "  return ((a + b) * 10) % 2 == 0\n")
    inspector = FunctionInspector(func.simpleFunc2)
    self.assertEqual(inspector.getFullSource(), "def \\\n    \\\n        simpleFunc2 \\\n                \\\n"
                                                "                (\n\n        )\\\n        \\\n        :\n"
                                                "  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature)
    self.assertEqual(inspector.getFullSource(), 'def simpleFunc_sameImpl_differentSignature(\n                       '
                                                '                    arg1 ,\n                                        '
                                                '   arg2\n                                          )     :\n'
                                                '  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated)
    self.assertEqual(inspector.getFullSource(), '@invertBool\ndef simpleFunc_sameImpl_differentSignature_decorated(\n'
                                                '                                           arg1 ,\n                 '
                                                '                          arg2\n                                    '
                                                '      )     :\n  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    self.assertEqual(inspector.getFullSource(), '  def simpleFunc( self ) \\\n          :\n'
                                                '    a = 2\n    b = 3\n    return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated_annotated)
    self.assertEqual(inspector.getFullSource(), '@invertBool\n'
                                                'def simpleFunc_sameImpl_differentSignature_decorated_annotated (\n'
                                                '                                           arg1   :    int,\n'
                                                '                                           arg2   :    str\n'
                                                '                                          )       ->   bool \\\n'
                                                '    :\n  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc12)
    self.assertEqual(inspector.getFullSource(), '@\\\ndefdef \\\n  (arg = " @defdef(dec) \\\n def simpleFunc12(): ")\n'
                                    'def \\\n        simpleFunc12 \\\n                ( str = "2:1",\n                '
                                    '  d = {"one": 1}\n        )\\\n        :\n  a = len(d)\n  b = len(str)\n'
                                    '  return ((a + b) * 10) % 2 == 0\n')

  def test_getFullSource_getMultipleTimes(self):
    inspector = FunctionInspector(func.simpleFunc)
    self.assertEqual(inspector.getFullSource(), "def simpleFunc():\n  a = 2\n  b = 3\n"
                                                "  return ((a + b) * 10) % 2 == 0\n")
    self.assertEqual(inspector.getFullSource(), "def simpleFunc():\n  a = 2\n  b = 3\n"
                                                "  return ((a + b) * 10) % 2 == 0\n")
    self.assertEqual(inspector.getFullSource(), "def simpleFunc():\n  a = 2\n  b = 3\n"
                                                "  return ((a + b) * 10) % 2 == 0\n")
    self.assertEqual(inspector.getFullSource(), "def simpleFunc():\n  a = 2\n  b = 3\n"
                                                "  return ((a + b) * 10) % 2 == 0\n")

  def test_getDefIndex_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def simpleFunc():\n"))
    inspector = FunctionInspector(func.simpleFunc2)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n    \\\n        simpleFunc2 "
                                               "\\\n                \\\n                (\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc3)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n    \\\n        simpleFunc3 "
                                               "\\\n                \\\n                (\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc4)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc4 \\\n                "
                                               "(\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc5)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc5 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc6)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc6 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc7)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc7 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc8)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc8 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc9)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc9 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc10)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc10 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc11)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc11 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def simpleFunc( self ) \\\n"))

  def test_getDefIndex_getMultipleTimes(self):
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def simpleFunc( self ) \\\n"))
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def simpleFunc( self ) \\\n"))
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def simpleFunc( self ) \\\n"))
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def simpleFunc( self ) \\\n"))

  def test_getNameIndex_examples(self):
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc( self ) \\\n"))
    inspector = FunctionInspector(func.simpleFunc)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc():\n"))
    inspector = FunctionInspector(func.simpleFunc2)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc2 \\\n                \\\n                (\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc3)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc3 \\\n                \\\n                (\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc4)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc4 \\\n                (\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc5)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc5 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc6)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc6 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc7)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc7 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc8)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc8 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc9)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc9 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc10)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc10 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc11)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc11 \\\n                ( arg\n        )\\\n        :"))

  def test_getNameIndex_getMultipleTimes(self):
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc( self ) \\\n"))
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc( self ) \\\n"))
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc( self ) \\\n"))
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc( self ) \\\n"))

  def test_getSignatureIndex_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("():\n"))
    inspector = FunctionInspector(func.simpleFunc2)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("(\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc3)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("(\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc4)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("(\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc5)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc6)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc7)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc8)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc9)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc10)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc11)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))

  def test_getSignatureIndex_getMultipleTimes(self):
    inspector = FunctionInspector(func.simpleFunc11)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))

  def test_getColonIndex_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def simpleFunc():"))
    inspector = FunctionInspector(func.simpleFunc2)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n    \\\n        simpleFunc2 \\\n                \\\n"
                                              "                (\n\n        )\\\n        \\\n        :"))
    inspector = FunctionInspector(func.simpleFunc3)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n    \\\n        simpleFunc3 \\\n                \\\n"
                                              "                (\n\n        )\\\n        \\\n        :"))
    inspector = FunctionInspector(func.simpleFunc4)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc4 \\\n                "
                                               "(\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc5)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc5 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc6)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc6 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc7)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc7 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc8)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc8 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc9)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc9 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc10)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc10 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc11)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc11 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc12)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc12 \\\n                ( str = \"2:1\","
                                              "\n                  d = {\"one\": 1}\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc25)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc25 \\\n                ( str = \"2:1\",  "
                                "# here is a ::comment::\n                  d = {\"one\": 1}\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc26)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("# also a comment in this line\n        )\\\n\\\n\\\n        :"))

  def test_getColonIndex_getMultipleTimes(self):
    inspector = FunctionInspector(func.simpleFunc12)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc12 \\\n                ( str = \"2:1\","
                                              "\n                  d = {\"one\": 1}\n        )\\\n        :"))
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc12 \\\n                ( str = \"2:1\","
                                              "\n                  d = {\"one\": 1}\n        )\\\n        :"))
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc12 \\\n                ( str = \"2:1\","
                                              "\n                  d = {\"one\": 1}\n        )\\\n        :"))
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc12 \\\n                ( str = \"2:1\","
                                              "\n                  d = {\"one\": 1}\n        )\\\n        :"))
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc12 \\\n                ( str = \"2:1\","
                                              "\n                  d = {\"one\": 1}\n        )\\\n        :"))

  def test_getImplementationIndex_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], "  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n")
    inspector = FunctionInspector(func.simpleFunc2)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], "  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n")
    inspector = FunctionInspector(func.simpleFunc3)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc4)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '    a = 2\n    b = 3\n    return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated_annotated)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc12)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc13)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc14)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc19)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc20)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc21)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc22)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc23)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc24)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')

  def test_getImplementationIndex_getMultipleTimes(self):
    inspector = FunctionInspector(func.simpleFunc14)
    source = inspector.getFullSource()
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')
    idx = inspector.getImplementationIndex()
    self.assertEqual(source[idx:], '  a = len(d)\n  b = len(str)\n  return ((a + b) * 10) % 2 == 0\n')

  def test_getDecorationIndex_notFound(self):
    inspector = FunctionInspector(func.simpleFunc)
    self.assertEqual(inspector.getDecorationIndex(), (False, -1))
    inspector = FunctionInspector(func.simpleFunc2)
    self.assertEqual(inspector.getDecorationIndex(), (False, -1))
    inspector = FunctionInspector(func.simpleFunc3)
    self.assertEqual(inspector.getDecorationIndex(), (False, -1))
    inspector = FunctionInspector(func.decorator)
    self.assertEqual(inspector.getDecorationIndex(), (False, -1))

  def test_getDecorationIndex_found(self):
    inspector = FunctionInspector(func.simpleFunc4)
    source = inspector.getFullSource()
    found, idx = inspector.getDecorationIndex()
    self.assertTrue(found)
    self.assertTrue(source[idx:].startswith("@defdeco\ndef \\\n"))
    inspector = FunctionInspector(func.simpleFunc5)
    source = inspector.getFullSource()
    found, idx = inspector.getDecorationIndex()
    self.assertTrue(found)
    self.assertTrue(source[idx:].startswith("@defdef (arg = \" def \")\ndef \\\n        simpleFunc5"))
    inspector = FunctionInspector(func.simpleFunc7)
    source = inspector.getFullSource()
    found, idx = inspector.getDecorationIndex()
    self.assertTrue(found)
    self.assertTrue(source[idx:].startswith("@defdef \\\n  (arg = \"\\\n          def simpleFunc7 ( ) \")\ndef \\"))
    inspector = FunctionInspector(func.simpleFunc14)
    source = inspector.getFullSource()
    found, idx = inspector.getDecorationIndex()
    self.assertTrue(found)
    self.assertTrue(source[idx:].startswith("@\\\ndefdef \\\n  (arg = \" @defdef(dec) \\\n "
                                            "def simpleFunc14(): \")\ndef \\"))
    inspector = FunctionInspector(func.simpleFunc15)
    source = inspector.getFullSource()
    found, idx = inspector.getDecorationIndex()
    self.assertTrue(found)
    self.assertTrue(source[idx:].startswith("@invertBool\n@\\\ndefdef \\\n  (arg = \" @defdef(dec) \\\n "
                                            "def simpleFunc15(): \")\ndef \\"))
    inspector = FunctionInspector(func.simpleFunc16)
    source = inspector.getFullSource()
    found, idx = inspector.getDecorationIndex()
    self.assertTrue(found)
    self.assertTrue(source[idx:].startswith("@invertBool\n@defdeco\n@\\\ndefdef \\\n  (arg = \" @defdef(dec) \\\n "
                                            "def simpleFunc16(): \")\ndef \\"))

  def test_getDecorationIndex_getMultipleTimes(self):
    inspector = FunctionInspector(func.simpleFunc16)
    source = inspector.getFullSource()
    found, idx = inspector.getDecorationIndex()
    self.assertTrue(found)
    self.assertTrue(source[idx:].startswith("@invertBool\n@defdeco\n@\\\ndefdef \\\n  (arg = \" @defdef(dec) \\\n "
                                            "def simpleFunc16(): \")\ndef \\"))
    found, idx = inspector.getDecorationIndex()
    self.assertTrue(found)
    self.assertTrue(source[idx:].startswith("@invertBool\n@defdeco\n@\\\ndefdef \\\n  (arg = \" @defdef(dec) \\\n "
                                            "def simpleFunc16(): \")\ndef \\"))
    found, idx = inspector.getDecorationIndex()
    self.assertTrue(found)
    self.assertTrue(source[idx:].startswith("@invertBool\n@defdeco\n@\\\ndefdef \\\n  (arg = \" @defdef(dec) \\\n "
                                            "def simpleFunc16(): \")\ndef \\"))
    found, idx = inspector.getDecorationIndex()
    self.assertTrue(found)
    self.assertTrue(source[idx:].startswith("@invertBool\n@defdeco\n@\\\ndefdef \\\n  (arg = \" @defdef(dec) \\\n "
                                            "def simpleFunc16(): \")\ndef \\"))
    inspector = FunctionInspector(func.simpleFunc)
    self.assertEqual(inspector.getDecorationIndex(), (False, -1))
    self.assertEqual(inspector.getDecorationIndex(), (False, -1))
    self.assertEqual(inspector.getDecorationIndex(), (False, -1))

  def test_isDecorator_notDecorator(self):
    self.assertFalse(FunctionInspector(func.simpleFunc).isDecorator())
    self.assertFalse(FunctionInspector(func.simpleFunc2).isDecorator())
    self.assertFalse(FunctionInspector(func.simpleFunc3).isDecorator())
    self.assertFalse(FunctionInspector(func.simpleFunc4).isDecorator())
    self.assertFalse(FunctionInspector(func.simpleFunc5).isDecorator())
    self.assertFalse(FunctionInspector(func.simpleFunc6).isDecorator())
    self.assertFalse(FunctionInspector(func.simpleFunc7).isDecorator())
    self.assertFalse(FunctionInspector(func.simpleFunc8).isDecorator())
    self.assertFalse(FunctionInspector(func.simpleFunc9).isDecorator())
    self.assertFalse(FunctionInspector(func.simpleFunc10).isDecorator())
    self.assertFalse(FunctionInspector(func.simpleFunc11).isDecorator())
    self.assertFalse(FunctionInspector(func.simpleFunc12).isDecorator())

  def test_isDecorator_decorator(self):
    self.assertTrue(FunctionInspector(func.defdeco).isDecorator())
    self.assertTrue(FunctionInspector(func.defdef).isDecorator())
    self.assertTrue(FunctionInspector(func.invertBool).isDecorator())

  def test_isDecorator_getMultipleTimes(self):
    inspector = FunctionInspector(func.defdeco)
    self.assertTrue(inspector.isDecorator())
    self.assertTrue(inspector.isDecorator())
    self.assertTrue(inspector.isDecorator())
    self.assertTrue(inspector.isDecorator())
    inspector = FunctionInspector(func.simpleFunc12)
    self.assertFalse(inspector.isDecorator())
    self.assertFalse(inspector.isDecorator())
    self.assertFalse(inspector.isDecorator())
    self.assertFalse(inspector.isDecorator())

  def test_getArgumentVariableNames_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    self.assertEqual(inspector.getArgumentVariableNames(), "")
    inspector = FunctionInspector(func.simpleFunc2)
    self.assertEqual(inspector.getArgumentVariableNames(), "")
    inspector = FunctionInspector(func.simpleFunc3)
    self.assertEqual(inspector.getArgumentVariableNames(), "")
    inspector = FunctionInspector(func.simpleFunc4)
    self.assertEqual(inspector.getArgumentVariableNames(), "")
    inspector = FunctionInspector(func.simpleFunc5)
    self.assertEqual(inspector.getArgumentVariableNames(), "arg")
    inspector = FunctionInspector(func.simpleFunc14)
    self.assertEqual(inspector.getArgumentVariableNames(), "str,d")

  def test_getArgumentVariableNames_getMultipleTimes(self):
    inspector = FunctionInspector(func.simpleFunc14)
    self.assertEqual(inspector.getArgumentVariableNames(), "str,d")
    self.assertEqual(inspector.getArgumentVariableNames(), "str,d")
    self.assertEqual(inspector.getArgumentVariableNames(), "str,d")
    self.assertEqual(inspector.getArgumentVariableNames(), "str,d")

  def test_getFunctionCallNames_examples(self):
    insp = FunctionInspector(func.simpleFunc)
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), ([], []))
    insp = FunctionInspector(func.SimpleClass.simpleFunc)
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), ([], []))
    insp = FunctionInspector(func.simpleFunc4)
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), ([], []))
    insp = FunctionInspector(func.simpleFunc14)
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), ([], []))
    insp = FunctionInspector(func.simpleFunc16)
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), ([], []))
    insp = FunctionInspector(func.simpleFunc17)
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), (['SimpleClass', 'simpleFunc16', 'simpleFunc2'], [('cl', 'simpleFunc')]))
    insp = FunctionInspector(func.simpleFunc18)
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), (['SimpleClass', 'simpleFunc16', 'simpleFunc2'],
                                        [('cl', 'simpleFunc'),
                                         ('other', 'saySomething'),
                                          ('otherFunctions', 'OtherClass'),
                                          ('otherFunctions', 'getFalseIfNotTrue')]))
    insp = FunctionInspector(func.simpleFunc34)
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), (['SimpleClass', 'simpleFunc16', 'simpleFunc2'],
                                        [('cl', 'simpleFunc'),
                                         ('other', 'saySomething'),
                                         ('otherFunctions', 'OtherClass'),
                                         ('otherFunctions', 'getFalseIfNotTrue')]))

  def test_getFunctionCallNames_getMultipleTimes(self):
    insp = FunctionInspector(func.simpleFunc18)
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), (['SimpleClass', 'simpleFunc16', 'simpleFunc2'],
                                        [('cl', 'simpleFunc'),
                                          ('other', 'saySomething'),
                                          ('otherFunctions', 'OtherClass'),
                                          ('otherFunctions', 'getFalseIfNotTrue')]))
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), (['SimpleClass', 'simpleFunc16', 'simpleFunc2'],
                                        [('cl', 'simpleFunc'),
                                         ('other', 'saySomething'),
                                         ('otherFunctions', 'OtherClass'),
                                         ('otherFunctions', 'getFalseIfNotTrue')]))
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), (['SimpleClass', 'simpleFunc16', 'simpleFunc2'],
                                        [('cl', 'simpleFunc'),
                                         ('other', 'saySomething'),
                                         ('otherFunctions', 'OtherClass'),
                                         ('otherFunctions', 'getFalseIfNotTrue')]))
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), (['SimpleClass', 'simpleFunc16', 'simpleFunc2'],
                                        [('cl', 'simpleFunc'),
                                         ('other', 'saySomething'),
                                         ('otherFunctions', 'OtherClass'),
                                         ('otherFunctions', 'getFalseIfNotTrue')]))
    funcs, methods = insp.getFunctionCallNames()
    self.assertEqual((funcs, methods), (['SimpleClass', 'simpleFunc16', 'simpleFunc2'],
                                        [('cl', 'simpleFunc'),
                                         ('other', 'saySomething'),
                                         ('otherFunctions', 'OtherClass'),
                                         ('otherFunctions', 'getFalseIfNotTrue')]))

  def test_getImplementationCode_examples(self):
    insp = FunctionInspector(func.simpleFunc_noReturn)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = 2\nb = 3\nisTrue = ((a + b) * 10) % 2 == 0\nif isTrue:\n  isTrue = not otherFunctions.getTrue()")
    insp = FunctionInspector(func.simpleFunc13)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc14)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc20)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc21)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc23)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc24)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc27)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.SimpleClass.simpleFunc)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = 2\nb = 3\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc28)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nif not d:\n  a += 2\n  if a == 20:\n    a = 12\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc29)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nif not d:\n  a += 2\n  if a == 20:returnValue = True\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc30)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nif not d:\n  a += 2\n  if a == 20 :  returnValue = True\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc31)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nif not d:\n  a += 2\n  if d[\"if True: return 2\"] == \"if False: return 3 \" :  returnValue = True\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc32)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nif not d:\n  a += 2\n  if d[\"if True: return 2\"] == \"if False: return 3 \" :  returnValue = True\nb = len(str)\nreturnValue = ((a + b) * 10) % 2 == 0")
    insp = FunctionInspector(func.simpleFunc33)
    code = insp.getImplementationCode()
    self.assertEqual(code, "a = len(d)\nif not d:\n  a += 2\n  if d[\"if True: return 2\"] == \"if False: return 3 \" :  returnValue = True\nb = len(str)\nreturnValue = \" return \"\nif not returnValue:returnValue = 2\nreturnValue = 2 if returnValue == ' return 2 ' else  3")
