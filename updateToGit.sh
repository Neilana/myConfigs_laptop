#!/bin/bash

# 1. i3 configuration
cp ~/.config/i3/* i3_config/

cp /usr/lib/i3blocks/i3blocks.conf i3_config/i3blocks/
cp /usr/lib/i3blocks/myBlocks/* i3_config/i3blocks/myBlocks

# 2. Startup configs
cp ~/.xinitrc startup_config/
cp ~/.bashrc startup_config/
cp ~/.vimrc startup_config/
cp ~/.bash_profile startup_config/

# 3. Color schemes (themes)
# xterm colors
cp ~/.Xresources appsColors_config/xterm/

# sublime text 3 theme
cp ~/.config/sublime-text-3/Packages/Colorsublime-Themes/MyTheme.tmTheme appsColors_config/sublime3

# ranger theme
cp ~/.config/ranger/colorschemes/MyTheme.py appsColors_config/ranger/

# cmus theme
cp /usr/share/cmus/MyTheme2.theme appsColors_config/cmus/

#4 keyboard
#
