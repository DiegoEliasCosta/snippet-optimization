# sample.py
import foo

data = open('file')                     # a function call
foo.bar(arg=data)                       # a function call
foo.bar(arg=foo.meow(foo.z(arg=data)))  # three function calls
foo.woof(foo.x.y(arg=data))             # two function calls
