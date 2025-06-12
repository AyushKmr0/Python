## Python hello.py

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

# --pycache--
- Source Change & Python Version
    ```bash
    hello_python.cpython-312.pyc
    ```
    - Works only for imported files
    - not for top level files

# Python Virtual Machine PVM

- Code loop to iterate byte code
- Run time engine
- Also known as Python interpreter

# Byte code is NOT machine Code

- Python specific interpretation
- cpython (standard implementation), jython, IronPython, Stackless, PyPy
    
