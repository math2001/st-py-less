import sublime, sublime_plugin
import os
import lesscpy
import io

import six
import ply

import threading



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

def view_from_sublime():
	return sublime.active_window().active_view()	


def compileAndWrite(v, settings, content=None):


	STYLES = settings.get('styles', 'styles')
	CSS = settings.get('css', 'css')
	LESS = settings.get('less', 'less')

	v = v or view_from_sublime()
	lessfile = v.file_name()
	sm("less2css: Compiling {}".format(lessfile))

	if not lessfile:
		return em('You must save this view to compile it!')

	ext = os.path.splitext(lessfile)[1]
	if ext != '.less':
		return em("Can only compile '.less' files, not '{}'!".format(ext))

	style_dir, cssfile = dirnameUntil(lessfile, STYLES)

	if style_dir is False:
		return em("All your style must be put in a {} folders. See README.md for more infos".format(STYLES))

	cssfile = CSS + os.path.sep + os.path.sep.join(cssfile.split(os.path.sep)[1:])
	cssfile = os.path.dirname(cssfile)
	cssfile = os.path.join(style_dir, cssfile, os.path.splitext(os.path.basename(lessfile))[0] + '.css')

	if content is None:
		with open(lessfile, 'r') as fp:
			content = fp.read()


	try:
		less = lesscpy.compile(io.StringIO(content))
	except lesscpy.exceptions.CompilationError as e:
		em(e.msg)
	else:

		dirname = os.path.dirname(cssfile)

		if not os.path.exists( dirname ):
			os.makedirs(dirname)

		with open(cssfile, 'w') as fp:
			fp.write(less)

		sm("less2css: Finished compiling {}".format(cssfile))



class LessToCssListenerCommand(sublime_plugin.EventListener):

	def on_pre_save_async(self, v):
		if os.path.splitext(v.file_name())[1] == '.less':
			settings = sublime.load_settings('less2css.sublime-settings')
			if not settings.get('compile_on_save', True):
				print('no compiling', settings.get('compile_on_save', True))
				return

			content = v.substr(sublime.Region(0, v.size()))
			compileAndWrite(v, settings)



class LessToCssCommand(sublime_plugin.ApplicationCommand):

	def run(self):
		sublime.set_timeout_async(compileAndWrite, 0)

	def is_visible(self):
		return os.path.splitext(view_from_sublime().file_name())[1] == '.less'
