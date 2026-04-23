################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Controls
################################################################################
default persistent.actual_controls = dict(
    dismiss = "K_SPACE",
    game_menu = "K_ESCAPE",
    toggle_skip = "K_TAB",
    skip = "K_LCTRL",
    rollback = "K_PAGEUP",
    rollforward = "K_PAGEDOWN",
    hide_windows = "K_h",
    screenshot = "K_s",
    self_voicing = "K_v",
    accessibility = "K_a"
)

init python:
    control_names = dict(
        # Mouse


        # Keys
        K_BACKSPACE = "Backspace",
        K_TAB = "Tab",
        K_CLEAR = "Clear",
        K_RETURN = "Return",
        K_PAUSE = "Pause",
        K_ESCAPE = "Escape",
        K_SPACE = "Space",
        K_EXCLAIM = "Exclaim",
        K_QUOTEDBL = "Quotedbl",
        K_HASH = "Hash",
        K_DOLLAR = "Dollar",
        K_AMPERSAND = "Ampersand",
        K_QUOTE = "Quote",
        K_LEFTPAREN = "Left Oarenthesis",
        K_RIGHTPAREN = "Right Oarenthesis",
        K_ASTERISK = "Asterisk",
        K_PLUS = "Plus Sign",
        K_COMMA = "Comma",
        K_MINUS = "Minus Sign",
        K_PERIOD = "Period",
        K_SLASH = "Forward Slash",
        K_0 = "0",
        K_1 = "1",
        K_2 = "2",
        K_3 = "3",
        K_4 = "4",
        K_5 = "5",
        K_6 = "6",
        K_7 = "7",
        K_8 = "8",
        K_9 = "9",
        K_COLON = "Colon",
        K_SEMICOLON = "Semicolon",
        K_LESS = "Less-than Sign",
        K_EQUALS = "Equals Sign",
        K_GREATER = "Greater-than Sign",
        K_QUESTION = "Question Mark",
        K_AT = "At",
        K_LEFTBRACKET = "Left Bracket",
        K_BACKSLASH = "Backslash",
        K_RIGHTBRACKET = "Right Bracket",
        K_CARET = "Caret",
        K_UNDERSCORE = "Underscore",
        K_BACKQUOTE = "Grave",
        K_a = "A",
        K_b = "B",
        K_c = "C",
        K_d = "D",
        K_e = "E",
        K_f = "F",
        K_g = "G",
        K_h = "H",
        K_i = "I",
        K_j = "J",
        K_k = "K",
        K_l = "L",
        K_m = "M",
        K_n = "N",
        K_o = "O",
        K_p = "P",
        K_q = "Q",
        K_r = "R",
        K_s = "S",
        K_t = "T",
        K_u = "U",
        K_v = "V",
        K_w = "W",
        K_x = "X",
        K_y = "Y",
        K_z = "Z",
        K_DELETE = "Delete",
        K_KP0 = "Keypad 0",
        K_KP1 = "Keypad 1",
        K_KP2 = "Keypad 2",
        K_KP3 = "Keypad 3",
        K_KP4 = "Keypad 4",
        K_KP5 = "Keypad 5",
        K_KP6 = "Keypad 6",
        K_KP7 = "Keypad 7",
        K_KP8 = "Keypad 8",
        K_KP9 = "Keypad 9",
        K_KP_PERIOD = "Keypad Period",
        K_KP_DIVIDE = "Keypad Divide",
        K_KP_MULTIPLY = "Keypad Multiply",
        K_KP_MINUS = "Keypad Minus",
        K_KP_PLUS = "Keypad Plus",
        K_KP_ENTER = "Keypad Enter",
        K_KP_EQUALS = "Keypad Equals",
        K_UP = "Up Arrow",
        K_DOWN = "Down Arrow",
        K_RIGHT = "Right Arrow",
        K_LEFT = "Left Arrow",
        K_INSERT = "Insert",
        K_HOME = "Home",
        K_END = "End",
        K_PAGEUP = "Page Up",
        K_PAGEDOWN = "Page Down",
        K_F1 = "F1",
        K_F2 = "F2",
        K_F3 = "F3",
        K_F4 = "F4",
        K_F5 = "F5",
        K_F6 = "F6",
        K_F7 = "F7",
        K_F8 = "F8",
        K_F9 = "F9",
        K_F10 = "F10",
        K_F11 = "F11",
        K_F12 = "F12",
        K_F13 = "F13",
        K_F14 = "F14",
        K_F15 = "F15",
        K_NUMLOCK = "Numlock",
        K_CAPSLOCK = "Capslock",
        K_SCROLLOCK = "Scrollock",
        K_RSHIFT = "Right Shift",
        K_LSHIFT = "Left Shift",
        K_RCTRL = "Right Control",
        K_LCTRL = "Left Control",
        K_RALT = "Right Alt",
        K_LALT = "Left Alt",
        K_RMETA = "Right Meta",
        K_LMETA = "Left Meta",
        #K_LSUPER = "Left Windows key",
        #K_RSUPER = "Right Windows key",
        #K_MODE = "Mode shift",
        #K_HELP = "Help",
        #K_PRINT = "Print screen",
        #K_SYSREQ = "Sysrq",
        #K_BREAK = "Break",
        #K_MENU = "Menu",
        #K_POWER = "Power",
        #K_EURO = "Euro"
    )

    permitted_controls = list(control_names.keys())

    action_names = dict(
        dismiss = "Advance dialogue",
        game_menu = "Game menu",
        toggle_skip = "Toggle skip",
        skip = "Skip",
        rollback = "Roll back to earlier dialogue",
        rollforward = "Roll forward to later dialogue",
        hide_windows = "Hide user interface",
        screenshot = "Screenshot",
        self_voicing = "Toggle self-voicing",
        accessibility = "Accessibility menu"
    )

    actual_controls = persistent.actual_controls

    def set_control(remap_action, remap_key):
        config.keymap[remap_action].clear()
        config.keymap[remap_action].append(remap_key)
        persistent.actual_controls[remap_action] = remap_key
        renpy.save_persistent()

        # Apply mouse controls
        if(remap_action == "rollback"):
            config.keymap[remap_action].append("mousedown_4")
        elif(remap_action == "game_menu"):
            config.keymap[remap_action].append("mouseup_3")
        elif(remap_action == "hide_windows"):
            config.keymap[remap_action].append("mouseup_2")
        elif(remap_action == "rollforward"):
            config.keymap[remap_action].append("mousedown_5")
        elif(remap_action == "dismiss"):
            config.keymap[remap_action].append("mouseup_1")
        

    for remap_action in list(actual_controls.keys()):
        set_control(remap_action, actual_controls[remap_action])

    # Action version of set_control
    @renpy.pure
    class SetControl(Action, DictEquality):
        def __init__(self, remap_action, remap_key):
            self.remap_action = remap_action
            self.remap_key = remap_key

        def __call__(self):
            set_control(self.remap_action, self.remap_key)
            global current_remap_action
            current_remap_action = None
            renpy.clear_keymap_cache() # Clear keymap cache, so new config.keymap can take effect
            renpy.restart_interaction() # Probably not necessary. Keeping just in case. Remove if causes problems.

screen controls_remap(remap_action):
    zorder 99999
    modal True

    for remap_key in permitted_controls:
        key [remap_key]:
            action [SetControl(remap_action, remap_key), Hide("controls_remap")]

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    #font "gui/fonts/Lexend-Medium.ttf"
    hover_underline True
    color "#d73a1b"

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")
    hover_sound "sfx/item_hover.wav"
    activate_sound "sfx/item_click.wav"

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    hover_sound "sfx/item_hover.wav"
    activate_sound "sfx/item_click.wav"

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    hover_sound "sfx/item_hover.wav"
    activate_sound "sfx/item_click.wav"

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    hover_sound "sfx/item_hover.wav"
    activate_sound "sfx/item_click.wav"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
    hover_sound "sfx/item_hover.wav"
    activate_sound "sfx/item_click.wav"


style frame:
    padding gui.frame_borders.padding


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

# Assuming 60 FPS, 1 frame of animation is equivalent to 1/60=0.01667 seconds.
# Since this animation is going to be *super* quick, I'm going to build it by multiplying the amount of seconds for 1 frame by the number of frames I want.

transform say_fade:
    alpha 0.0
    zoom 0.9

    parallel:
        linear (0.01667 * 4) alpha 1.0
    parallel:
        linear (0.01667 * 4) zoom 1.0
    
    on hide:
        parallel:
            linear (0.01667 * 4) alpha 0.0
        parallel:
            linear (0.01667 * 4) zoom 0.9

transform who_angled:
    rotate 1.1

transform what_angled:
    rotate 0.9

transform who_angled_left:
    rotate -1.1

transform what_angled_left:
    rotate -0.9

transform NullTransform:
    pass

screen say(who, what, who_transform=who_angled, what_transform=what_angled):
    style_prefix "say"

    # Only show window if text is set.
    if what:
        window:
            background "gui/dialogue_box.png"
            xoffset 750
            yoffset 800
            left_padding 191
            right_padding 50

            at say_fade
            id "window"

            hbox:
                id "hbox"

                if who is not None:
                    frame:
                        padding (0, 0, 0, 0)

                        text who id "who" at who_transform
                elif persistent.dialogue_position != "modern":
                    # Provides the same spacing as the "who" text for the old, clean text system
                    frame:
                        padding (0, 0, 0, 0)

                        text "" id "who" at who_transform

                frame:
                    xfill True
                    padding (0, 0, 0, 0)
                    
                    text what id "what" at what_transform

init python:
    DEFAULT_YOFFSET = 800

    CHARACTER_COLORS = {
        "Amy": "#18336a",
        "Chloe": "#632566",
        "None": "#2f2b2b",
    }

    config.character_id_prefixes.append("hbox")
    
    def say_arguments_callback(char, *args, **kwargs):
        if persistent.dialogue_position == "clean-top" or persistent.dialogue_position == "clean-bottom":
            kwargs["window_background"] = None

            col = CHARACTER_COLORS[str(char)]

            kwargs["window_xalign"] = 0.5
            kwargs["window_yalign"] = 0.0
            kwargs["window_xoffset"] = 0
            kwargs["window_yoffset"] = 0
            kwargs["window_left_padding"] = 0
            kwargs["window_right_padding"] = 0

            kwargs["hbox_yoffset"] = 48
            kwargs["hbox_spacing"] = 0
            kwargs["hbox_box_wrap_spacing"] = 4
            kwargs["hbox_box_wrap"] = True
            kwargs["hbox_box_align"] = 0.5
            kwargs["hbox_yanchor"] = 0.0

            kwargs["who_outlines"] = [(2, col, 2, 2), (2, col, 1, 1), (2, col, 0, 0)]
            kwargs["what_outlines"] = [(2, col, 2, 2), (2, col, 1, 1), (2, col, 0, 0)]
            kwargs["show_who_transform"] = NullTransform
            kwargs["show_what_transform"] = NullTransform

            kwargs["who_xalign"] = 0.5
            kwargs["who_textalign"] = 0.5
            kwargs["who_size"] = 24
            kwargs["who_yalign"] = 0.0

            kwargs["what_xalign"] = 0.5
            kwargs["what_textalign"] = 0.5
            kwargs["what_yalign"] = 0.0
            kwargs["what_yoffset"] = 0

            if persistent.dialogue_position == "clean-bottom":
                kwargs["window_yalign"] = 1.0
                kwargs["hbox_yoffset"] = -48

            return args, kwargs

        # Select new textbox to use
        if("textbox" in kwargs):
            dtb.useTextbox(kwargs["textbox"])

        # Get textbox values
        box = dtb.getUsedTextbox()

        textbox_variant = kwargs["textbox_variant"] if "textbox_variant" in kwargs else box["type"]
        outline = kwargs["textbox_outline"] if "textbox_outline" in kwargs else box["outline"]

        kwargs["window_xoffset"] = (kwargs["window_xoffset"] if "window_xoffset" in kwargs else box["xoffset"])

        kwargs["window_yoffset"] = (kwargs["window_yoffset"] if "window_yoffset" in kwargs else box["yoffset"])
        if(kwargs["window_yoffset"] == None):
            kwargs["window_yoffset"] = DEFAULT_YOFFSET

        # Type
        if textbox_variant == "left" or textbox_variant == "left_down":
            if textbox_variant == "left_down":
                kwargs["window_background"] = "gui/dialogue_box_left_down.png"
            else:
                kwargs["window_background"] = "gui/dialogue_box_left.png"

            kwargs["window_left_padding"] = 50
            kwargs["window_right_padding"] = 191
            kwargs["window_xanchor"] = 1.0
            kwargs["window_yanchor"] = 0.0

            kwargs["hbox_box_reverse"] = True
            kwargs["show_who_transform"] = who_angled_left
            kwargs["show_what_transform"] = what_angled_left

        if textbox_variant == "narrator":
            kwargs["window_background"] = "gui/dialogue_box_narrator.png"
            kwargs["window_left_padding"] = 79
            kwargs["window_right_padding"] = 30
            kwargs["window_top_padding"] = 45
            kwargs["window_xsize"] = 1038
            kwargs["window_ysize"] = 229
            kwargs["window_xanchor"] = .5
            kwargs["window_yanchor"] = .5

            kwargs["show_who_transform"] = NullTransform
            kwargs["show_what_transform"] = NullTransform

        if textbox_variant == "narrator_small":
            if outline:
                kwargs["window_background"] = "gui/dialogue_box_narrator_small_outline.png"
            else:
                kwargs["window_background"] = "gui/dialogue_box_narrator_small.png"

            kwargs["window_left_padding"] = 60
            kwargs["window_right_padding"] = 60
            kwargs["window_xsize"] = 1038
            kwargs["window_ysize"] = 160
            kwargs["window_xanchor"] = .5
            kwargs["window_yanchor"] = .5

            kwargs["show_who_transform"] = NullTransform
            kwargs["show_what_transform"] = NullTransform
            kwargs["what_xalign"] = 0.5
            
        if textbox_variant == "centered":
            kwargs["window_background"] = None

            kwargs["window_xanchor"] = 0.5
            kwargs["window_yanchor"] = 0.5
            kwargs["window_xalign"] = 0.5
            kwargs["window_yalign"] = 0.5
            kwargs["window_xoffset"] = 0
            kwargs["window_yoffset"] = 0
            kwargs["window_left_padding"] = 0
            kwargs["window_right_padding"] = 0

            kwargs["hbox_yoffset"] = 48
            kwargs["hbox_spacing"] = 0
            kwargs["hbox_box_wrap_spacing"] = 4
            kwargs["hbox_box_wrap"] = True
            kwargs["hbox_box_align"] = 0.5
            kwargs["hbox_yanchor"] = 0.0

            kwargs["show_who_transform"] = NullTransform
            kwargs["show_what_transform"] = NullTransform

            kwargs["who_xalign"] = 0.5
            kwargs["who_textalign"] = 0.5
            kwargs["who_size"] = 24
            kwargs["who_yalign"] = 0.0

            kwargs["what_xalign"] = 0.5
            kwargs["what_textalign"] = 0.5
            kwargs["what_yalign"] = 0.0
            kwargs["what_yoffset"] = 0

        return args, kwargs

    class DynamicTextbox(store.object):
        def __init__(self):
            self.boxes = {}
            self.used = None
            
        def setTextbox(self, id, type, xoffset, yoffset, outline=False):
            self.boxes[id] = {
                "type": type,
                "xoffset": xoffset,
                "yoffset": yoffset,
                "outline": outline
            }

        def getTextbox(self, id):
            if id in self.boxes:
                return self.boxes[id]
            else:
                return {
                    "type": "right",
                    "xoffset": 750,
                    "yoffset": DEFAULT_YOFFSET,
                    "outline": False
                }
        
        def useTextbox(self, id):
            self.used = id

        def getUsedTextbox(self):
            return self.getTextbox(self.used)

define config.say_arguments_callback = say_arguments_callback

default dtb = DynamicTextbox()


style window is default
style say_window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style say_window:
    xalign 0.0
    ysize 165
    xsize 900

style say_hbox:
    xpos 0
    
    ypos 0
    yanchor 0.5

    xfill True
    yfill True
    box_align None
    box_wrap False
    spacing 32
    yoffset 150
    box_reverse False
    box_justify False
    
style say_label:
    properties gui.text_properties("name", accent=True)

    xalign 0.0
    xfill False

    ypos 0
    yanchor 0.5

    font "gui/fonts/Lexend-Black.ttf"
    size 32
    textalign 0.0

    adjust_spacing False

style say_dialogue:
    properties gui.text_properties("dialogue")

    xalign 0.0
    xfill True

    ypos 0.0
    yanchor 0.5
    yoffset 5

    font "gui/fonts/Lexend-Bold.ttf"
    size 28
    textalign 0.0

    adjust_spacing False

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.


screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 1.0
            yalign 1.0
            yoffset -5

            textbutton _("Back") action Rollback()
            #textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            #textbutton _("Save") action ShowMenu('save')
            textbutton _("Menu") action ShowMenu('save')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            #textbutton _("Options") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    font gui.navigation_text_font
    hover_sound "sfx/item_hover.wav"
    activate_sound "sfx/item_click.wav"

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    font gui.navigation_text_font
    #outlines [
    #    (0, "#000000a0", 2, 2)
    #]


## --- GALLERY --- ##
init python:
    import math

    # CG gallery
    g = Gallery()

    g.unlocked_advance = True
    g.navigation = True
    g.span_buttons = True # NOTE: This and navigation are off because it allowed you to see locked images????
    g.slideshow_delay = 6

    # Gallery item list - must be image names without extension - and must always be of .png files
    # Don't forget to also define the persistent variables in script.rpy
    galleryList = [
        
    ]

    for itemArr in galleryList:
        g.button("g_btn_" + itemArr[0])

        for item in itemArr:
            g.image(item)

            # NOTE: Condition must be after image!! Why doth the documentation lie?!
            g.condition("persistent.g_unlocks[\"" + item + "\"]") # NOTE: If this is highlighted in red, it is just VSCode being weird. This is correct.
    
    # The transition used when switching images.
    g.transition = Dissolve(0.25)

    # Gallery grid
    g_cols = gui.gallery_cols

    g_rows = math.ceil(len(galleryList) / g_cols)
    g_thumb_margin = 20
    g_thumb_width = math.ceil(gui.gallery_viewport_width / g_cols - (g_thumb_margin))
    g_thumb_height = math.ceil(g_thumb_width / 16 * 9)

    # Music gallery
    music_gallery_items = {
        
    }

    music_gallery_rows = len(music_gallery_items.keys())

    current_playing_music = None

    @renpy.pure
    class MusicGalleryButtonAction(Action):
        def __init__(self, music_file):
            self.music_file = music_file

        def __call__(self):
            global current_playing_music

            if current_playing_music == self.music_file:
                current_playing_music = None
                renpy.music.stop("music")
            else:
                current_playing_music = self.music_file
                renpy.music.play(self.music_file, channel="music", loop=True)

            renpy.restart_interaction()

        def get_selected(self):
            global current_playing_music
            return current_playing_music == self.music_file
    
    def MusicGalleryButton(music_file, value=None):
        def get():
            return MusicGalleryButtonAction(music_file=music_file)
        
        rv = get()

        if rv is not None:
            if isinstance(rv, tuple):
                rv, alt = rv
            else:
                alt = None

            if alt is not None:
                rv.alt = __(alt)
            else:
                rv.alt = __(music_file) + " [text]"
                
        return rv

screen gallery:
    tag menu

    default pref_menu = "cgs"

    use game_menu(_("Gallery")):
        vbox:
            spacing 23

            hbox:
                style_prefix "tabs"

                textbutton _("CGs") action SetScreenVariable("pref_menu", "cgs")
                textbutton _("Music") action SetScreenVariable("pref_menu", "music")
                textbutton _("Scene Select") action SetScreenVariable("pref_menu", "scenes")

            viewport:
                style_group "gallery_wrapper"

                yinitial 0.0
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                if pref_menu == "scenes":
                    use gallery_scenes
                elif pref_menu == "cgs":
                    use gallery_cgs
                elif pref_menu == "music":
                    use gallery_music

screen gallery_music():
    grid 1 music_gallery_rows:
        xfill True

        for item in music_gallery_items.keys():
            if persistent.m_unlocks[item]:
                textbutton _(music_gallery_items[item]["name"]):
                    style "music_gallery_button"
                    action MusicGalleryButton("music/" + music_gallery_items[item]["file"])
            else:
                label _("???"):
                    style "music_gallery_item_inactive"

style music_gallery_item_inactive:
    padding (27, 8, 15, 8)

style music_gallery_item_inactive_text:
    color "#8888887f"
    size gui.interface_text_size
    font "gui/fonts/Lexend-Regular.ttf"

style music_gallery_button:
    padding (27, 8, 15, 8)
    foreground "gui/button/music_[prefix_]foreground.png"

style music_gallery_button_text:
    font "gui/fonts/Lexend-Regular.ttf"
    size gui.interface_text_size
    color gui.idle_color
    hover_color "#d73a1b"
    selected_color "#d73a1b"
    #selected_color "#d73a1b"
    #selected_font "gui/fonts/Lexend-Bold.ttf"

style gallery_wrapper_vscrollbar:
    unscrollable gui.unscrollable

# Scene select
init python:
    scenesList = [
        
    ]

    scenes_cols = 3
    scenes_rows = math.ceil(len(scenesList) / scenes_cols)
    scenes_thumb_margin = 20
    scenes_thumb_width = math.ceil(gui.gallery_viewport_width / scenes_cols - (scenes_thumb_margin))
    scenes_thumb_height = math.ceil(scenes_thumb_width / 16 * 9)

screen gallery_scenes():
    grid scenes_cols scenes_rows:
        xfill True
        yspacing scenes_thumb_margin

        for item in scenesList:
            if persistent.scene_unlocks[item]:
                frame:
                    xfill False
                    yfill False
                    padding (0, 0, 0, 0)
                    margin (0, 0, 0, 0)
                    xmaximum scenes_thumb_width
                    ymaximum scenes_thumb_height

                    add "scene_thumbnails/" + item + ".png"

                    imagebutton:
                        idle "scene_thumbnails/" + item + ".png"
                        hover im.Scale("gallery_thumb_hover.png", scenes_thumb_width, scenes_thumb_height)
                        hover_sound "sfx/item_hover.wav"
                        activate_sound "sfx/item_click.wav"

                        action Confirm(
                            _("Loading this scene will lose unsaved progress.\nAre you sure you want to do this?"),
                            yes=Start(item),
                            no=None,
                            confirm_selected=False
                        )
            else:
                frame:
                    xfill False
                    yfill False
                    padding (0, 0, 0, 0)
                    margin (0, 0, 0, 0)
                    xmaximum scenes_thumb_width
                    ymaximum scenes_thumb_height

                    add im.Scale("gallery_thumb_locked.png", g_thumb_width, g_thumb_height)

screen gallery_cgs():
    grid g_cols g_rows:
        xfill True

        for itemArr in galleryList:
            add g.make_button("g_btn_" + itemArr[0],
                "gallery_thumbnails/" + itemArr[0] + "_thumb.png",
                im.Scale("gallery_thumb_locked.png", g_thumb_width, g_thumb_height),
                bottom_margin=g_thumb_margin,
                right_margin=g_thumb_margin,
                hover_border=im.Scale("gallery_thumb_hover.png", g_thumb_width, g_thumb_height)
            )

screen gallery_navigation(gallery):
    hbox:
        xalign 1.0
        yalign 1.0
        yoffset -5

        style_group "gallery"

        textbutton _("Prev") action gallery.Previous(unlocked=gallery.unlocked_advance)
        textbutton _("Next") action gallery.Next(unlocked=gallery.unlocked_advance)
        textbutton _("Slideshow") action gallery.ToggleSlideshow()
        textbutton _("Return") action gallery.Return()


style gallery_button:
    padding (15, 6, 15, 0)

style gallery_button_text:
    font gui.navigation_text_font
    size 21
    color gui.idle_small_color
    hover_color "#d73a1b"
    selected_color gui.accent_color

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    vbox:
        if main_menu:
            if skippedMenuIntro == False:
                at nav_fade
        
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing 15

        if main_menu:

            textbutton _("Start"):
                action Start()

        else:

            textbutton _("Save"):
                action ShowMenu("save")
                
        textbutton _("Load"):
                action ShowMenu("load")

        if not main_menu:
            textbutton _("History"):
                action ShowMenu("history")

        #textbutton _("Gallery"):
        #    action ShowMenu("gallery")

        #textbutton _("About"):
        #        action ShowMenu("about")
                
        textbutton _("Options"):
                action ShowMenu("preferences")

        #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Controls"):
            #    action ShowMenu("help")

        if _in_replay:

            textbutton _("End Replay"):
                action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu"):
                action MainMenu()

        
        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit"):
                action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    font gui.navigation_text_font

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font gui.navigation_text_font
    hover_color "#d73a1b"

## Custom animation stuff
transform confirm_fade:
    on show:
        alpha 0.0
        ease 0.25 alpha 1.0
    on hide:
        ease 0.25 alpha 0.0

transform nav_fade:
    on show:
        alpha 0
        xoffset -50
        
        parallel:
            easein 0.5 alpha 1.0
        parallel:
            easein 0.5 xoffset 0
    on hide:
        alpha 0.0
        xoffset -50

transform main_menu_logo_fade:
    on show:
        alpha 0.0
        xoffset -50

        parallel:
            easein 0.5 alpha 1.0
        
        parallel:
            easein 0.5 xoffset 0
    
transform main_menu_fade:
    on show:
        alpha 0.0

        parallel:
            linear 0.5 alpha 1.0



## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

define skippedMenuIntro = False

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

    #on "show":
    #    action Play("music", "music/Summertime_Sunset.flac", loop=True)
    #on "replace" action [Pause(0.5), Play("music", "music/Summertime_Sunset.flac")]
    #on "replaced" action Stop("music")

    add gui.main_menu_background
    add CSnowBlossom(At("images/particles/particle_party.png", anim_particle_party), border=64, count=20, start=2.0, fast=True, yspeed=(-25, -15), xspeed=(-30, 30), horizontal=False)
    add CSnowBlossom(At("images/particles/particle_party.png", anim_particle_party_far), border=64, count=50, start=2.0, fast=True, yspeed=(-10, -5), xspeed=(-15, 15), horizontal=False)

    frame:
        at main_menu_fade
        style "main_menu_frame"

    add "gui/logo.png" at main_menu_logo_fade:
        xalign 0.0
        yalign 0.0
        yoffset 100
        xoffset 50
        size [512, 873 * (512 / 2471)]

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:
        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):
    on "hide" action SetVariable("current_playing_music", None)

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
    font "gui/fonts/Lexend-Bold.ttf"

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:
            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n":
                    line_spacing 5

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

default persistent.voice_acting = "all"
default persistent.voice_lang = None
default persistent.sound_effects = "all"
default persistent.sound_effects_sfw = persistent.sound_effects == "all" or persistent.sound_effects == "sfw_only"
default persistent.sound_effects_nsfw = persistent.sound_effects == "all" or persistent.sound_effects == "nsfw_only"
default persistent.dialogue_position = "modern"
default persistent.reduced_movement = False

init -10 python:
    class SetDialoguePosition(Action, FieldEquality):
        identity_fields = [ "object" ]
        equality_fields = [ "field", "value" ]

        kind = "field"

        def __init__(self, value):
            self.value = value        

        def __call__(self):
            persistent.dialogue_position = self.value
            renpy.restart_interaction()

        def get_selected(self):
            return persistent.dialogue_position == self.value
    
    class SetVoiceActing(Action, FieldEquality):
        identity_fields = [ "object" ]
        equality_fields = [ "field", "value" ]

        kind = "field"

        def __init__(self, value):
            self.value = value        

        def __call__(self):
            persistent.voice_acting = self.value

            if self.value == "all":
                # Clears mute list
                persistent._voice_mute.clear()
            if self.value == "characters":
                # Clears mute list
                persistent._voice_mute.clear()
                persistent._voice_mute.add("narrator")
            elif self.value == "none":
                # Mutes characters
                persistent._voice_mute.clear()
                persistent._voice_mute.add("character")
                persistent._voice_mute.add("narrator")

            renpy.restart_interaction()

        def get_selected(self):
            return persistent.voice_acting == self.value

    class ToggleReducedMovement(Action, FieldEquality):
        identity_fields = [ "object" ]
        equality_fields = [ "field" ]

        kind = "field"     

        def __call__(self):
            persistent.reduced_movement = not persistent.reduced_movement
            renpy.restart_interaction()

        def get_selected(self):
            return persistent.reduced_movement == True
        
    class SetVoiceLanguage(Action, FieldEquality):
        identity_fields = [ "object" ]
        equality_fields = [ "field", "value" ]

        kind = "field"

        def __init__(self, value):
            self.value = value        

        def __call__(self):
            persistent.voice_lang = self.value

            if self.value == "japanese":
                config.auto_voice = "tl/japanese/voices/{id}.wav"
            elif self.value == None:
                config.auto_voice = "voices/{id}.wav"

            renpy.restart_interaction()

        def get_selected(self):
            return persistent.voice_lang == self.value

    class SetSoundEffects(Action, FieldEquality):
        identity_fields = [ "object" ]
        equality_fields = [ "field", "value" ]

        kind = "field"

        def __init__(self, value):
            self.value = value        

        def __call__(self):
            persistent.sound_effects = self.value
            renpy.restart_interaction()

        def get_selected(self):
            return persistent.sound_effects == self.value

    class ToggleSoundEffectsNsfw(Action, FieldEquality):
        identity_fields = [ "object" ]
        equality_fields = [ "field" ]

        kind = "field"     

        def __call__(self):
            persistent.sound_effects_nsfw = not persistent.sound_effects_nsfw
            renpy.restart_interaction()

        def get_selected(self):
            return persistent.sound_effects_nsfw == True

    class ToggleSoundEffectsSfw(Action, FieldEquality):
        identity_fields = [ "object" ]
        equality_fields = [ "field" ]

        kind = "field"

        def __call__(self):
            persistent.sound_effects_sfw = not persistent.sound_effects_sfw
            renpy.restart_interaction()

        def get_selected(self):
            return persistent.sound_effects_sfw == True

    def CustomPref(name, value=None):
        name = name.lower()

        if isinstance(value, basestring):
            value = value.lower()
        
        def get():
            if name == "dialogue position":
                return SetDialoguePosition(value)
            elif name == "voice acting":
                return SetVoiceActing(value)
            elif name == "reduced-movement":
                return ToggleReducedMovement()
            elif name == "voice lang":
                return SetVoiceLanguage(value)
            #elif name == "sound effects":
            #    return SetSoundEffects(value)
            elif name == "sound effects nsfw":
                return ToggleSoundEffectsNsfw()
            elif name == "sound effects sfw":
                return ToggleSoundEffectsSfw()
        
        rv = get()

        if rv is not None:
            if isinstance(rv, tuple):
                rv, alt = rv
            else:
                alt = None

            if alt is not None:
                rv.alt = __(alt)
            else:
                rv.alt = __(name) + " [text]"
                
        return rv

screen preferences():
    tag menu

    default pref_menu = "settings"

    use game_menu(_("Options")):
        style_prefix "help"

        vbox:
            spacing 23

            hbox:
                style_prefix "tabs"

                textbutton _("Settings") action SetScreenVariable("pref_menu", "settings")

                if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                    textbutton _("Keyboard") action SetScreenVariable("pref_menu", "keyboard")
                    textbutton _("Mouse") action SetScreenVariable("pref_menu", "mouse")

                    if GamepadExists():
                        textbutton _("Gamepad") action SetScreenVariable("pref_menu", "gamepad")

                textbutton _("Credits") action SetScreenVariable("pref_menu", "credits")

            viewport:
                yinitial 0.0
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                if pref_menu == "keyboard":
                    use keyboard_help
                elif pref_menu == "mouse":
                    use mouse_help
                elif pref_menu == "gamepad":
                    use gamepad_help
                elif pref_menu == "settings":
                    use prefs_settings
                elif pref_menu == "credits":
                    use prefs_credits

style tabs:
    spacing 0

style tabs_button:
    padding (0, 0, 0, 0)
    margin (0, 0, 32, 0)

style help_vscrollbar:
    unscrollable gui.unscrollable

screen prefs_credits:
    vbox:
        spacing 8

        label _("Illustrations"):
            style "prefs_credits_section_label"
            top_margin 0

        label _("Sulcate"):
            style "prefs_credits_label"

        label _("Voice Acting"):
            style "prefs_credits_section_label"

        label _("Baku Satsu (Amy)"):
            style "prefs_credits_label"

        label _("Gina Galore (Chloe)"):
            style "prefs_credits_label"

        label _("Kitt Nevada (Narrator)"):
            style "prefs_credits_label"

        label _("Music"):
            style "prefs_credits_section_label"

        label _("g3ntlebreeze"):
            style "prefs_credits_label"

        label _("Narrative Consultation & Editing"):
            style "prefs_credits_section_label"

        label _("Pleasant Girl"):
            style "prefs_credits_label"

        label _("Development & Production"):
            style "prefs_credits_section_label"

        label _("MadCreativity"):
            style "prefs_credits_label"

        label _("Other Credits & Licenses"):
            style "prefs_credits_section_label"

        label _("Benefitship was created using Ren'Py [renpy.version_only]."):
            style "prefs_credits_label"
        label _("Impact on head by JakLocke -- https://freesound.org/s/698054/ -- License: Attribution 4.0"):
            style "prefs_credits_label"
        #label _("The Wave Shader Ren'Py Module was made by Daniel Westfall and is under the MIT License."):
        #    style "prefs_credits_label"
        label _("OpenNSFW SFX were made by LeHornySFX3D"):
            style "prefs_credits_label"
        label _("This program contains free software under a number of licenses, including the MIT License and GNU Lesser General Public License. A complete list of software, including links to full source code, can be found at https://www.renpy.org/doc/html/license.html"):
            style "prefs_credits_label"

style prefs_credits_section_label:
    margin (0, 32, 0, 0)

style prefs_credits_section_label_text:
    size gui.interface_text_size
    font "gui/fonts/Lexend-Bold.ttf"
    #color "#d73a1b"

style prefs_credits_label_text:
    size gui.interface_text_size
    font "gui/fonts/Lexend-Regular.ttf"
    color "#ffffff"

screen prefs_settings:
    vbox:
        hbox:
            box_wrap True

            if renpy.variant("pc") or renpy.variant("web"):

                vbox:
                    style_prefix "radio"
                    label _("Display"):
                        top_margin 0
                    textbutton _("Window") action Preference("display", "any window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

            vbox:
                style_prefix "check"
                label _("Skip"):
                    top_margin 0
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            #vbox:
            #    style_prefix "radio"
            #    label _("Text Language"):
            #        top_margin 0
            #    textbutton "English (Original)" action Language(None)
            #    textbutton "Japanese" action Language("japanese")

            #vbox:
            #    style_prefix "radio"
            #    label _("Voice Language"):
            #        top_margin 0
            #    textbutton "English (Original)" action CustomPref("voice lang", None)
            #    textbutton "Japanese" action CustomPref("voice lang", "japanese")

            vbox:
                style_prefix "radio"
                label _("Voice Acting"):
                    top_margin 0
                
                textbutton _("Characters & Narration") action CustomPref("voice acting", "all")
                textbutton _("Characters") action CustomPref("voice acting", "characters")
                textbutton _("None") action  CustomPref("voice acting", "none")

            vbox:
                style_prefix "check"
                label _("Sound Effects"):
                    top_margin 0

                #textbutton _("All") action CustomPref("sound effects", "all")
                textbutton _("SFW") action CustomPref("sound effects sfw")
                textbutton _("NSFW") action CustomPref("sound effects nsfw")
                #textbutton _("None") action  CustomPref("sound effects", "none")

            vbox:
                style_prefix "radio"
                label _("Dialogue Type"):
                    top_margin 2 * gui.pref_spacing
                textbutton _("Textboxes") action CustomPref("dialogue position", "modern")
                textbutton _("Clean (Top)") action CustomPref("dialogue position", "clean-top")
                textbutton _("Clean (Bottom)") action CustomPref("dialogue position", "clean-bottom")

            vbox:
                style_prefix "check"
                label _("VFX Options"):
                    top_margin 2 * gui.pref_spacing
                textbutton _("Reduced Movement") action CustomPref("reduced-movement")

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

        null height (4 * gui.pref_spacing)

        hbox:
            style_prefix "slider"
            box_wrap True

            #vbox:

                #label _("Text Speed")

                #bar value Preference("text speed")

            vbox:

                if config.has_music:
                    label _("Music Volume"):
                        top_margin 0

                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:

                    label _("Sound Volume"):
                        top_margin 0

                    hbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)

                if config.has_voice:
                    label _("Voice Volume"):
                        top_margin 0

                    hbox:
                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"

            vbox:
                label _("Auto-Forward Time"):
                    top_margin 0

                hbox:
                    bar value Preference("auto-forward time")

                #label _("Dialogue Position (Vertical)")

                #hbox:
                #    bar value CustomPref("dialogue position")


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0
    font "gui/fonts/Lexend-Bold.ttf"

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

init -10 python:
    current_remap_action = None

    @renpy.pure
    class SetCustomFieldKeymap(Action):
        def __init__(self, remap_action):
            self.remap_action = remap_action

        def __call__(self):
            global current_remap_action
            current_remap_action = self.remap_action
            renpy.show_screen("controls_remap", self.remap_action)
            renpy.restart_interaction()

        def get_selected(self):
            global current_remap_action
            return current_remap_action == self.remap_action
    
    def CustomPrefKeymap(remap_action, value=None):
        def get():
            return SetCustomFieldKeymap(remap_action=remap_action)
        
        rv = get()

        if rv is not None:
            if isinstance(rv, tuple):
                rv, alt = rv
            else:
                alt = None

            if alt is not None:
                rv.alt = __(alt)
            else:
                rv.alt = __(remap_action) + " [text]"
                
        return rv

screen keyboard_help():
    vbox:
        spacing 0

        for i, remap_action in enumerate(list(action_names.keys())):
            hbox:
                label _(action_names[remap_action]):
                    style "setting_label"
                    if i == 0:
                        top_margin 0

                textbutton _(control_names[config.keymap[remap_action][0]]):
                    style "setting_button"
                    action CustomPrefKeymap(remap_action=remap_action)
                    if i == 0:
                        top_margin 0

style setting_label:
    xsize 480
    margin (0, 8, 0, 8)

style setting_label_text:
    size gui.interface_text_size
    font "gui/fonts/Lexend-Bold.ttf"
    color "#ffffff"

style setting_button:
    margin (16, 8, 16, 8)
    padding (0, 0, 0, 0)

style setting_button_text:
    font "gui/fonts/Lexend-Regular.ttf"
    color gui.idle_color
    insensitive_color gui.insensitive_color
    hover_color "#d73a1b"
    #selected_font "gui/fonts/Lexend-Bold.ttf"
    selected_color "#d73a1b"
    size gui.interface_text_size

init python:
    mouse_controls = {
        "Advance dialogue and activate interface": "Left Click",
        "Hide user interface": "Middle Click",
        "Game menu": "Right Click",
        "Roll back to earlier dialogue": "Mouse Wheel Up",
        "Roll forward to later dialogue": "Mouse Wheel Down"
    }

    gamepad_controls = {
        "Advance dialogue and activate interface": "Right Trigger / Bottom Button",
        "Roll back to earlier dialogue": "Left Trigger / Left Shoulder",
        "Roll forward to later dialogue": "Right Shoulder",
        "Navigate interface": "D-Pad / Sticks",
        "Game menu": "Start / Guide",
        "Hide user interface": "Y / Top Button"
    }

screen mouse_help():
    vbox:
        spacing 0

        for i, remap_action in enumerate(list(mouse_controls.keys())):
            hbox:
                label _(remap_action):
                    style "setting_label"
                    if i == 0:
                        top_margin 0

                label _(mouse_controls[remap_action]):
                    style "setting_perm_label"
                    if i == 0:
                        top_margin 0

style setting_perm_label:
    margin (16, 8, 16, 8)

style setting_perm_label_text:
    font "gui/fonts/Lexend-Bold.ttf"
    color "#d73a1b"
    size gui.interface_text_size

screen gamepad_help():
    vbox:
        spacing 0

        for i, remap_action in enumerate(list(gamepad_controls.keys())):
            hbox:
                label _(remap_action):
                    style "setting_label"
                    if i == 0:
                        top_margin 0

                label _(gamepad_controls[remap_action]):
                    style "setting_perm_label"
                    if i == 0:
                        top_margin 0

        textbutton _("Calibrate") action GamepadCalibrate()

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0
    font "gui/fonts/Lexend-Bold.ttf"
    color "#d73a1b"
    line_spacing 0
    line_leading 0

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm
screen confirm(message, yes_action, no_action):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    window:
        at confirm_fade
        window:
            add "gui/overlay/confirm.png"

    frame:
        at confirm_fade
        style "confirm_frame"
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900