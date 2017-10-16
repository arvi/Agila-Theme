import re
import sublime
import sublime_plugin

class AgilaSelectThemeCommand(sublime_plugin.TextCommand):
    def run(self, action):
        self.themes = [
            "Agila",
            "Agila Origin",
            "Agila Dracula",
            "Agila Monokai",
            "Agila Cobalt",
            "Agila Classic",
            "Agila Light",
            "Agila Neon",
        ]
        self.schemes = [
            "Packages/Agila Theme/Agila Oceanic Next.tmTheme",
            "Packages/Agila Theme/Agila Origin Oceanic Next.tmTheme",
            "Packages/Agila Theme/Agila Dracula.tmTheme",
            "Packages/Agila Theme/Agila Monokai Extended.tmTheme",
            "Packages/Agila Theme/Agila Cobalt.tmTheme",
            "Packages/Agila Theme/Agila Classic Oceanic Next.tmTheme",
            "Packages/Agila Theme/Agila Light Solarized.tmTheme",
            "Packages/Agila Theme/Agila Neon Monocyanide.tmTheme",
        ]

        self.show_panel()

    def show_panel(self):
        self.view.window().show_quick_panel(self.themes, self.on_done, on_highlight=self.on_highlighted)

    def on_done(self, index):
        theme = self.themes[index] + '.sublime-theme'
        self.set_scheme(self.schemes[index])
        self.set_theme(theme)
        self.save_settings(theme)

    def on_highlighted(self, index):
        self.set_scheme(self.schemes[index])
        self.set_theme(self.themes[index] + '.sublime-theme')

    def set_scheme(self, scheme):
        self.get_settings().set('color_scheme', scheme)

    def set_theme(self, theme):
        self.get_settings().set('theme', theme)

    def get_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')

    def save_settings(self, theme):
        sublime.save_settings('Preferences.sublime-settings')
        sublime.status_message('Agila Theme: ' + theme)
        print('')
        print('[Agila Theme] ' +  theme)
        print('')
