# Copyright original theme © 2021 rdbende <rdbende@gmail.com>
# Copyright russian-spring © 2022 Mons <mons@mons.ws>

source theme/light.tcl

option add *tearOff 0

proc set_theme {mode} {
	if {$mode == "light"} {
		ttk::style theme use "russian-spring-light"

		array set colors {
		    -fg             "#20202c"
		    -bg             "#e8eded"
		    -disabledfg     "#a0a0a0"
		    -selectfg       "#f6f8f8"
		    -selectbg       "#2f60d8"
		}

        ttk::style configure . \
            -background $colors(-bg) \
            -foreground $colors(-fg) \
            -troughcolor $colors(-bg) \
            -focuscolor $colors(-selectbg) \
            -selectbackground $colors(-selectbg) \
            -selectforeground $colors(-selectfg) \
            -insertwidth 1 \
            -insertcolor $colors(-fg) \
            -fieldbackground $colors(-selectbg) \
            -font {"Segoe Ui" 10} \
            -borderwidth 0 \
            -relief flat

        tk_setPalette background [ttk::style lookup . -background] \
            foreground [ttk::style lookup . -foreground] \
            highlightColor [ttk::style lookup . -focuscolor] \
            selectBackground [ttk::style lookup . -selectbackground] \
            selectForeground [ttk::style lookup . -selectforeground] \
            activeBackground [ttk::style lookup . -selectbackground] \
            activeForeground [ttk::style lookup . -selectforeground]
        
        ttk::style map . -foreground [list disabled $colors(-disabledfg)]

        option add *font [ttk::style lookup . -font]
        option add *Treeview.show tree
        option add *Menu.selectcolor $colors(-fg)
	}
}
