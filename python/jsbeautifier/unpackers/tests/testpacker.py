#
#     written by Stefano Sanfilippo <a.little.coder@gmail.com>
#

"""Tests for P.A.C.K.E.R. unpacker."""

import unittest
from jsbeautifier.unpackers.packer import detect, unpack

# pylint: disable=R0904


class TestPacker(unittest.TestCase):
    """P.A.C.K.E.R. testcase."""

    def test_detect(self):
        """Test detect() function."""
        def positive(source): return self.assertTrue(detect(source))

        def negative(source): return self.assertFalse(detect(source))

        negative('')
        negative('var a = b')
        positive('eval(function(p,a,c,k,e,r')
        positive('eval ( function(p, a, c, k, e, r')

    def test_unpack(self):
        """Test unpack() function."""
        def check(inp, out):
            return detect(inp) and self.assertEqual(unpack(inp), out)

        check("eval(function(p,a,c,k,e,r){e=String;if(!''.replace(/^/,String)"
              "){while(c--)r[c]=k[c]||c;k=[function(e){return r[e]}];e="
              "function(){return'\\\\w+'};c=1};while(c--)if(k[c])p=p.replace("
              "new RegExp('\\\\b'+e(c)+'\\\\b','g'),k[c]);return p}('0 2=1',"
              "62,3,'var||a'.split('|'),0,{}))", 'var a=1')
        check("function test (){alert ('This is a test!')}; "
              "eval(function(p,a,c,k,e,r){e=String;if(!''.replace(/^/,String))"
              "{while(c--)r[c]=k[c]||c;k=[function(e){return r[e]}];e=function"
              "(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp("
              "'\\b'+e(c)+'\\b','g'),k[c]);return p}('0 2=1',3,3,"
              "'var||a'.split('|'),0,{}))",
              "function test (){alert ('This is a test!')}; var a=1")


if __name__ == '__main__':
    unittest.main()
