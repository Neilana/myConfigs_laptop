#!/bin/bash

# 1. i3 configuration
cp i3_config/config ~/.config/i3/
cp i3_config/wallpaper.jpg ~/.config/i3/

cp i3_config/i3blocks/i3blocks.conf /usr/lib/i3blocks/
cp i3_config/i3blocks/myBlocks/* /usr/lib/i3blocks/myBlocks/

# 2. Startup configs
cp startup_config/.xinitrc ~/

# 3. Color schemes (themes)
# xterm colors
cp appsColors_config/xterm/.Xresources ~/
xrdb -load ~/.Xresources

# sublime text 3 theme
cp appsColors_config/sublime3/MyTheme.tmTheme ~/.config/sublime-text-3/Packages/Colorsublime-Themes/

# ranger theme
cp appsColors_config/ranger/MyTheme.py ~/.config/ranger/colorschemes/

# cmus theme (nned to "colorscheme Mytheme2" in cmus to refresh theme (even if the theme is the same))
cp appsColors_config/cmus/MyTheme2.theme /usr/share/cmus/
