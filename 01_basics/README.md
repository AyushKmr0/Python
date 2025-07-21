# Python hello.py

```bash

python_code.py      ->      Byte Code       ->      python VM
                                |
                            mostly hidden

```

## Compile to Byte code
    - Low level & Platform Independent (not machine code) 
    - Byte code runs faster

```bash
.pyc      ->      Compiled python (Frozen Binaries)

```

## --pycache--
- Source Change & Python Version
    ```bash
    hello_python.cpython-312.pyc
    ```
    - Works only for imported files
    - not for top level files

## Python Virtual Machine PVM

- Code loop to iterate byte code
- Run time engine
- Also known as Python interpreter

## Byte code is NOT machine Code

- Python specific interpretation
- cpython (standard implementation), jython, IronPython, Stackless, PyPy

<br/>
    
---
---

<br/>

# Object Types / Data Types

- Number : 1234, 3.14, 3+4j, 0b111, Deciaml(), Fraction()

- String : 'spam', "Bob's", b'a\x01x', u'sp\xc4m'

- List : [1, [2, 'three'], 4, 5], list(range(10))

- Tuple : (1, 'spam', 4, 'U'), typle('spam'), namedtuple

- Dictionary : {'food' : 'spam', 'taste' : 'yum'}, dict(hours = 10)

- Set : set('abc'), {'a', 'b', 'c'}

- Boolean : True, False

- None : None

- Functions, modules, classes

- Advance : Decorators, Generators, Iterators, MetaProgramming
