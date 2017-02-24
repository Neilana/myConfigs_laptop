#!/bin/bash

# 1. i3 configuration
mkdir -p ~/.config/i3/
cp i3_config/config/* ~/.config/i3/

mkdir -p /usr/lib/i3blocks/myBlocks
cp i3_config/i3blocks/i3blocks.conf /usr/lib/i3blocks/
cp i3_config/i3blocks/myBlocks/* /usr/lib/i3blocks/myBlocks/

mkdir -p ~/.fonts
cp i3_config/fonts/* ~/.fonts/

# 2. Startup configs
cp startup_config/* ~/

# 3. Color schemes (themes)
# xterm colors
cp appsColors_config/xterm/.Xresources ~/
xrdb -load ~/.Xresources

# sublime text 3 theme
mkdir -p ~/.config/sublime-text-3/Packages/Colorsublime-Themes/
cp appsColors_config/sublime3/MyTheme.tmTheme ~/.config/sublime-text-3/Packages/Colorsublime-Themes/

# ranger theme
mkdir -p  ~/.config/ranger/colorschemes/
cp appsColors_config/ranger/MyTheme.py ~/.config/ranger/colorschemes/

# cmus theme (nned to "colorscheme Mytheme2" in cmus to refresh theme (even if the theme is the same))
mkdir -p /usr/share/cmus/
cp appsColors_config/cmus/MyTheme2.theme /usr/share/cmus/
