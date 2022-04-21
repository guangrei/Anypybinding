# -*-coding:utf8;-*-
"""
The MIT License (MIT)

Copyright (c) 2022 anybinding https://github.com/guangrei/Anypybinding

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import subprocess
import os
import sys
import shlex


class Bind(object):

    def __init__(self, bin, path=None, direct_output=False):
        self.bin = [bin]
        self.direct_output = direct_output
        if path is None:
            self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        else:
            if os.path.isdir(path):
                self.path = path
            else:
                raise IOError("path isn't exists!")

    def _evaluate(self, command):
        command = shlex.split(command)
        if self.direct_output:
            p = subprocess.Popen(command, cwd=self.path)
            p.communicate()
            if p.poll() != 0:
                raise RuntimeError("exit code: {}".format(p.poll()))
        else:
            p = subprocess.Popen(command, cwd=self.path, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, universal_newlines=True)
            stdout, stderr = p.communicate()
            if p.poll() != 0:
                raise RuntimeError("{}".format(stdout))
            return stdout

    def _(self, *args):
        command = self.bin + list(args)
        if self.direct_output:
            p = subprocess.Popen(command, cwd=self.path)
            p.communicate()
            if p.poll() != 0:
                raise RuntimeError("exit code: {}".format(p.poll()))
        else:
            p = subprocess.Popen(command, cwd=self.path, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, universal_newlines=True)
            stdout, stderr = p.communicate()
            if p.poll() != 0:
                raise RuntimeError("{}".format(self.output))
            return stdout

    def __getattr__(self,
                    name):

        def call_cmd(*args):

            arg = " ".join([str(i) for i in args])
            command = "{0} {1} {2}".format(
                self.bin[0], name.replace("_", "-"), arg)
            return self._evaluate(command)
        return call_cmd


if __name__ == "__main__":
    pass
