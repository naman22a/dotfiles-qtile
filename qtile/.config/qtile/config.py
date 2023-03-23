import os
import subprocess
from typing import List

from libqtile import bar, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
terminal = "alacritty"
browser = "firefox"
file_manger = "nautilus"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key(
        [mod, "shift"],
        "q",
        lazy.spawn("shutdown now"),
        desc="Shutdown Qtile",
    ),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="toggle fullscreen"),
    Key([mod], "b", lazy.spawn(browser)),
    Key([mod], "e", lazy.spawn(file_manger)),
    # Rofi
    Key([mod, "shift"], "semicolon", lazy.spawn("rofi -show emoji -modi emoji")),
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget",
    ),
    Key([mod], "Right", lazy.screen.next_group()),
    Key([mod], "Left", lazy.screen.prev_group()),
    # Volume Buttons
    Key([mod], "m", lazy.spawn("alacritty -e alsamixer")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 -q set Master 2dB+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 -q set Master 2dB-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -c 0 -q set Master toggle")),
    # PowerOff / Restart
    Key([mod], "p", lazy.spawn("sh /home/naman/.scripts/powermenu")),
    # Scrrenshot
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui")),
    Key(
        [mod],
        "s",
        lazy.spawn("flameshot full --clipboard --path ~/Pictures/Screenshots"),
    ),
    # Brightness
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brillo -A 5"),
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brillo -U 5"),
    ),
]

groups = []

group_labels = ["◉", "◉", "◉", "◉", "◉", "◉"]
group_names = [str(i) for i in range(1, len(group_labels) + 1)]

for i in range(len(group_names)):
    group = Group(name=group_names[i], layout="MonadTall", label=group_labels[i])

    groups.append(group)

    keys.extend(
        [
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
        ]
    )

colors = {
    "Rosewater": "#f5e0dc",
    "Flamingo": "#f2cdcd",
    "Pink": "#f5c2e7",
    "Mauve": "#cba6f7",
    "Red": "#f38ba8",
    "Maroon": "#eba0ac",
    "Peach": "#fab387",
    "Yellow": "#f9e2af",
    "Green": "#a6e3a1",
    "Teal": "#94e2d5",
    "Sky": "#89dceb",
    "Sapphire": "#74c7ec",
    "Blue": "#89b4fa",
    "Lavender": "#b4befe",
    "Text": "#cdd6f4",
    "Subtext1": "#bac2de",
    "Subtext0": "#a6adc8",
    "Overlay2": "#9399b2",
    "Overlay1": "#7f849c",
    "Overlay0": "#6c7086",
    "Surface2": "#585b70",
    "Surface1": "#45475a",
    "Surface0": "#313244",
    "Base": "#1e1e2e",
    "Mantle": "#181825",
    "Crust": "#11111b",
    "Transparent": "#00000000",
}

layout_theme = {
    "border_width": 2,
    "border_focus": colors["Red"],
    "margin": 15,
}


layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(border_focus=colors["Sapphire"], border_width=4),
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.RatioTile(**layout_theme),
    # layout.TreeTab(**layout_theme),
]

widget_defaults = dict(
    font="Mononoki Nerd Font",
    fontsize=17,
    padding=10,
)

extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=3),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=21,
                    foreground=colors["Mantle"],
                    background=colors["Transparent"],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors["Blue"],
                    background=colors["Mantle"],
                ),
                widget.GroupBox(
                    rounded=False,
                    active=colors["Text"],
                    inactive=colors["Surface1"],
                    highlight_method="line",
                    this_current_screen_border=colors["Red"],
                    fontsize=18,
                    background=colors["Mantle"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=21,
                    foreground=colors["Mantle"],
                    background=colors["Transparent"],
                ),
                widget.Spacer(length=bar.STRETCH),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=25,
                    foreground=colors["Mantle"],
                    background=colors["Transparent"],
                ),
                widget.TextBox(
                    text="󱑍",
                    foreground=colors["Red"],
                    background=colors["Mantle"],
                ),
                widget.Clock(
                    margin=0,
                    padding=10,
                    format="%I:%M %p",
                    background=colors["Mantle"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=25,
                    foreground=colors["Mantle"],
                    background=colors["Transparent"],
                ),
                widget.Spacer(length=bar.STRETCH),
                widget.Systray(padding=5),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=25,
                    foreground=colors["Mantle"],
                    background=colors["Transparent"],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors["Green"],
                    background=colors["Mantle"],
                ),
                widget.Memory(
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(terminal + " -e htop")
                    },
                    format="{MemUsed: .0f}{mm}",
                    measure_mem="G",
                    padding=0,
                    background=colors["Mantle"],
                    decorations=[
                        BorderDecoration(
                            colour=colors["Text"],
                            border_width=[0, 0, 2, 0],
                            padding_x=5,
                            padding_y=None,
                        )
                    ],
                ),
                widget.Battery(
                    charge_char="󰂄",
                    discharge_char="󰂀",
                    format="{char}{percent: 1.0%}",
                    update_interval=0.1,
                    background=colors["Mantle"],
                ),
                widget.TextBox(
                    text="󰕾",
                    padding=3,
                    foreground=colors["Blue"],
                    background=colors["Mantle"],
                ),
                widget.Volume(
                    fmt="{}",
                    channel="Master",
                    background=colors["Mantle"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    margin=10,
                    fontsize=21,
                    foreground=colors["Mantle"],
                    background=colors["Transparent"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=21,
                    foreground=colors["Mantle"],
                    background=colors["Transparent"],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors["Peach"],
                    background=colors["Mantle"],
                ),
                widget.Wlan(
                    format="{essid}",
                    background=colors["Mantle"],
                    interface="wlp3s0",
                    update_interval=0.1,
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            "sh /home/naman/.scripts/wifimenu"
                        )
                    },
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=21,
                    foreground=colors["Mantle"],
                    background=colors["Transparent"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=21,
                    foreground=colors["Mantle"],
                    background=colors["Transparent"],
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    foreground=colors["Lavender"],
                    background=colors["Mantle"],
                    padding=7,
                    scale=0.7,
                ),
                widget.CurrentLayout(
                    foreground=colors["Flamingo"],
                    background=colors["Mantle"],
                    padding=7,
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=21,
                    foreground=colors["Mantle"],
                    background=colors["Transparent"],
                ),
            ],
            24,
            background=colors["Transparent"],
        )
    )
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="kdenlive"),  # kdenlive
        Match(wm_class="gimp"),  # gimp
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# startup apps


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
