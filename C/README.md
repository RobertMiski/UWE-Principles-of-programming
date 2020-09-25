# C

In this folder it will have verious files to show different techquies to help anyone who is stuck.

if you are having trouble with setting C up with vs code by getting error with:`#include <stdio.h>`
press `Ctrl` `Shift` `p` and type `C/C++:Edit Configurations (JSON)` .
you'll need to chang the `"intelliSenseMode": "msvc-x64"` to `"intelliSenseMode": "gcc-x64"`,
`compilerPath` to the path of the gcc complier commonly found in `"C:/MinGW/bin/gcc.exe"` and add some paths to `includePath` if you find you gcc complier in `C:/MinGW/bin/gcc.exe` then

```
"C:/MinGW/lib/gcc/mingw32/9.2.0/include",
"C:/MinGW/lib/gcc/mingw32/9.2.0/include/c++",
"C:/MinGW/lib/gcc/mingw32/9.2.0"
```

if not then tray anf find these folder where ever you installed you gcc complier.

## Basics

- hello world (getting started for the first time)
- data types
- Selections (how to use if, if elif, if else statments)
- Iteration (to loop through someting)
- importing (importing you own code from another file or a module from online)

## Methods-functions- subroutines

- defining a method
- passing data in to a method (arguments)
- returning values from methods
