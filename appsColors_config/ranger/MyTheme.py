#File : ~/.config/ranger/colorscheme/MyTheme.py

# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *


class Default(ColorScheme):
    progress_bar_color = red

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                bg = blue
            if context.border:
                fg = default
            if context.media:
                if context.image:
                    fg = green
                else:
                    fg = magenta
            if context.container:
                fg = blue
            if context.directory:
                attr |= bold
                fg = red
            elif context.executable and not \
                    any((context.media, context.container,
                        context.fifo, context.socket)):
                attr |= bold
                fg = yellow
            if context.socket:
                fg = magenta
                attr |= bold
            if context.fifo or context.device:
                fg = green
                if context.device:
                    attr |= bold
            if context.link:
                fg = context.good and cyan or magenta
            if context.tag_marker and not context.selected:
                attr |= bold
                if fg in (blue, magenta):
                    fg = white
                else:
                    fg = blue
            if not context.selected and (context.cut or context.copied):
                fg = black
                attr |= bold
            if context.main_column:
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    fg = green
            if context.badinfo:
                if attr & reverse:
                    bg = magenta
                else:
                    fg = magenta

            if context.inactive_pane:
                fg = cyan

        elif context.in_titlebar:
            attr |= bold
            if context.hostname:
                fg = context.bad and blue or yellow
            elif context.directory:
                fg = red
            elif context.tab:
                if context.good:
                    bg = yellow
            elif context.link:
                fg = cyan

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = cyan
                elif context.bad:
                    fg = magenta
            if context.marked:
                attr |= bold | reverse
                fg = green
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = blue
            if context.loaded:
                bg = self.progress_bar_color
            if context.vcsinfo:
                fg = red
                attr &= ~bold
            if context.vcscommit:
                fg = green
                attr &= ~bold
            if context.vcsdate:
                fg = cyan
                attr &= ~bold

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = red

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color

        if context.vcsfile and not context.selected:
            attr &= ~bold
            if context.vcsconflict:
                fg = magenta
            elif context.vcschanged:
                fg = blue
            elif context.vcsunknown:
                fg = blue
            elif context.vcsstaged:
                fg = yellow
            elif context.vcssync:
                fg = yellow
            elif context.vcsignoblue:
                fg = default

        elif context.vcsremote and not context.selected:
            attr &= ~bold
            if context.vcssync or context.vcsnone:
                fg = yellow
            elif context.vcsbehind:
                fg = blue
            elif context.vcsahead:
                fg = red
            elif context.vcsdiverged:
                fg = magenta
            elif context.vcsunknown:
                fg = blue

        return fg, bg, attr