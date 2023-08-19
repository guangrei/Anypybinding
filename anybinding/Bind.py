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

    def __init__(self, bin, path=None, direct_output=False, output_flag=1, timeout=0):
        if self.isIpy() == 'jupyter':
            self.output_flag = 2
        else:
            self.output_flag = output_flag
        self.bin = [bin]
        self.pid = 0
        self.timeout = timeout
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
            self.pid = p.pid
            if self.timeout > 0:
                p.wait(timeout=self.timeout)
            else:
                p.wait()
            p.communicate()
            if p.poll() != 0:
                raise RuntimeError("exit code: {}".format(p.poll()))
        else:
            p = subprocess.Popen(command, cwd=self.path, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, universal_newlines=True)
            self.pid = p.pid
            if self.timeout > 0:
                p.wait(timeout=self.timeout)
            else:
                p.wait()
            stdout, stderr = p.communicate()
            if self.output_flag == 2:
                return p.poll()
            if p.poll() != 0:
                raise RuntimeError("{}".format(stdout))
            return stdout

    def _(self, *args):
        command = self.bin + [str(i) for i in args]
        if self.direct_output:
            p = subprocess.Popen(command, cwd=self.path)
            self.pid = p.pid
            if self.timeout > 0:
                p.wait(timeout=self.timeout)
            else:
                p.wait()
            p.communicate()
            if p.poll() != 0:
                raise RuntimeError("exit code: {}".format(p.poll()))
        else:
            p = subprocess.Popen(command, cwd=self.path, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, universal_newlines=True)
            self.pid = p.pid
            if self.timeout > 0:
                p.wait(timeout=self.timeout)
            else:
                p.wait()
            stdout, stderr = p.communicate()
            if p.poll() != 0:
                raise RuntimeError("{}".format(self.output))
            return stdout

    def isIpy(self):
        try:
            check = str(type(get_ipython()))  # noqa: F821
            if 'zmqshell' in check:
                return 'jupyter'
            elif 'terminal' in check:
                return 'ipython'
            else:
                return False
        except:
            return False

    def __getattr__(self,
                    name):

        def call_cmd(*args, **kwargs):
            args = list(args)
            for k, v in kwargs.items():
                if k == "_":
                    if len(v):
                        args.append(v)
                    continue
                elif len(k) > 1:
                    k = "--"+str(k).replace("_", "-")
                else:
                    k = "-"+str(k).replace("_", "-")
                args.append(k)
                if len(v):
                    args.append(v)

            arg = " ".join([str(i) for i in args])
            command = "{0} {1} {2}".format(
                self.bin[0], name.replace("_", "-"), arg)
            return self._evaluate(command)
        return call_cmd


if __name__ == "__main__":
    pass
