# Less Compiler For Sublime Text 3


You want to compile your Less files when you save them, but you don't want to instal nodejs just for this... So, you're stuck... Guess what? You're not because of this repo ;)

This plugin compiles automatically your less files as soon as you save them, using a [lesscpy](https://github.com/lesscpy/lesscpy). 

## Usage

To use this plugin, you need to organize your styles in a specific way:

	styles/
		less/
			what/
				ever.less
				you/
					want.less
			really.less
		css/
			# your less file will be compiled here with the same structure
			what/
				ever.css
				you/
					want.css
			really.css



## Installation

The installation is for now a bit tricky, because lesscpy's got some (small) dependences

### First dependence: `six.py` 

Go to your package folder (of sublime text), create a new file, and paste [this content](https://bitbucket.org/gutworth/six/raw/ca4580a5a648fc75abc568907e81abc80b05d58c/six.py) in it.

### Second dependence: `ply`

This one is a bit harder to install. You need to copy [this folder](https://github.com/dabeaz/ply/tree/master/ply) into you package folder. You an use [this website](http://kinolien.github.io/gitzip/) to do so. Extract it into `Packages` as a folder named `ply`. <a href="https://kinolien.github.com/gitzip/?download=https://github.com/dabeaz/ply/tree/master/ply" target="_blank"> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 26 26" fill="currentColor" style="width: 20px; height: 20px; vertical-align: middle;	"><path d="M25 17h-2c-.6 0-1 .4-1 1v2.5c0 .3-.2.5-.5.5h-17c-.3 0-.5-.2-.5-.5V18c0-.6-.4-1-1-1H1c-.6 0-1 .4-1 1v6c0 .6.4 1 1 1h24c.6 0 1-.4 1-1v-6c0-.6-.4-1-1-1zM12.3 16.7c.2.2.5.3.7.3s.5-.1.7-.3l6-6c.2-.2.3-.4.3-.7s-.1-.5-.3-.7l-1.4-1.4c-.2-.2-.4-.3-.7-.3-.3 0-.5.1-.7.3l-1 1c-.3.3-.9.1-.9-.4V2c0-.6-.4-1-1-1h-2c-.6 0-1 .4-1 1v6.6c0 .4-.5.7-.9.4l-1-1c-.2-.2-.4-.3-.7-.3-.3 0-.5.1-.7.3L6.3 9.4c-.2.2-.3.4-.3.7s.1.5.3.7l6 5.9z"/></svg> Download `.zip`</a>

### `lesscpy`

Same as `ply`, you need to download [this folder](https://github.com/lesscpy/lesscpy/tree/master/lesscpy) and extract it into you package folder. <a href="https://kinolien.github.com/gitzip/?download=https://github.com/lesscpy/lesscpy/tree/master/lesscpy" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 26 26" fill="currentColor" style="width: 20px; height: 20px; vertical-align: middle;	"><path d="M25 17h-2c-.6 0-1 .4-1 1v2.5c0 .3-.2.5-.5.5h-17c-.3 0-.5-.2-.5-.5V18c0-.6-.4-1-1-1H1c-.6 0-1 .4-1 1v6c0 .6.4 1 1 1h24c.6 0 1-.4 1-1v-6c0-.6-.4-1-1-1zM12.3 16.7c.2.2.5.3.7.3s.5-.1.7-.3l6-6c.2-.2.3-.4.3-.7s-.1-.5-.3-.7l-1.4-1.4c-.2-.2-.4-.3-.7-.3-.3 0-.5.1-.7.3l-1 1c-.3.3-.9.1-.9-.4V2c0-.6-.4-1-1-1h-2c-.6 0-1 .4-1 1v6.6c0 .4-.5.7-.9.4l-1-1c-.2-.2-.4-.3-.7-.3-.3 0-.5.1-.7.3L6.3 9.4c-.2.2-.3.4-.3.7s.1.5.3.7l6 5.9z"/></svg> Download `.zip`</a>

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

