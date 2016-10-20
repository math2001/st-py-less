# Less Compiler For Sublime Text 3


You want to compile your Less files when you save them, but you don't want to instal nodejs just for this... So, you're stuck... Guess what? You're not because of this repo ;)

This plugin compiles automatically your less files as soon as you save them, using a lesscpy.

## Installation

The installation is for now a bit tricky, because lesscpy's got some (small) dependences

### First dependence: `six.py` 

Go to your package folder (of sublime text), create a new file, and paste [this content](https://bitbucket.org/gutworth/six/raw/ca4580a5a648fc75abc568907e81abc80b05d58c/six.py) in it.

### Second dependence: `ply`

This one is a bit harder to install. You need to copy [this folder](https://github.com/dabeaz/ply/tree/master/ply) into you package folder. You an use [this website](http://kinolien.github.io/gitzip/) to do so. Extract it into `Packages` as a folder named `ply`.

### Third dependence: `lesscpy`

Same as `ply`, you need to download [this folder](https://github.com/lesscpy/lesscpy/tree/master/lesscpy) and extract it into you package folder.

### Install the plugin

Last step: get into your package directory and `clone` this repo (or download the zip and extract it). 

### At the end

At the end, your `packages` folder should look like this:
	
	Packages/
		...
		User/
		ply/
			__init__.py
			cpp.py
			ctokens.py
			lex.py
			yacc.py
			ygen.py
		lesscpy/
			less2css.py
			README.md
			...
		six.py

