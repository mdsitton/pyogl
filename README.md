[![Code Health](https://landscape.io/github/mdsitton/pyogl/master/landscape.svg?style=flat)](https://landscape.io/github/mdsitton/pyogl/master)
# pyogl
From scratch python opengl binding  and generation tool.

To regenerate the binding run `gengl.py`.
Currently the code requires pysdl2 to load opengl functions for platforms other than windows.(this will change here soon)

To use the binding you need to call init() after you have an active opengl context(This may change in the future)