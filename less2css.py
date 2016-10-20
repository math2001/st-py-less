import sublime, sublime_plugin
import os
import lesscpy
import io

import six
import ply

from threading import Thread





def md(*t, **kwargs): sublime.message_dialog(kwargs.get('sep', ' ').join([str(el) for el in t]))

def sm(*t, **kwargs): sublime.status_message(kwargs.get('sep', ' ').join([str(el) for el in t]))

def em(*t, **kwargs): sublime.error_message(kwargs.get('sep', ' ').join([str(el) for el in t]))

def dirnameUntil(path, dirname):
	"""
		dirname is the path to stop
	"""

	if not (os.path.sep + dirname + os.path.sep) in path:
		return False, False

	path = path.split(os.path.sep)
	rest = []
	while path[-1] != dirname and len(path) > 1:
		rest.append(path.pop(-1))
	rest.reverse()
	return os.path.sep.join(path), os.path.sep.join(rest)

class LessCompiler(Thread):

	def __init__(self, less, done, args=[], kwargs={}):
		self.less = less
		self.done = done
		self.done_args = args
		self.done_kwargs = kwargs

		super(LessCompiler, self).__init__()

	def run(self):
		try:
			css = lesscpy.compile(io.StringIO(self.less))
		except lesscpy.exceptions.CompilationError as e:
			em(e.msg)
		else:
			# return print(self.done_args, self.done_kwargs)
			self.done(css, *self.done_args, **self.done_kwargs)
			return None

	
def compileAndWrite(v=False):

	print('run')

	STYLES = 'styles'
	CSS = 'css'
	LESS = 'less'

	v = v or sublime.active_window().active_view()
	lessfile = v.file_name()
	lessfile = 'C:\\Users\\math\\AppData\\Roaming\\Sublime Text 3\\Packages\\less2css\\styles\\less\\sample.less'

	if not lessfile:
		return em('You must save this view to compile it!')

	ext = os.path.splitext(lessfile)[1]
	if ext != '.less':
		return em("Can only compile '.less' files, not '{}'!".format(ext))

	

	style_dir, cssfile = dirnameUntil(lessfile, STYLES)

	if style_dir is False:
		return em("All your style must be put in a {} folders. See README.md for more infos".format(STYLES))

	cssfile = 'css' + os.path.sep + os.path.sep.join(cssfile.split(os.path.sep)[1:])
	cssfile = os.path.dirname(cssfile)
	cssfile = os.path.join(style_dir, cssfile, os.path.splitext(os.path.basename(lessfile))[0] + '.css')


	with open(lessfile, 'r') as fp:
		content = fp.read()


	try:
		less = lesscpy.compile(io.StringIO(content))
	except lesscpy.exceptions.CompilationError as e:
		em(e.msg)
	else:
		with open(cssfile, 'w') as fp:
			fp.write(less)


class LessToCssListenerCommand(sublime_plugin.EventListener):

	def on_post_save_async(self, v):
		if os.path.splitext(v.file_name())[1] == '.less':
			compileAndWrite(v)



