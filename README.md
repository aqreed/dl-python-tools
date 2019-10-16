# dltools

|  |  |
| ------ | ------ |
| Description | Deep Learning Tools |
| Author | aqreed <aqreed@protonmail.com> |
| Version | 0.0.1 |
| Python Version | 3.6 |
| Requires | Numpy, Matplotlib |

This packages is a compendium of tools I use in Deep Learning applications. Some are of my own, some are adapted from other developers (and will be credited for it).

---
**NOTE**:
dltools is under development and might change in the near future.

---

### Dependencies

This package depends on Python, NumPy and Matplotlib and is usually tested on Linux with the following versions:

Python 3.6, NumPy 1.16, Matplotlib 3.0

### Installation


To install in development mode:

```sh
$ git clone https://github.com/aqreed/dl-python-tools.git
$ cd dl-python-tools
$ pip install -e .
```

### Testing

dltools recommends py.test for running the test suite. Running from the top directory:

```sh
$ pytest
```

To test coverage (also from the top directory):

```sh
$ pytest --cov
```

### Bug reporting

Please feel free to open an [issue](https://github.com/aqreed/dl-python-tools/issues) on GitHub!

### License

MIT (see `COPYING`)
