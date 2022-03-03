# Agila Theme
#### A Sublime Text 3 UI Theme
***

### Changelog

##### Version 2.3.0 - CURRENT VERSION
* Added missing scopes for variable.function and message.error. Thanks to davidhcefx :)

##### Version 2.2.0
* Added support for title bar (introduced in Dev Build 3127). Thanks to kcmr :)

##### Version 2.1.0
* Added nano mode support (convenient for small laptops). Thanks to polyvertex :)
    ```json
        "theme_agila_nano_mode": true,
    ```

* Added sidebar plus/minus icons beside folder. Thanks to mikedcook :)
    ```json
        "theme_agila_sidebar_plus_minus": true,
    ```

* Added Visual Studio Agila Theme ported by whtsky :)
    - https://marketplace.visualstudio.com/items?itemName=whtsky.agila-theme

##### Version 2.0.0
* Added Markdown Support based on theme (prerequisite: Markdown Extended Sublime Package)
    - activated via skins package when you chose a specific skin
    - activated via Preferences > Settings - Syntax Specific (when you open a .md file)
* Modified Skins settings
    - added Markdown Extended settings
* Removed file extension preferences
    - https://github.com/arvi/Agila-Theme/issues/22
* Fixed Agila Monocyanide background color (toned-down a bit)
* Acknowledged fantastic Skins pull request from Cldfire in README contributors :)

##### Version 1.9.0
* Added two more sidebar tree options with "mini" as the smallest
(to save spacing for large projects)
    ```json
        "theme_agila_sidebar_mini":true,
        "theme_agila_sidebar_xsmall":true,
    ```
* Added Agila Cobalt Theme :)
    ```json
        "theme": "Agila Cobalt.sublime-theme",
        "color_scheme": "Packages/Agila Theme/Agila Cobalt.tmTheme",
    ```
* Fixed Agila Monocyanide Theme colors
* Fixed all theme's find panel selection colors to match the actual theme

##### Version 1.8.0
* Added active tab text color for easier identification (default: pink)
    ```json
        "theme_agila_active_tab_entry_white": true,
        "theme_agila_active_tab_entry_gray": true,
        "theme_agila_active_tab_entry_lightblue": true,
        "theme_agila_active_tab_entry_yellow": true,
        "theme_agila_active_tab_entry_pink": true,
    ```
* Added Agila Neon Theme :)
    ```json
        "theme": "Agila Neon.sublime-theme",
        "color_scheme": "Packages/Agila Theme/Agila Neon Monocyanide.tmTheme",
    ```
* Modified Monokai Extended and Light Solarized based on their latest repo changes

##### Version 1.7.0
* Modified Oceanic Color Scheme and Light Solarized based on their latest repo changes
    - You can now use Active Guide with these schemes, just add:
        ```json
            "indent_guide_options":
            [
                "draw_normal",
                "draw_active"
            ],
        ```
* Added other color schemes to Agila Family :)
    - Based on default Oceanic Next Color Scheme
        ```json
            "theme": "Agila Origin.sublime-theme",
            "color_scheme": "Packages/Agila Theme/Agila Origin Oceanic Next.tmTheme",
        ```
    - Based on Dracula Color Scheme
        ```json
            "theme": "Agila Dracula.sublime-theme",
            "color_scheme": "Packages/Agila Theme/Agila Dracula.tmTheme",
        ```
    - Based on Monokai Extended Scheme
        ```json
            "theme": "Agila Monokai.sublime-theme",
            "color_scheme": "Packages/Agila Theme/Agila Monokai Extended.tmTheme",
        ```
* Added theme override options
    - overrides default theme sidebar, scrollbars and tab background based on theme scheme background
        ```json
            "theme_agila_camouflage": true,
        ```
    - overrides default theme sidebar and tab background only based on theme scheme background
        ```json
            "theme_agila_camouflage_semi": true,
        ```
* Modified scrollbar thinness options and default
    - default changed from width: 3 --> width: 4
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

##### Version 1.6.0
* Fixed code completion and quick panel selection and hover state highlight
* Fixed sidebar tree structure (major UI changes)
* Added sidebar tree structure compact option (no parent-child folder indentation)
    ```json
        "theme_agila_compact_sidebar": true,
    ```
* Added sidebar file icons - lighter shade option
    ```json
        "theme_agila_sidebar_light_icons": true,
    ```

##### Version 1.5.0
* Fixed selection highlight
* Added code completion and quick panel color options
    ```json
        "theme_agila_auto_complete_white": true,
        "theme_agila_auto_complete_gray": true,
        "theme_agila_auto_complete_lightblue": true,
        "theme_agila_auto_complete_yellow": true,
        "theme_agila_auto_complete_pink": true,
    ```

##### Version 1.4.0
* Added sidebar heading color options - thanks to [davidmatas](https://github.com/davidmatas)
    ```json
        "theme_agila_sidebar_heading_white": true,
        "theme_agila_sidebar_heading_gray": true,
        "theme_agila_sidebar_heading_lightblue": true,
        "theme_agila_sidebar_heading_yellow": true,
        "theme_agila_sidebar_heading_pink": true,
    ```

##### Version 1.3.0
* Reduced default tab height
* Added tab height compact option (smaller than the default tab height)
    ```json
        "theme_agila_compact_tab": true
    ```
* Modified default scrollbars color: distraction-free color choice based on theme

##### Version 1.2.0
* Fixed tab element font size and dirty marker tint issues seen in a Windows machine.

##### Version 1.1.0
* Fixed Error Loading Scheme path error experienced during installation via Package Control