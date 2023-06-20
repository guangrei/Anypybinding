[![Downloads](https://static.pepy.tech/badge/anybinding)](https://pepy.tech/project/anybinding) [![Downloads](https://static.pepy.tech/badge/anybinding/month)](https://pepy.tech/project/anybinding) [![Downloads](https://static.pepy.tech/badge/anybinding/week)](https://pepy.tech/project/anybinding)

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
