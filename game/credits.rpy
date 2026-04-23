label credit_text(creditText, hold=1.0):
    show text creditText:
        align (0.5, 0.5)
    with Dissolve(0.5)

    pause hold

    scene black
    with Dissolve(0.5)

    pause 0.25

    return

# Credit controls
screen credits_controls():
    zorder 99999
    modal False

    # Skip credits
    key ["K_SPACE", "mouseup_1"]:
        action Jump("credits_end")

# Undo any credit-specific variables and return to main menu
label credits_end:
    hide screen credits_controls

    # Allow skipping and rollback again.
    $ _game_menu_screen = old_game_menu_screen
    $ quick_menu = True
    $ _dismiss_pause = True
    $ _skipping = True
    $ _rollback = True
    $ config.allow_skipping = True

    # Additional () are necessary. I guess MainMenu() returns a function.
    $ MainMenu(confirm=False)()

    return

label credits:
    window hide

    # Prevent skipping or rollback of any kind.
    $ old_game_menu_screen = _game_menu_screen
    $ quick_menu = False
    $ _game_menu_screen = None
    $ _dismiss_pause = False
    $ _skipping = False
    $ _rollback = False
    $ config.skipping = None
    $ config.allow_skipping = False

    show screen credits_controls

    #play music "music/Summertime_Sunset_Piano.flac" loop

    scene black
    with Dissolve(1.5)

    # Benefitship
    show image "gui/logo.png":
        align [0.5, 0.5]
        size [512, 269 * (512 / 1225)]
    with Dissolve(0.75)

    pause 1

    scene black
    with Dissolve(0.75)
    
    # Credit texts
    call credit_text("Illustrated by Sulcate") from _call_credit_text
    call credit_text("Voice cast:\nBaku Satsu (Amy)\nGina Galore (Chloe)\nKitt Neveda (Narrator)") from _call_credit_text_1
    call credit_text("Music by g3ntlebreeze") from _call_credit_text_2
    call credit_text("Narrative Consultation & Editing by Pleasant Girl") from _call_credit_text_3 
    call credit_text("Created by MadCreativity") from _call_credit_text_4

    # RFH Games
    show image "splash.png" at center
    with Dissolve(0.75)

    pause 1

    #stop music fadeout 1.5

    scene black
    with Dissolve(0.75)

    scene image "gui/main_menu.png"
    with Dissolve(0.75)

    jump credits_end

    return