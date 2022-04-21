this library can binding any command line program to pythonic way, work for python 2 and 3.

## Installation

```
pip install anybinding
```

## Example

```python
from anybinding import Bind

busybox = Bind("busybox")
output = busybox._("--help")
output = busybox.ls("-a", "/")
```

for git program please use https://github.com/guangrei/Gitpybinding