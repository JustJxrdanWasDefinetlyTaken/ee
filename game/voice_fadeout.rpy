# Automatically puts a very short fade out at the end of voice lines if they're interrupted. This prevents distracting pops and clicks.
# Time can also be increased to provide a more natural transition.
# You don't need to do anything to get this to work. Just place this file in your game folder and you're done.

# Developed by MadCreativity for Benefitship and other RFH Games' titles.

# Benefitship (NSFW): https://twitter.com/benefitshipgame
# RFH Games (NSFW): https://twitter.com/rfhgames

# This entire file is under CC0, meaning you can do *literally anything*. It's public domain.
# https://creativecommons.org/public-domain/cc0/

init -1400 python:
    from threading import Timer

    voice_fadeout = 0.065

    # Essentially just copy-pasted from the Ren'Py source code, and then modified to support fadeout.
    def voice_interact():
        if not config.has_voice:
            return

        if _voice.ignore_interaction:
            return

        mode = renpy.get_mode()

        if (mode is None) or (mode == "with"):
            return

        if getattr(renpy.context(), "_menu", False) and not _preferences.voice_after_game_menu:
            renpy.sound.stop(channel="voice", fadeout=voice_fadeout)
            return

        if _preferences.voice_sustain and not _voice.sustain:
            _voice.sustain = "preference"

        if _voice.play:
            _voice.sustain = False

        vi = VoiceInfo()

        if not _voice.sustain:
            _voice.info = vi

        if not vi.sustain:
            _voice.play = vi.filename
        else:
            _voice.play = None

        _voice.auto_file = vi.auto_filename
        _voice.sustain = vi.sustain
        _voice.tlid = vi.tlid

        volume = persistent._character_volume.get(_voice.tag, 1.0)

        if (not volume) or (_voice.tag in persistent._voice_mute):
            renpy.sound.stop(channel="voice", fadeout=voice_fadeout)
            store._last_voice_play = _voice.play

        elif _voice.play:
            if not config.skipping:
                renpy.music.get_channel("voice").set_volume(volume)
                renpy.sound.stop(channel="voice", fadeout=voice_fadeout)

                __voiceplay = _voice.play
                
                def play_audio():
                    renpy.sound.play(__voiceplay, channel="voice")
                
                t = Timer(voice_fadeout, play_audio)
                t.start()

            store._last_voice_play = _voice.play

        elif not _voice.sustain:
            renpy.sound.stop(channel="voice", fadeout=voice_fadeout)

            if not getattr(renpy.context(), "_menu", False):
                store._last_voice_play = None

        _voice.play = None    
        _voice.sustain = False
        _voice.tag = None
    
    # Remove existing voice_interact() function and replace it with my own
    for i in config.start_interact_callbacks:
        if i.__name__ == "voice_interact":
            config.start_interact_callbacks.remove(i)

    config.start_interact_callbacks.append(voice_interact)

    for i in config.fast_skipping_callbacks:
        if i.__name__ == "voice_interact":
            config.fast_skipping_callbacks.remove(i)

    config.fast_skipping_callbacks.append(voice_interact)

    for i in config.nointeract_callbacks:
        if i.__name__ == "voice_interact":
            config.nointeract_callbacks.remove(i)

    config.nointeract_callbacks.append(voice_interact)