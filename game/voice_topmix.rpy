# Automatically dips music and sound volume smoothly when voice lines are playing.
# You don't need to do anything to get this to work. Just place this file in your game folder and you're done.

# Developed by MadCreativity for Benefitship and other RFH Games' titles.

# Benefitship (NSFW): https://twitter.com/benefitshipgame
# RFH Games (NSFW): https://twitter.com/rfhgames

# This entire file is under CC0, meaning you can do *literally anything*. It's public domain.
# https://creativecommons.org/public-domain/cc0/

init -1 python:
    # You may change these variables
    dynamic_volume_attack_speed = 0.500 # Time from standard volume to ducked volume in seconds
    dynamic_volume_release_speed = 1.000 # Time from ducked volume to standard volume in seconds
    dynamic_volume_low = 0.6 # New volume on dip
    music_standard_volume = 0.3

    # Do not change anything below here unless you know what you're doing
    periodic_calls_per_second = 20 # Defined by Ren'Py
    dynamic_volume_high = 1.0 # Volume to return to after dip - generally always 1.0, unless it's been programatically changed
    dynamic_volume = 1.0 # Current volume
    dynamic_volume_dir = 1 # Current volume change direction

    dynamic_volume_attack_rate = (dynamic_volume_high - dynamic_volume_low) / (dynamic_volume_attack_speed * periodic_calls_per_second)
    dynamic_volume_release_rate = (dynamic_volume_high - dynamic_volume_low) / (dynamic_volume_release_speed * periodic_calls_per_second)

    def update_dynamic_volume():
        global dynamic_volume_dir
        global dynamic_volume
        global dynamic_volume_attack_rate
        global dynamic_volume_release_rate
        global dynamic_volume_low
        global dynamic_volume_high

        channel_voice = renpy.audio.audio.get_channel("voice")
        
        if channel_voice.get_playing():
            dynamic_volume_dir = -1
        else:
            dynamic_volume_dir = 1
        
        if dynamic_volume_dir == -1:
            if dynamic_volume > dynamic_volume_low:
                dynamic_volume -= dynamic_volume_attack_rate
            else:
                dynamic_volume = dynamic_volume_low
        elif dynamic_volume_dir == 1:
            # Only increase volume again if "auto" mode is disabled. This is to prevent a mildly irritating increase in volume between dialogue.
            if not _preferences.afm_enable:
                if dynamic_volume < dynamic_volume_high:
                    dynamic_volume += dynamic_volume_release_rate
                else:
                    dynamic_volume = dynamic_volume_high

        renpy.music.set_volume(dynamic_volume * music_standard_volume)
        renpy.sound.set_volume(dynamic_volume)

    config.periodic_callbacks.append(update_dynamic_volume)