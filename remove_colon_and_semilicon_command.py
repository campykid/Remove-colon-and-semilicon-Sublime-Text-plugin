import sublime, sublime_plugin

class RemoveColonAndSemiliconCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		REPL_STRING = ""
		REPL_PATTERN = [':', ';']
		for region in self.view.sel():
			content = self.view.substr(region)

			for pattern in REPL_PATTERN:
				content = content.replace(pattern, REPL_STRING)
				self.view.replace(edit, region, content)
