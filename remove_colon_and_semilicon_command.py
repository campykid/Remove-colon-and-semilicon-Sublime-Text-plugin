import sublime, sublime_plugin

class RemoveColonAndSemiliconCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		REPL_STRING = ""
		for region in self.view.sel():
			content = self.view.substr(region)
			content = content.replace(':', REPL_STRING)
			self.view.replace(edit, region, content)

		for region in self.view.sel():
			content = self.view.substr(region)
			content = content.replace(';', REPL_STRING)
			self.view.replace(edit, region, content)
