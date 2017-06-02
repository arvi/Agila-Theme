# Agila Theme
##### A Sublime Text 3 UI Theme
Couldn't find a theme I really dig, so I tried to make my own theme based on all the things/elements I like from wonderful themes I've used before. :)

***

## Screenshots
Screenshots below are based on the default starting point of all Agila Themes wherein _Font face: [__Inconsolata__](https://www.google.com/fonts/specimen/Inconsolata) | Font size: 21*._ 

You can customize the UI to your liking _(e.g camouflage workspace with the color scheme background, sidebar, tab, autocomplete, and scrollbar setup/color preferences)_ by referring to the **"[Settings](#settings)"** section of this documentation. Enjoy! :)

#### Agila Theme
![Screenshot](https://www.dropbox.com/s/jt3choxq6b583t7/Agila%20Theme.png?raw=1)

#### Agila Origin Theme
![Screenshot](https://www.dropbox.com/s/wuhcxftbw1nk9gn/Agila%20Origin%20Oceanic%20Next%20Theme.png?raw=1)

#### Agila Dracula Theme
![Screenshot](https://www.dropbox.com/s/egklxdt86ilap4l/Agila%20Dracula%20Theme.png?raw=1)

#### Agila Monokai Theme
![Screenshot](https://www.dropbox.com/s/y10kw35wunjssxi/Agila%20Monokai%20Theme.png?raw=1)

#### Agila Cobalt Theme
![Screenshot](https://www.dropbox.com/s/uh2cdicqe75onki/Agila%20Cobalt%20Theme.png?raw=1)

#### Agila Classic Theme
![Screenshot](https://www.dropbox.com/s/xlg43vr2ikxogch/Agila%20Classic%20Theme.png?raw=1)

#### Agila Light Theme
![Screenshot](https://www.dropbox.com/s/tmjpeas5iuvotbd/Agila%20Light%20Theme.png?raw=1)

#### Agila Neon Theme
![Screenshot](https://www.dropbox.com/s/fdv9lhvqsqnmxux/Agila%20Neon%20Theme.png?raw=1)

---

### How to Install

##### *Chill* way
via [Package Control](https://packagecontrol.io/), where Agila is listed as *`Agila Theme`*.

1. Open Command Palette using menu item *`Tools > Command Palette...`* or `CMD/CTRL + SHIFT + P`
2. Choose `Package Control: Install Package`
3. Find *`Agila Theme`* and hit *`Enter`*

##### *Woooo* way
via installing the theme manually.

1. [Download the latest release .zip](https://github.com/arvi/Agila-Theme/releases)
2. Unzip and rename folder to *`Agila Theme`*.
3. Move *`Agila Theme`* folder inside the Packages directory (*`Preferences > Browse packages...`*)

---
### Themes
Agila themes include Markdown syntax highlighting provided you have [Markdown Extended](https://packagecontrol.io/packages/Markdown%20Extended) package installed.

### Activation
##### *Chill* way via Skins
[Skins](https://packagecontrol.io/packages/Skins) provides an easy way to manage your themes for Sublime Text 3. Run its `Select Skin` command from the Command Palette *`Tools > Command Palette...`* or `CMD/CTRL + SHIFT + P` and choose any of the various `Agila` theme variants from the list. 
**No extra steps for activating Markdown syntax highlighting based on selected theme.**


##### *Woooo* way
via User Preferences file (*`Sublime Text > Preferences > Settings - User`*). After setting up,
don't forget to **restart Sublime Text Editor** for changes to take effect. 

**To also enable Markdown syntax highlighting based on selected theme:**

1. Open a Markdown file
2. Go to Preferences > Settings - Syntax Specific and change `color_scheme` value based on the last `color_scheme` setting specific to theme below.

##### Default theme
#
```json
"theme": "Agila.sublime-theme",
"color_scheme": "Packages/Agila Theme/Agila Oceanic Next.tmTheme",
```

```json
"color_scheme": "Packages/Agila Theme/Markdown/Oceanic Next Markdown.tmTheme"
```

##### Origin theme
#
```json
"theme": "Agila Origin.sublime-theme",
"color_scheme": "Packages/Agila Theme/Agila Origin Oceanic Next.tmTheme",
```
```json
"color_scheme": "Packages/Agila Theme/Markdown/Oceanic Next Origin Markdown.tmTheme"
```

##### Dracula theme
#
```json
"theme": "Agila Dracula.sublime-theme",
"color_scheme": "Packages/Agila Theme/Agila Dracula.tmTheme",
```
```json
"color_scheme": "Packages/Agila Theme/Markdown/Dracula Markdown.tmTheme"
```

##### Monokai theme
#
```json
"theme": "Agila Monokai.sublime-theme",
"color_scheme": "Packages/Agila Theme/Agila Monokai Extended.tmTheme",
```
```json
"color_scheme": "Packages/Agila Theme/Markdown/Monokai Markdown.tmTheme"
```

##### Cobalt theme
#
```json
"theme": "Agila Cobalt.sublime-theme",
"color_scheme": "Packages/Agila Theme/Agila Cobalt.tmTheme",
```
```json
"color_scheme": "Packages/Agila Theme/Markdown/Cobalt Markdown.tmTheme"
```

##### Classic theme
#
```json
"theme": "Agila Classic.sublime-theme",
"color_scheme": "Packages/Agila Theme/Agila Classic Oceanic Next.tmTheme",
```
```json
"color_scheme": "Packages/Agila Theme/Markdown/Classic Oceanic Next Markdown.tmTheme"
```

##### Light theme
#
```json
"theme": "Agila Light.sublime-theme",
"color_scheme": "Packages/Agila Theme/Agila Light Solarized.tmTheme",
```
```json
"color_scheme": "Packages/Agila Theme/Markdown/Light Solarized Markdown.tmTheme"
```

##### Neon theme
#
```json
"theme": "Agila Neon.sublime-theme",
"color_scheme": "Packages/Agila Theme/Agila Neon Monocyanide.tmTheme",
```
```json
"color_scheme": "Packages/Agila Theme/Markdown/Neon Monocyanide Markdown.tmTheme"
```
#


Note: You can use active guide with these schemes by adding:
```json
"indent_guide_options":
[
    "draw_normal",
    "draw_active"
],
```

---

### Settings
I've made some UI parts customizable e.g icon colors, sidebar items, etc.. :)

##### THEME OVERRIDE
#
overrides default theme sidebar, scrollbars and tab background based on theme scheme background
```json
"theme_agila_camouflage": true, 
```

overrides default theme sidebar and tab background only based on theme scheme background
```json
"theme_agila_camouflage_semi": true,
```

overrides all the theme_agila_* size settings; convenient for small laptops
```json
"theme_agila_nano_mode": true,
```

##### SIDEBAR COMPACT TREE STRUCTURE - NO INDENTATION
#
```json
"theme_agila_compact_sidebar": true,
```

##### SIDEBAR TREE SIZE (default: medium)
#
```json
"theme_agila_sidebar_mini": true,
"theme_agila_sidebar_xsmall": true,
"theme_agila_sidebar_small": true,
"theme_agila_sidebar_medium": true,
"theme_agila_sidebar_large": true,
```

##### SIDEBAR HEADING (default: theme-based color)
#
```json
"theme_agila_sidebar_heading_white": true,
"theme_agila_sidebar_heading_gray": true,
"theme_agila_sidebar_heading_lightblue": true,
"theme_agila_sidebar_heading_yellow": true,
"theme_agila_sidebar_heading_pink": true,
```

##### SIDEBAR ENTRY/ITEM FONT SIZE (default: 13)
#
```json
"theme_agila_sidebar_font_xsmall": true, //font-size: 11
"theme_agila_sidebar_font_small": true, //font-size: 12
"theme_agila_sidebar_font_big": true, //font-size: 14
```

##### SIDEBAR SELECTED ENTRY/ITEM (default: pink)
#
```json
"theme_agila_sidebar_selected_entry_white": true,
"theme_agila_sidebar_selected_entry_gray": true,
"theme_agila_sidebar_selected_entry_lightblue": true,
"theme_agila_sidebar_selected_entry_yellow": true,
"theme_agila_sidebar_selected_entry_pink": true,
```

##### SIDEBAR LIGHT ICONS (default: dark)
#
```json
"theme_agila_sidebar_light_icons": true,
```

##### SIDEBAR FOLDER PLUS/MINUS ICONS
#
if a plus/minus icon is preferred beside folder icon
```json
"theme_agila_sidebar_plus_minus": true,
```

##### COMPACT TAB - REDUCED TAB HEIGHT
#
```json
"theme_agila_compact_tab": true,
```

##### ACTIVE TAB - TEXT COLOR (default: pink)
#
```json
"theme_agila_active_tab_entry_white": true,
"theme_agila_active_tab_entry_gray": true,
"theme_agila_active_tab_entry_lightblue": true,
"theme_agila_active_tab_entry_yellow": true,
"theme_agila_active_tab_entry_pink": true,
```

##### MODIFIED TAB - ICON MARKER COLOR (default: light blue)
#
```json
"theme_agila_modified_tab_marker_white": true,
"theme_agila_modified_tab_marker_gray": true,
"theme_agila_modified_tab_marker_lightblue": true,
"theme_agila_modified_tab_marker_yellow": true,
"theme_agila_modified_tab_marker_pink": true,
```

##### AUTOCOMPLETE - KEYWORD COLOR (default: white)
#
```json
"theme_agila_auto_complete_white": true,
"theme_agila_auto_complete_gray": true,
"theme_agila_auto_complete_lightblue": true,
"theme_agila_auto_complete_yellow": true,
"theme_agila_auto_complete_pink": true,
```

##### SCROLLBAR COLORS (default: theme based color)
#
```json
"theme_agila_vertical_scrollbar_white": true,
"theme_agila_horizontal_scrollbar_white": true,

"theme_agila_vertical_scrollbar_gray": true,
"theme_agila_horizontal_scrollbar_gray": true,

"theme_agila_vertical_scrollbar_lightblue": true,
"theme_agila_horizontal_scrollbar_lightblue": true,

"theme_agila_vertical_scrollbar_yellow": true,
"theme_agila_horizontal_scrollbar_yellow": true,

"theme_agila_vertical_scrollbar_pink": true,
"theme_agila_horizontal_scrollbar_pink": true,
```

##### SCROLLBAR THINNESS (default: 4)
#
```json
"theme_agila_vertical_scrollbar_thickest": true,   //width: 6
"theme_agila_horizontal_scrollbar_thickest": true,

"theme_agila_vertical_scrollbar_thicker": true,   //width: 5
"theme_agila_horizontal_scrollbar_thicker": true,

"theme_agila_vertical_scrollbar_thinner": true,    //width: 3
"theme_agila_horizontal_scrollbar_thinner": true,

"theme_agila_vertical_scrollbar_thinnest": true,   //width: 2
"theme_agila_horizontal_scrollbar_thinnest": true,

"theme_agila_vertical_scrollbar_invisible": true,  //width:  0
"theme_agila_horizontal_scrollbar_invisible": true,
```
#
---
### My Sublime Settings :p
##### **https://gist.github.com/arvi/b71cd26b7a20944a7d53607213d56c20**
#
#
---
### Ports
- [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=whtsky.agila-theme) by whtsky 
---
### Thanks to
- [Preap Theme](https://packagecontrol.io/packages/Preap) - UI inspiration and .sublime-theme source code :)
- [Spacegray Theme](http://kkga.github.io/spacegray) - UI inspiration and .sublime-theme source code :)
- [amCoder Theme](https://packagecontrol.io/packages/Theme%20-%20amCoder) - UI inspiration and .sublime-theme source code :)
- [Neka Theme](https://packagecontrol.io/packages/Neka%20Theme) - Icons
- [Oceanic Next Color Scheme](https://packagecontrol.io/packages/Oceanic%20Next%20Color%20Scheme) - where Default and Classic theme color scheme are based
- [Solarized Color Scheme](https://packagecontrol.io/packages/Solarized%20Color%20Scheme) - where Light theme color scheme is based
- [Dracula Color Scheme](https://draculatheme.com/sublime/)
- [Monokai Extended Color Scheme](https://github.com/jonschlinkert/sublime-monokai-extended)
- [Monocyanide Color Scheme](https://github.com/Centril/sublime-monocyanide-colorscheme)
- [Cobalt2 Scheme](https://github.com/wesbos/cobalt2)
- [Colorhexa](http://www.colorhexa.com/) - color combinations
- `meteor create --sample todos` - screenshot code snippet :p
- Contributor(s): [davidmatas](https://github.com/davidmatas), [Cldfire](https://github.com/Cldfire), [polyvertex](https://github.com/polyvertex), [mikedcook](https://github.com/mikedcook), [kcmr](https://github.com/kcmr)

---
### Fun Experiments :p
Have a color combination in mind or perhaps you also want to try and create your own? Check the *`Agila.sublime-theme`* source code... I made it super easy for anyone to customize a sublime UI theme through my extensive comments. :p Enjoy! :)
