import imp
import unittest
from mock import patch
from io import BytesIO, StringIO
import six

pyp = imp.load_source('pyp', 'pyp')

if six.PY2:
    Stream = BytesIO
else:
    Stream = StringIO


class TestPypLargeFile(unittest.TestCase):

    class fakeOptparse(object):
        pass

    def _toPypStr(self, a):
        return [[pyp.PypStr(x.strip())] for x in a if x.strip()]

    def setUp(self):
        # what will become the options global in pyp,
        # an optparse arguments object
        fop = self.fakeOptparse()
        fop.small = False
        fop.text_file = False
        fop.manual = False
        fop.unmodified_config = False
        fop.rerun = False
        fop.blank_inputs = False
        fop.no_input = False

        self.pypObj = pyp.Pyp(opts=fop)

    def tearDown(self):
        self.pypObj = None

    def test_simple(self):
        inputs = self._toPypStr(['the quick brown fox'])
        argLine = ['p']
        expectedOut = 'the quick brown fox\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_slashes(self):
        inputs = self._toPypStr(['foo/bar'])
        argLine = ['s']
        expectedOut = 'foo\tbar\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

        argLine = ['slash']
        expectedOut = 'foo\tbar\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_index(self):
        inputs = self._toPypStr(['foo/bar'])
        argLine = ['s[0]']
        expectedOut = 'foo\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

        inputs = self._toPypStr(['foo\tbar'])
        argLine = ['w[0]']
        expectedOut = 'foo\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_single_pipe(self):
        inputs = self._toPypStr(['foo/bar'])
        argLine = ['s', 'u']
        expectedOut = 'foo_bar\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_split_join(self):
        inputs = self._toPypStr(['foo/bar'])
        argLine = [''' '_'.join(p.split('/')) ''']
        expectedOut = 'foo_bar\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_add(self):
        inputs = self._toPypStr(['foo/bar/foo1/bar1'])
        argLine = ['s[1] + s[3]']
        expectedOut = 'bar\tbar1\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_add_parens(self):
        inputs = self._toPypStr(['foo/bar/foo1/bar1'])
        argLine = ['(s[1] + s[3])']
        expectedOut = 'barbar1\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_parens_index(self):
        inputs = self._toPypStr(['foo/bar/foo1_bar1'])
        argLine = ['(s[1] + u[1])[1]']
        expectedOut = 'a\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_addition_index(self):
        inputs = self._toPypStr(['foo/bar/foo1_bar1'])
        argLine = ['s[1] + u[1]', 'p[1]']
        expectedOut = 'bar1\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_parens_pipe_index(self):
        inputs = self._toPypStr(['foo/bar/foo1_bar1'])
        argLine = ['(s[1] + u[1])', 'p[1]']
        expectedOut = 'a\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_regex(self):
        inputs = self._toPypStr(['QQQAbCd1234qqq'])
        argLine = ['p.re(\'[0-9a-fA-F]+\')']
        expectedOut = 'AbCd1234\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_replace(self):
        inputs = self._toPypStr(['foobar'])
        argLine = [''' p.replace('foo', 'bar') ''']
        expectedOut = 'barbar\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_string_format(self):
        inputs = self._toPypStr(['foo bar'])
        argLine = [''' '%s %s' % (w[1], w[0]) ''']
        expectedOut = 'bar foo\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_string_format_complex(self):
        inputs = self._toPypStr(['abc/123'])
        argLine = [''' '%d_%s' % (int(p.digits()[0]), s[0]) ''']
        expectedOut = '123_abc\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_kill(self):
        inputs = self._toPypStr(['foo bar', 'foobar', 'Foo Bar'])
        argLine = [''' p.kill('foobar') ''']
        expectedOut = 'foo bar\nFoo Bar\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_upper(self):
        inputs = self._toPypStr(['foo bar', 'foobar', 'Foo Bar'])
        argLine = ['p.upper()']
        expectedOut = 'FOO BAR\nFOOBAR\nFOO BAR\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_file(self):
        inputs = self._toPypStr(
            ['/home/abc/foobar.txt', '/usr/local/helloworld.psd', 'barfoo.csv']
        )
        argLine = ['p.file()']
        expectedOut = 'foobar.txt\nhelloworld.psd\nbarfoo.csv\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_dir(self):
        inputs = self._toPypStr(
            ['/home/abc/foobar.txt', '/usr/local/helloworld.psd', 'barfoo.csv']
        )
        argLine = ['p.dir()']
        expectedOut = '/home/abc\n/usr/local\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_digits(self):
        inputs = self._toPypStr(['abc123abc321'])
        argLine = ['p.digits()']
        expectedOut = '123\t321\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_isdigit(self):
        inputs = self._toPypStr(['abc123abc321', '123', '123.0'])
        argLine = ['p.isdigit()']
        expectedOut = '123\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_not_isdigit(self):
        inputs = self._toPypStr(['abc123abc321', '123', '123.0'])
        argLine = ['not p.isdigit()']
        expectedOut = 'abc123abc321\n123.0\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_keep(self):
        inputs = self._toPypStr(['abc123abc321', '123', '123.0', 'foo321bar'])
        argLine = [''' keep('321') ''']
        expectedOut = 'abc123abc321\nfoo321bar\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

        inputs = self._toPypStr(['abc123abc321', '123', '123.0', 'foo321bar'])
        argLine = [''' k('321') ''']
        expectedOut = 'abc123abc321\nfoo321bar\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_lose(self):
        inputs = self._toPypStr(['abc123abc321', '123', '123.0', 'foo321bar'])
        argLine = [''' lose('321') ''']
        expectedOut = '123\n123.0\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

        inputs = self._toPypStr(['abc123abc321', '123', '123.0', 'foo321bar'])
        argLine = [''' l('321') ''']
        expectedOut = '123\n123.0\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_trim(self):

        inputs = self._toPypStr(
            ['/home/abc/foobar.txt', '/usr/local/helloworld.psd', 'barfoo.csv']
        )
        argLine = ['p.trim()']
        expectedOut = '/home/abc\n/usr/local\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)

    def test_type_and_dir(self):

        inputs = self._toPypStr(
            ['/home/abc/foobar.txt', '/usr/local/helloworld.psd', 'barfoo.csv']
        )
        argLine = ['p.trim()']
        expectedOut = '/home/abc\n/usr/local\n'

        with patch('sys.stdout', new=Stream()) as cap_stdout:
            self.pypObj.processLarge(inputs, [], argLine, [])
            self.assertEquals(cap_stdout.getvalue(), expectedOut)
