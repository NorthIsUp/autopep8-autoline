autopep8-autoline
=================


![PyPi](https://img.shields.io/pypi/v/autopep8_autoline.svg)
![Build Status](https://img.shields.io/travis/NorthIsUp/autopep8_autoline.svg)


Want to run autopep8 but only on the lines you just changed?

autopep8-autolines wraps `autopep8` with some git stuff to automagically add the `--line-range`  option for each file passed in.

Usage is just like the `autopepe8` command. If y

If you are in a git repo the tool will discover all the changed files via some git commands.

```shell
$ autopep8-autoline
```
