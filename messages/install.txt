# Agila Theme
##### A Sublime Text 3 UI Theme
Couldn't find a theme I really dig, so I tried to make my own theme based on all the things/elements I like from wonderful themes I've used before. :)

***

## Screenshots
*Current font settings in screenshots:
Font face: [__Inconsolata__](https://www.google.com/fonts/specimen/Inconsolata) | Font size: 22*

#### Agila Theme
![Screenshot](https://www.dropbox.com/s/jt3choxq6b583t7/Agila%20Theme.png?raw=1)

#### Agila Classic Theme
![Screenshot](https://www.dropbox.com/s/xlg43vr2ikxogch/Agila%20Classic%20Theme.png?raw=1)

#### Agila Light Theme
![Screenshot](https://www.dropbox.com/s/tmjpeas5iuvotbd/Agila%20Light%20Theme.png?raw=1)

---

### How to Install

##### *Chill* way
via [Package Control](https://packagecontrol.io/), where Agila is listed as *`Agila Theme`*.

1. Open Command Palette using menu item *`Tools -> Command Palette...`*
2. Choose `Package Control: Install Package`
3. Find *`Agila Theme`* and hit *`Enter`*

##### *Woooo* way
via installing the theme manually.

1. [Download the latest release .zip](https://github.com/arvi/Agila-Theme/releases)
2. Unzip and rename folder to *`Agila Theme`*.
3. Move *`Agila Theme`* folder inside the Packages directory (*`Preferences > Browse packages...`*)

---

### How to Activate Theme
via User Preferences file (*`Sublime Text -> Preferences -> Settings - User`*). After setting up,
don't forget to **restart Sublime Text Editor** for changes to take effect.

##### Default theme
#
```json
"theme": "Agila.sublime-theme",
"color_scheme": "Packages/Agila Theme/Agila Oceanic Next.tmTheme",
```

##### Classic theme
#
```json
"theme": "Agila Classic.sublime-theme",
"color_scheme": "Packages/Agila Theme/Agila Classic Oceanic Next.tmTheme",
```

##### Light theme
#
```json
"theme": "Agila Light.sublime-theme",
"color_scheme": "Packages/Agila Theme/Agila Light Solarized.tmTheme",
```
#

---

### Settings
I've made some UI parts customizable e.g icon colors, sidebar items, etc.. :)
###### SIDEBAR SIZE (default: medium)
#
```json
"theme_agila_sidebar_small": true,
"theme_agila_sidebar_medium": true,
"theme_agila_sidebar_large": true,
```

###### SIDEBAR ENTRY/ITEM FONT SIZE (if not set, will default to font size: 13)
#
```json
"theme_agila_sidebar_font_xsmall": true, //font-size: 11
"theme_agila_sidebar_font_small": true, //font-size: 12
"theme_agila_sidebar_font_big": true, //font-size: 14
```

###### SIDEBAR SELECTED ENTRY/ITEM (default: pink)
#
```json
"theme_agila_sidebar_selected_entry_white": true,
"theme_agila_sidebar_selected_entry_gray": true,
"theme_agila_sidebar_selected_entry_lightblue": true,
"theme_agila_sidebar_selected_entry_yellow": true,
"theme_agila_sidebar_selected_entry_pink": true,
```

###### MODIFIED TAB - ICON MARKER COLOR (default: light blue)
#
```json
"theme_agila_modified_tab_marker_white": true,
"theme_agila_modified_tab_marker_gray": true,
"theme_agila_modified_tab_marker_lightblue": true,
"theme_agila_modified_tab_marker_yellow": true,
"theme_agila_modified_tab_marker_pink": true,
```

###### SCROLLBAR COLORS
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

###### SCROLLBAR THINNESS (if not set, will default to thin:3)
#
```json
"theme_agila_vertical_scrollbar_thinner": true,    //thin:2
"theme_agila_horizontal_scrollbar_thinner": true,

"theme_agila_vertical_scrollbar_thinnest": true,   //thin:1
"theme_agila_horizontal_scrollbar_thinnest": true,

"theme_agila_vertical_scrollbar_invisible": true,  //thin: 0
"theme_agila_horizontal_scrollbar_invisible": true,
```
#
---
### Thanks to
- [Preap Theme](https://packagecontrol.io/packages/Preap) - UI inspiration and .sublime-theme source code :)
- [Spacegray Theme](http://kkga.github.io/spacegray) - UI inspiration and .sublime-theme source code :)
- [amCoder Theme](https://packagecontrol.io/packages/Theme%20-%20amCoder) - UI inspiration and .sublime-theme source code :)
- [Neka Theme](https://packagecontrol.io/packages/Neka%20Theme) - Icons
- [Oceanic Next Color Scheme](https://packagecontrol.io/packages/Oceanic%20Next%20Color%20Scheme) - where Default and Classic theme color scheme are based
- [Solarized Color Scheme](https://packagecontrol.io/packages/Solarized%20Color%20Scheme) - where Light theme color scheme is based
- [Colorhexa](http://www.colorhexa.com/) - color combinations
- `meteor create --sample todos` - screenshot code snippet :p

---
### Fun Experiments :p
Have a color combination in mind or perhaps you also want to try and create your own? Check the *`Agila.sublime-theme`* source code... I made it super easy for anyone to customize a sublime UI theme through my extensive comments. :p Enjoy! :)