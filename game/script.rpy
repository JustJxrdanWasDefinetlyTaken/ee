init -10 python:
    def can_play_sfw():
        return persistent.sound_effects_sfw == True

    def can_play_nsfw():
        return persistent.sound_effects_nsfw == True


## Parallax stuff - currently unused
transform parallax_far:
    subpixel True
    zoom 1.03
    xalign 0.5
    yalign 0.5

# TODO: I actually kinda like the breathing animation. Could be worth having on by default with a toggle.
transform breathe:
    animation
    subpixel True
    yalign 1.0

    yzoom 0.997
    xzoom 1.003
    
    parallel:
        ease 2.8 yzoom 1.003
        ease 2.8 yzoom 0.997
        repeat
    parallel:
        ease 2.8 xzoom 0.997
        ease 2.8 xzoom 1.003
        repeat


transform parallax_anim(distance):
    animation
    subpixel True
    
    parallel:
        function checkReducedMovement
    
        ease 4.0 xoffset round(0 * distance)
        ease 4.0 xoffset round(10 * distance)
        ease 4.0 xoffset round(2 * distance)
        ease 4.0 xoffset round(14 * distance)
        repeat
    parallel:
        function checkReducedMovement
    
        ease 3.0 yoffset round(0 * distance)
        ease 3.0 yoffset round(20 * distance)
        ease 3.0 yoffset round(4 * distance)
        ease 3.0 yoffset round(16 * distance)
        repeat

# All character images have a 20px yoffset downwards to allow for "bounce" animations, which go a maximum of 20 pixels up.
#   If the yoffset isn't there, the sprite will end, revealing the background and the cutoff point.

# IDEA: Add xanchor 0.5 to all character images and remove all uses of xalign.
#   Alternatively, see if there's a way to wrap a layeredimage in another displayable, so the layeredimage can have its own xanchor, meaning xalign can still be used on the displayable.

init python:
    # Ambient sound channel
    renpy.music.register_channel("ambient", "sfx", True, tight=True)

# Colors
define NIGHT_COLOR = "#4e596d"
define LIT_COLOR = "#faf6d7"
define MIDDAY_LIT_COLOR = "#faf6d177"

# Solid
image white = Solid("#fff")

# Characters
define roomie = Character(
    "Amy",
    who_color="#fff",
    voice_tag="character"
    )

define futa = Character(
    "Chloe",
    who_color="#fff",
    voice_tag="character"
    )

define narrator = Character(
    voice_tag="narrator"
    )

#########################
### DEVELOPMENT NOTES ###
#########################
#
# Following the line after a transition, add a show of the transition result.
#
# Example:
# 
# show roomie casual_2:
#    alpha 0.0
#    easein 0.25 alpha 1.0
# with Pause(0.5)
#    
# "Amy makes a few large movements with her arms before stretching her legs."
#
# show roomie casual_2:
#    alpha 1.0
# with None
#

init python:
    def resetNarration():
        dtb.setTextbox("narrator", "narrator", round(1920 / 2), 800 + round(229 / 2))
        dtb.setTextbox("narrator_small", "narrator_small", round(1920 / 2), 850 + round(161 / 2))
    
    def checkReducedMovement(trans, st, at, /):
        if not persistent.reduced_movement:
            return None
        else:
            # Do not run
            return 0

define af = renpy.audio.filter

label story:
    $ dtb.setTextbox("futa", "right", 750, 800)
    $ dtb.setTextbox("roomie", "left", 1100, 750)
    $ dtb.setTextbox("narrator", "narrator", round(1920 / 2), 800 + round(229 / 2))
    $ dtb.setTextbox("narrator_small", "narrator_small", round(1920 / 2), 850 + round(161 / 2))
    
    #camera:
    #    xalign 0.5
    #    yalign 0.5
    #    zoom 1.05
    #    xoffset 0
    #    yoffset 0
    #    subpixel True

    #    parallel:
    #        ease 2.5 xoffset 0
    #        ease 2.5 xoffset 4
    #        ease 2.5 xoffset 0
    #        ease 2.5 xoffset 6
    #        repeat
    #    parallel:
    #        ease 3.0 yoffset 0
    #        ease 3.0 yoffset 20
    #        ease 3.0 yoffset 8
    #        ease 3.0 yoffset 16
    #        repeat
    #with None

    $ renpy.music.set_audio_filter("music", af.Lowpass(400), replace=True)
    
    play music "music/relaxing.ogg" fadein 0.75

    pause 0.75

    futa "Mn... I don't know about this..." (textbox="narrator_small", textbox_outline=True)

    $ renpy.music.set_audio_filter("music", None, replace=True, duration=1.5)

    scene cg_dressing_room_01:
        subpixel True
        zoom 1.8
        xalign 0.16
        yalign 0.25
    with Dissolve(0.75)

    "Chloe's flushed face peeks out from behind the dressing room curtain." (textbox="narrator_small")
    "Amy lets out a soft laugh at the sight."

    show cg_dressing_room_01:
        parallel:
            ease 3.0 zoom 1.0
        parallel:
            ease 3.0 xalign 0.5
        parallel:
            ease 3.0 yalign 0.5
    with None

    roomie "No, come on~!" (textbox="roomie")
    roomie "Let me see."

    futa "..." (textbox="futa")

    roomie "Please~?" (textbox="roomie")

    "Chloe glances around." (textbox="narrator_small")

    futa "I-I don't think I can go out there." (textbox="futa")
    futa "Uhm, can you maybe just... come in here with me?"

    "Amy lets out an artificially exasperated sigh, rolling her eyes even as her lips curve into a smile." (textbox="narrator_small")

    # NOTE: I'll probably cut this one out in the final version - it's just here to be included in VA lines.
    roomie "*Sigh*" (textbox="roomie")
    # [AR] Comment 1

    futa "S-Sorry..." (textbox="futa")
    # [AR] There are a lot of tildes being used in quick succession, and I think it's a good idea to cut a few out.

    "Chloe chuckles awkwardly, leaning back behind the curtain as Amy approaches with a grin on her face." (textbox="narrator_small")
    # [AR] Edit for clarity

    roomie "Okay, let's see what's so bad~" (textbox="roomie")

    scene cg_dressing_room_02:
        subpixel True
        zoom 1.8
        xalign 0.5
        yalign 0.5
        xoffset 300
        yoffset 430

        pause 0.5

        parallel:
            ease 6.0 yoffset -430
    with ImageDissolve("transitions/trans_01.png", 0.75, 16, reverse=True)

    $ dtb.setTextbox("futa", "right", 1000, 600)
    $ dtb.setTextbox("roomie", "left", 1500, 550)
    $ dtb.setTextbox("narrator_small", "narrator_small", round(1920 / 2), 80 + round(161 / 2))

    "Lifting the curtain briefly to the side to enter the dressing room, Amy looks Chloe up and down." (textbox="narrator_small")
    
    roomie "Pft—" (textbox="roomie")

    futa "D-Don't laugh!" (textbox="futa")

    roomie "Sorry~!" (textbox="roomie")

    "Stifling her laughter, Amy eyes the thick bulge at the front of Chloe's pants, biting her lip." (textbox="narrator_small")
    "In comparison to Chloe's usual choice of thick jeans, the tight, thin leggings leave very little to the imagination."

    show cg_dressing_room_02:
        parallel:
            ease 6.0 zoom 1.0
        parallel:
            ease 6.0 yoffset 0
        parallel:
            ease 6.0 xoffset 0
    with None

    $ dtb.setTextbox("futa", "right", 850, 800)
    $ dtb.setTextbox("roomie", "left", 1120, 800)
    $ dtb.setTextbox("narrator_small", "narrator_small", round(1920 / 2), 850 + round(161 / 2))

    roomie "Well, I think you look kinda hot in them~" (textbox="roomie")

    "Chloe's cheeks turning bright red, she buries her face in her hands." (textbox="narrator_small")

    futa "I-I can't go outside in these." (textbox="futa")
    futa "Everyone will see!"

    roomie "Personally, I think they accentuate your assets nicely." (textbox="roomie")
    roomie "So, how about you just wear them {i}inside{/i} for now?"
    roomie "We can switch away from jogging for a while and maybe try doing some yoga together!"
    roomie "I was planning on doing some later, actually. You could join me!"
    roomie "How does that sound?"

    futa "O-Okay, that could be fun." (textbox="futa")

    roomie "And hey, maybe it'll help you get the confidence to wear them outside too." (textbox="roomie")

    futa "I... don't know about that." (textbox="futa")
    futa "B-But I think... I can wear them inside."

    roomie "Yeah, that's what I'm talking about, Chloe!" (textbox="roomie")

    "Amy grins, giving Chloe a light tap on the shoulder." (textbox="narrator_small")
    "Chloe smiles back, still a little uncertain."
    # [AR] "Awkwardly" was already used as a descriptor for Chloe in this scene, so I changed this to avoid repetition.
    # [AR] But if this doesn't match up with the intended emotion for her, please feel free to swap it out for something else!

    roomie "I've picked out a new pair of shorts for myself too." (textbox="roomie")
    roomie "The other pair are starting to get a bit tight around the cheeks, if you know what I'm saying, haha."
    roomie "They've started riding up and chafing whenever we go jogging."
    roomie "Plus, I'm pretty sure they give me a cameltoe."

    futa "Eheh, yeah, I-I noticed." (textbox="futa")

    "Giggling, Amy gestures in the direction of the exit." (textbox="narrator_small")

    roomie "Well, why don't you go ahead and change back into your jeans, and we can get out of here, yeah?" (textbox="roomie")

    futa "Yeah, that sounds good." (textbox="futa")
    # [AR] Comment 3

    $ renpy.music.set_audio_filter("music", af.Lowpass(400), replace=True, duration=1.5)

    scene black
    with Dissolve(1.5)

    "Some 30 minutes later, back home..." (textbox="narrator_small", textbox_outline=True)

    $ renpy.music.set_audio_filter("music", None, replace=True, duration=1.5)

    scene _bg_living_room_day
    show roomie yoga arm_back_straight:
        xzoom 1.0
        xalign 0.8
    show futa yoga smiling:
        xzoom -1.0
        xalign 0.2

        alpha 0.0
        xoffset -100
    with Dissolve(0.75)

    show futa:
        parallel:
            linear 0.75 alpha 1.0
        parallel:
            easein 0.75 xoffset 0
    with Pause(0.5)

    $ dtb.setTextbox("futa", "right", 750, 800)
    $ dtb.setTextbox("roomie", "left", 1230, 800)

    futa "O-Okay, I'm ready... I think." (textbox="futa")

    show futa:
        alpha 1.0
        xoffset 0
    with None

    show roomie:
        ease 0.15 yoffset -10
        ease 0.075 yoffset 0
    with None

    show roomie grinning
    with Dissolve(0.15)

    roomie "Awesome!" (textbox="roomie")

    show roomie:
        yoffset 0
    with None

    roomie "Try not to overwork yourself or anything, okay?"

    show roomie smiling
    with Dissolve(0.25)

    roomie "I know you're a lot newer to this than I am, so don't be afraid to take a break if you need it."

    show roomie relaxed
    with Dissolve(0.25)

    roomie "I'll try to stick with some of the lighter exercises."

    show futa excited
    with Dissolve(0.25)

    futa "Ah, thank you." (textbox="futa")

    show futa smiling
    with Dissolve(0.25)

    futa "I-I'll do my best to keep up with you..."

    show roomie grinning arm_back_bent
    with Dissolve(0.25)
    
    roomie "Great!" (textbox="roomie")
    roomie "First up, we're gonna do a warrior pose."

    show roomie:
        ease 0.25 xoffset 10
        pause 0.1
        ease 0.5 xoffset -10
        pause 0.1
        ease 0.25 xoffset 0
    with None

    roomie "Just put your leg forward like this, stretch this one back, then lift your arms like so..."
    
    show roomie:
        xoffset 0
    with None

    roomie "Make sense?"

    show futa:
        ease 0.25 xoffset 5
        pause 0.1
        ease 0.25 xoffset 10
        pause 0.1
        ease 0.5 xoffset -5
        pause 0.1
        ease 0.25 xoffset 5
    with None

    show futa genuine overlay_sweat
    with Dissolve(0.25)

    futa "Like... this?" (textbox="futa")

    show futa:
        xoffset 5
    with None

    roomie "Yup! Now just hold that pose..." (textbox="roomie")
    roomie "...and..."
    roomie "...let go."

    show futa:
        ease 0.5 yoffset 20
    with None

    futa "Hahh... Okay, that... wasn't so bad." (textbox="futa")

    show futa:
        yoffset 20
        ease 0.5 yoffset 0
    with None

    roomie "Haha, well, like I said, we're starting easy." (textbox="roomie")

    show futa:
        yoffset 0
    with None

    roomie "Now, for this next one, you keep your legs straight, then bend down and touch your toes, okay?"
    
    show roomie:
        ease 0.5 yoffset 30
    with None

    show roomie relaxed arm_back_straight arm_front_belly
    with Dissolve(0.25)

    roomie "Just like this!"

    show roomie:
        yoffset 30
    with None

    show futa:
        ease 0.5 yoffset 20
    with None

    futa "Mm..." (textbox="futa")

    show futa:
        yoffset 20
    with None

    show image "images/cg/@2/yoga/01.png" as yoga01:
        subpixel True
        zoom 1.6
        xalign 0.5
        yalign 1.0
        xoffset 130
        yoffset 50

        parallel:
            easein 3.0 yoffset 0
        parallel:
            easein 3.0 zoom 1.8
    with Dissolve(1.0)

    $ dtb.setTextbox("futa", "right", 150, 150)
    $ dtb.setTextbox("roomie", "left", 1500, 180)

    futa "..."

    show roomie:
        ease 0.5 yoffset 0
    with None
    
    roomie "Hm?" (textbox="roomie")
    roomie "Chloe, you alright?"
    roomie "You sorta stopped mid-movement."

    hide yoga01
    with Dissolve(0.1)
    
    $ dtb.setTextbox("futa", "right", 750, 800)
    $ dtb.setTextbox("roomie", "left", 1230, 800)

    show futa:
        ease 0.15 yoffset -10
        ease 0.1 yoffset 0
    with None

    show futa shocked 
    with Dissolve(0.25)

    futa "O-Oh, yeah, sorry!" (textbox="futa")

    show futa giggling 
    with Dissolve(0.25)

    futa "I just, uhm..."

    show futa genuine 
    with Dissolve(0.25)

    futa "Are those the old shorts?"

    show roomie smiling arm_front_bent
    with Dissolve(0.25)

    roomie "Yup, they still work just fine for yoga!" (textbox="roomie")
    roomie "It's mainly the friction from running that makes them chafe."
    roomie "Why, what's up?"

    futa "It's just... they're, uhm..." (textbox="futa")

    show futa:
        ease 0.5 xoffset -10
    with None

    show futa aroused 
    with Dissolve(0.25)

    futa "...really tight around... your..."

    show roomie mystified
    with Dissolve(0.25)

    roomie "Hm?" (textbox="roomie")

    "Amy glances down to see what Chloe's eyes are locked on." (textbox="narrator_small")

    show roomie grinning arm_back_bent
    with Dissolve(0.25)

    roomie "Haha, I told you I got cameltoe~" (textbox="roomie")
    roomie "Is it distracting you?"

    show futa:
        ease 0.5 xoffset 0
    with None

    show futa embarrassed_happy 
    with Dissolve(0.25)

    futa "I-It's okay, I can keep going." (textbox="futa")

    show futa:
        xoffset 0
    with None

    show roomie smiling arm_front_belly
    with Dissolve(0.25)

    roomie "Dope." (textbox="roomie")
    roomie "Next up is the downward dog."

    show roomie:
        ease 0.25 yoffset -10
        ease 0.5 yoffset 10
    with None

    roomie "Like this!"

    show roomie:
        yoffset 10
    with None

    show futa smiling -overlay_blush 
    with Dissolve(0.25)

    futa "Right, I've seen that one before." (textbox="futa")

    show futa:
        ease 0.25 yoffset -10
        ease 0.5 yoffset 10
    with None

    "Following Amy's lead, Chloe stretches out her arms and legs, lifting herself off the floor and pushing her butt into the air." (textbox="narrator_small")

    show futa:
        yoffset 10
    with None

    roomie "You got it?" (textbox="roomie")

    futa "Y-Yes, I think so." (textbox="futa")

    show futa:
        ease 0.15 xoffset -2
        ease 0.15 xoffset 2
        ease 0.15 xoffset -2
        ease 0.15 xoffset 2
        ease 0.15 xoffset -2
        ease 0.15 xoffset 2
    with None

    show futa overlay_sweat
    with Dissolve(0.25)

    "Her arms tremble a bit, struggling to hold her bodyweight up." (textbox="narrator_small")

    show futa:
        xoffset 2
    with None

    show roomie:
        ease 0.25 yoffset 15
    with None

    show roomie relaxed arm_back_straight
    with Dissolve(0.25)

    roomie "Aaand relax." (textbox="roomie")

    show roomie:
        yoffset 15
    with None

    show futa:
        ease 0.5 yoffset 20
    with None
    
    show futa giggling 
    with Dissolve(0.25)

    futa "*HUFF*" (textbox="futa")

    show futa:
        yoffset 20
    with None

    "With an exhausted exhale, Chloe falls onto the floor, her breathing heavy." (textbox="narrator_small")

    show roomie:
        ease 0.5 yoffset 15
    with None

    roomie "You alright?" (textbox="roomie") # TODO: Maybe we should cut this down to just "d'ya need a break?" after Chloe's huffing? Or maybe this is okay anyway.
    
    futa "*Huff*" (textbox="futa")

    show futa smiling
    with Dissolve(0.25)
    
    futa "Yeah, I-I'm okay."

    roomie "D'ya need a break?" (textbox="roomie")

    show futa giggling
    with Dissolve(0.25)

    futa "Uhm... maybe just a short one..." (textbox="futa")

    show futa genuine
    with Dissolve(0.25)

    futa "I'm sorry."

    show roomie smiling arm_front_bent
    with Dissolve(0.25)

    roomie "Hey, relax, it's no problem." (textbox="roomie")

    show roomie relaxed
    with Dissolve(0.25)
    
    roomie "Actually, do you mind if I keep going in the meantime?"

    show roomie grinning
    with Dissolve(0.25)

    roomie "You can just join in when you feel like you're... motivated. Okay~?"

    show futa smiling
    with Dissolve(0.25)

    futa "Y-Yeah, that sounds good." (textbox="futa")
    futa "Thanks."

    show roomie arm_back_bent
    with Dissolve(0.25)

    "Amy does a quick stretch of her upper body, then moves her legs apart, standing with her back to Chloe." (textbox="narrator_small")

    show roomie:
        pause 0.1
        easein 0.5 yoffset -10
        easein 0.75 yoffset -2
    with None

    roomie "Hmng..." (textbox="roomie")

    show roomie:
        yoffset -2
    with None

    show roomie:
        parallel:
            easeout 0.5 yoffset 200
        parallel:
            ease 0.5 alpha 0.0
    with None

    "Then, in one smooth movement, Amy curves her upper body down onto the floor." (textbox="narrator_small")

    show roomie:
        yoffset 200
        alpha 0.0
    with None

    scene image "images/cg/@2/yoga/01.png":
        subpixel True
        zoom 1.5
        xalign 0.8
        yalign 0.0

        pause 0.25

        parallel:
            ease 3.0 zoom 1.0
        parallel:
            ease 3.0 yalign 0.5
        parallel:
            ease 3.0 xalign 0.5
    with ImageDissolve("transitions/trans_01.png", 0.75, 16, reverse=True)

    $ dtb.setTextbox("futa", "right", 100, 200)
    $ dtb.setTextbox("roomie", "left", 1260, 380)
    $ dtb.setTextbox("narrator_small", "narrator_small", 600, 60 + round(161 / 2))
    $ dtb.setTextbox("narrator", "narrator", 600, 80 + round(161 / 2))

    "Her butt raised up in the air and her legs spread, Amy's tight cameltoe sits directly at Chloe's eye level." (textbox="narrator_small")

    futa "Th-Th-Th—" (textbox="futa")

    roomie "So?" (textbox="roomie")
    roomie "Motivated yet~?"

    futa "H-How did you—" (textbox="futa")
    futa "Where did you even see—"

    roomie "Haha, well, I {i}do{/i} use the internet." (textbox="roomie")
    roomie "Plus, it's basically just a modified yoga pose."
    roomie "I guess it's not really in style anymore, but I figured you wouldn't mind~"

    futa "Hhh~" (textbox="futa")

    stop music fadeout 1.5

    if can_play_nsfw():
        play sound "sfx/CLOTHRIP01-01.mp3" volume 1.5

    scene black
    with ImageDissolve("transitions/trans_07.png", 0.25, 16, reverse=True)

    $ resetNarration()

    "Suddenly, a loud tearing rings out across the room." (textbox="narrator_small", textbox_outline=True)

    scene _bg_living_room_day
    show futa yoga overlay_sweat overlay_blush aroused pants_erect:
        xzoom -1.0
        xalign 0.13
        yoffset 64
        
        ease 0.35 yoffset -10
        ease 0.1 yoffset 0
    with ImageDissolve("transitions/trans_07.png", 0.25, 16, reverse=True)
    
    pause 0.25

    # Art of Amy and Chloe in the living room, ready to do yoga.

    $ dtb.setTextbox("futa", "right", 750, 600)
    $ dtb.setTextbox("roomie", "left_down", 1900, 800)
    $ dtb.setTextbox("narrator", "narrator", 1250, 600)
    #$ dtb.setTextbox("narrator_small", "narrator_small", 1250, 600)
    $ dtb.setTextbox("narrator_small", "narrator_small", round(1920 / 2), 850 + round(161 / 2))

    roomie "Wh—" (textbox="roomie")

    play music "music/nsfw.ogg" fadein 1.5

    roomie "Woah~"
  
    "Chloe's thick shaft bursts through the seam of her leggings, hanging loose alongside her heavy balls, forced out through the tight fabric." (textbox="narrator")

    show futa:
        ease 0.3 xoffset 40
        pause 0.1
        ease 0.2 xoffset 60
    with None

    futa "Hmng..." (textbox="futa")
    
    show futa:
        xoffset 60
        ease 0.35 xoffset 400

        parallel:
            ease 0.15 yoffset -10
            ease 0.3 yoffset 40
        parallel:
            pause 0.15
            ease 0.3 alpha 0.0
    with None

    "Lost in her arousal, Chloe doesn't seem to care, and instead rushes up behind Amy, pulling at her yoga shorts." (textbox="narrator_small")

    show futa:
        xoffset 400
        yoffset 40
        alpha 0.0
    with None

    roomie "Oh, wow, that really got you worked up, huh!" (textbox="roomie")
    
    if can_play_nsfw():
        play sound "sfx/CLOTHRIP01-04.mp3" volume 1.5
    
    scene image "images/cg/@2/yoga/02_nofuta.png":
        xalign 0.5
        yalign 0.5
        zoom 1.2
        subpixel True

        easein 3.0 zoom 1.0
    with ImageDissolve("transitions/trans_18.png", 0.35, 16, reverse=True)

    $ dtb.setTextbox("narrator_small", "narrator_small", round(1920 / 2), 80 + round(161 / 2))
    $ dtb.setTextbox("futa", "right", 850, 850)
    $ dtb.setTextbox("roomie", "left_down", 1800, 800)

    "There's another loud rip and Amy lurches forwards as Chloe tears her shorts open, revealing her bare pussy." (textbox="narrator_small")

    roomie "H-Huh?!" (textbox="roomie")

    if can_play_nsfw():
        play ambient "sfx/cunnulingus_1.wav" volume 1.0
    
    show image "images/cg/@2/yoga/02_solofuta.png":
        xalign 0.5
        yalign 0.5
        zoom 1.1
        subpixel True
        alpha 0.0
        
        parallel:
            easein 1.5 zoom 1.0
        parallel:
            linear 1.5 alpha 1.0
    with Dissolve(0.5)

    $ dtb.setTextbox("narrator_small", "narrator_small", round(1920 / 2), 850 + round(161 / 2))

    "Her mind wrapped with lust, Chloe thrusts out her tongue, letting it slither past Amy's hot entrance." (textbox="narrator_small")

    roomie "Fwogh~!" (textbox="roomie")

    "Chloe's dick twitches madly at the sound of Amy's moans." (textbox="narrator_small")

    roomie "Hwh-woah!" (textbox="roomie")
    roomie "You alright down there, Chloe?"
    roomie "You're really going at it today, huh?"

    stop ambient fadeout 0.5
    
    if can_play_nsfw():
        play sound "sfx/cunnulingus_pullout.wav"

    "There's a sultry, sticky sound as Chloe pulls a little away, letting spit dribble loosely from her tongue." (textbox="narrator_small")

    show image "images/cg/@2/yoga/02_solofuta.png":
        parallel:
            ease 1.5 alpha 0.75
        parallel:
            ease 1.5 zoom 1.1
    show image "images/cg/@2/yoga/02_nofuta.png":
        parallel:
            ease 1.5 zoom 1.05
    with None

    futa "Hhhh..." (textbox="futa")

    "Her hard breaths of air flow over Amy's entrance, causing her to shiver slightly." (textbox="narrator_small")

    futa "Hnhh... You're... so hot..." (textbox="futa")

    roomie "Pfthahaha, Chloe??" (textbox="roomie")
    roomie "Can you even see me properly from down there?"

    futa "I... I can see plenty...!" (textbox="futa")

    show image "images/cg/@2/yoga/02_nofuta.png":
        xalign 0.5
        yalign 0.5
        subpixel True
        
        parallel:
            ease 0.25 yoffset -8
            ease 0.2 yoffset 0
            pause 0.25
            ease 0.2 yoffset -8
            ease 0.2 yoffset 0
            ease 0.2 yoffset -8
            ease 0.2 yoffset 0
        parallel:
            ease 0.2 xoffset -4
            ease 0.2 xoffset 0
            pause 0.25
            ease 0.2 xoffset -4
            ease 0.2 xoffset 0
            ease 0.2 xoffset -4
            ease 0.2 xoffset 0
    with None

    "Amy wiggles her hips a little impatiently." (textbox="narrator_small")

    roomie "Haha, you're... actually kind of leaving me on the edge here, Chloe, so could you— Hmahhh~!" (textbox="roomie")
 
    if can_play_nsfw():
        play ambient "sfx/cunnulingus_1.wav" volume 1.0

    show image "images/cg/@2/yoga/02_nofuta.png":
        ease 1.5 zoom 1.0

        parallel:
            function checkReducedMovement
            ease 3.0 zoom 1.06
            ease 3.0 zoom 1.0
            repeat
    show image "images/cg/@2/yoga/02_solofuta.png":
        parallel:
            ease 1.5 zoom 1.0
        parallel:
            ease 1.5 alpha 1.0

        pause 0.0

        parallel:
            function checkReducedMovement
            ease 3.0 zoom 1.06
            ease 3.0 zoom 1.0
            repeat
    with None

    "It seems Chloe was already gearing up to continue as she's flicks her tongue over Amy's clit." (textbox="narrator_small")
    "Amy's pretty, shaven pussy is becoming an increasingly slobbery mess as Chloe's spit mingles with Amy's juices."
    
    roomie "Mnh!" (textbox="roomie")

    "Amy lets out a soft moan, her toes curling up as she teeters on the edge of ecstasy." (textbox="narrator_small")

    camera:
        parallel:
            ease 0.1 yoffset -4
            ease 0.1 yoffset 0
            ease 0.1 yoffset -4
            ease 0.1 yoffset 0
    with None

    show white:
        alpha 0.0
        ease 0.5 alpha 0.25
        ease 0.75 alpha 0.0
    with None

    roomie "Oh fhanghhh!" (textbox="roomie")

    camera:
        parallel:
            ease 0.1 yoffset -4
            ease 0.1 yoffset 0
            ease 0.1 yoffset -4
            ease 0.1 yoffset 0
            ease 0.1 yoffset -3
            ease 0.1 yoffset 0
            ease 0.1 yoffset -2
            ease 0.1 yoffset 0
    with None

    show white:
        alpha 0.0
        ease 0.75 alpha 0.35
        ease 1.25 alpha 0.0
    with None

    "Barely able to maintain her pose as her legs seize up with rapid twitches, Amy breathes a wet groan of pleasure." (textbox="narrator_small")
    
    camera:
        parallel:
            ease 0.1 yoffset -2
            ease 0.1 yoffset 0
            ease 0.1 yoffset -2
            ease 0.1 yoffset 0
    with None

    show white:
        alpha 0.0
        ease 0.5 alpha 0.25
        ease 0.75 alpha 0.0
    with None

    roomie "Hahh, damn..." (textbox="roomie")

    "Sticky lubricant drips from her cunt, running down the inside of her thigh and covering Chloe's tongue." (textbox="narrator_small")

    stop ambient fadeout 0.5
    
    "Slick with Amy's fluids, Chloe pulls a bit away, momentarily observing the hot, messy entrance in front of her."
    "Her mind foggy from Amy's scent and wetness, Chloe raises herself up, her breathing heavy."

    scene black
    with ImageDissolve("transitions/trans_07.png", 0.25, 16, reverse=True)

    pause 0.1

    scene image "images/cg/@2/yoga/03_nolines.png":
        subpixel True
        xalign 0.7
        yalign 0.2
        zoom 1.9
        xoffset -80
        yoffset 180

        easein 0.75 zoom 2.15

        block:
            function checkReducedMovement
            ease 2.0 zoom 1.9
            ease 2.0 zoom 2.0
            repeat
    with ImageDissolve("transitions/trans_03.png", 0.35, 16, reverse=True)

    $ dtb.setTextbox("futa", "left", 1000, 750)
    $ dtb.setTextbox("roomie", "left", 1200, 800)
    $ resetNarration()

    if can_play_nsfw():
        play sound "sfx/thrust_1.wav"

    futa "Hfewhh~" (textbox="futa")

    "Unsteady on her feet, she plunges herself deep inside of Amy with a single thrust, her cock easily sliding through Amy's wet pussy." (textbox="narrator")

    if can_play_nsfw():
        play ambient "sfx/thrusting_1.wav"

    show image "images/cg/@2/yoga/03_nolines.png":
        parallel:
            ease 1.5 xalign 0.5
        parallel:
            ease 1.5 yalign 0.5
        parallel:
            ease 1.5 xoffset 0
        parallel:
            ease 1.5 yoffset 0
        parallel:
            ease 1.5 zoom 1.0
        
        block:
            function checkReducedMovement
            ease 2.0 zoom 1.05
            ease 2.0 zoom 1.0
            repeat
    with None

    show image "images/cg/@2/yoga/03_lines.png":
        subpixel True
        xalign 0.5
        yalign 0.5
        zoom 1.05

        parallel:
            function checkReducedMovement
            rotate 1
            pause 0.07
            rotate 0
            pause 0.07
            rotate 2
            pause 0.07
            rotate -1
            pause 0.07
            repeat
    with Dissolve(1.0)

    $ dtb.setTextbox("futa", "left", 1100, 370)
    $ dtb.setTextbox("roomie", "left_down", 1300, 700)
    $ dtb.setTextbox("narrator_small", "narrator_small", 570, 50 + round(161 / 2))
    $ dtb.setTextbox("narrator", "narrator", 570, 75 + round(161 / 2))

    "Wrapping herself around Amy's body, Chloe humps into the other woman with none of the exhaustion she'd shown moments before." (textbox="narrator")
    "Her fingers sink into the soft flesh of Amy's tits as she pistons her hips wildly." (textbox="narrator_small")

    futa "F-Fhfuck, you're so h-hot in those shorts!" (textbox="futa")

    roomie "Ohah, you don't— don't say~" (textbox="roomie")
    roomie "Oh, shit."
    roomie "Chloe, I'm slipping!"

    show image "images/cg/@2/yoga/03_nolines.png":
        parallel:
            ease 0.6 zoom 1.5
    with Pause(0.25)
    
    scene image "images/cg/@2/yoga/04_nolines.png":
        subpixel True
        xalign 0.5
        yalign 1.0
        zoom 1.5
        
        parallel:
            ease 1.5 yalign 0.5
        parallel:
            ease 1.5 zoom 1.0

        pause 0.0

        parallel:
            function checkReducedMovement
            ease 1.5 zoom 1.05
            ease 1.5 zoom 1.0
            repeat
    show image "images/cg/@2/yoga/04_lines.png":
        subpixel True
        xalign 0.5
        yalign 0.5
        zoom 1.05

        parallel:
            function checkReducedMovement
            rotate 1
            pause 0.07
            rotate 0
            pause 0.07
            rotate 2
            pause 0.07
            rotate -1
            pause 0.07
            repeat
    with ImageDissolve("transitions/trans_07.png", 0.35, 16, reverse=True)

    $ dtb.setTextbox("futa", "left", 920, 700)
    $ dtb.setTextbox("roomie", "right", 950, 300)
    $ resetNarration()

    futa "Hng~!" (textbox="futa")

    "With surprising strength, Chloe hoists Amy up from the floor, holding her up like she's nothing more than a sex toy." (textbox="narrator_small")

    roomie "Woagfh~!" (textbox="roomie")
    roomie "Shfuck, o-okay, that works!"
    roomie "Ah— ah! You're really hitting— hahh!"

    "The abrupt adjustment in position has Chloe's cock now pounding against a particularly sensitive spot inside of Amy." (textbox="narrator_small")

    roomie "Hah, fuck, I'm—!" (textbox="roomie")
    roomie "Hmng!!"

    "As Amy's belly bulges from another deep thrust, her body begins to tremble, her muscles contracting as she climaxes." (textbox="narrator_small")
    "She tightens around Chloe's dick, her cunt gripping and sliding along it as if demanding to keep her inside."
    "Feeling only greater pleasure, Chloe keeps pounding Amy's plump pussy, oblivious to their absurd pose."
    "Her hard cock holds up Amy's entire lower body all on its own as Amy's insides stretch around it."

    stop ambient fadeout 0.25

    if can_play_nsfw():
        play sound "sfx/cum_1.wav"
        play ambient "sfx/cumming_1.wav"

    show image "images/cg/@2/yoga/04_nolines.png":
        parallel:
            ease 0.5 yalign 0.6
        parallel:
            ease 0.5 zoom 1.3
    with None

    show white:
        alpha 0.0
        ease 0.5 alpha 1.0
        ease 1.5 alpha 0.0
    with Pause(0.5)

    show image "images/cg/@2/yoga/05_bgs.png" behind white:
        subpixel True
        xalign 0.5
        yalign 0.6
        zoom 1.3

        parallel:
            ease 1.5 zoom 1.0
        parallel:
            ease 1.5 yalign 0.5

        block:
            function checkReducedMovement
            ease 1.5 zoom 1.05
            ease 1.5 zoom 1.0
            repeat
    show image "images/cg/@2/yoga/05_chars.png" behind white:
        subpixel True
        xalign 0.5
        yalign 0.6
        zoom 1.3

        parallel:
            ease 1.5 zoom 1.0
        parallel:
            ease 1.5 yalign 0.5

        block:
            function checkReducedMovement
            ease 1.5 zoom 1.05
            ease 1.5 zoom 1.0
            repeat
    show image "images/cg/@2/yoga/05_lines.png" behind white:
        subpixel True
        xalign 0.5
        yalign 0.5
        zoom 1.05

        parallel:
            function checkReducedMovement
            rotate 1
            pause 0.07
            rotate 0
            pause 0.07
            rotate 2
            pause 0.07
            rotate -1
            pause 0.07
            repeat
    with Dissolve(0.25)

    $ dtb.setTextbox("futa", "right", 850, 400)
    $ dtb.setTextbox("roomie", "left", 950, 300)
    
    futa "Gohgh~!!" (textbox="futa")

    "Chloe's whole body tenses up, her hands gripping Amy's tits like stress balls as she lets out a groan of pleasure." (textbox="narrator_small")
    "Then, holding Amy's body in a vice grip, Chloe explodes inside her."
    "Creamy ropes of thick, gooey seed rush from Chloe's balls, pulsating up through her shaft."
    "Her thick baby batter covers Amy's insides, filling and stretching her womb."
    
    roomie "Fhuck, this never gets old~~" (textbox="roomie")
    roomie "Hogh..."

    stop ambient fadeout 0.75

    if can_play_nsfw():
        play sound "sfx/cum_2.wav"

    "With another hard thrust, as if to squeeze the last of the cum from her balls, Chloe's grip on Amy finally loosens." (textbox="narrator_small")
    # [AR] Edit for sentence flow

    show image "images/cg/@2/yoga/05_bgs.png":
        ease 1.5 zoom 1.0
    show image "images/cg/@2/yoga/05_chars.png":
        ease 1.5 zoom 1.0
    show image "images/cg/@2/yoga/05_lines.png":
        parallel:
            function checkReducedMovement
            rotate 1
            pause 0.07
            rotate 0
            pause 0.07
            rotate 2
            pause 0.07
            rotate -1
            pause 0.07
            repeat
        parallel:
            ease 0.75 alpha 0.0
    with None

    futa "Hahefh..." (textbox="futa")

    if can_play_nsfw():
        play sound "sfx/pullout_1.wav"

    "With a thick, musky sound, Chloe's long shaft slips out of Amy's pussy as she falls backwards." (textbox="narrator_small")
    "Long strings of cum drool between the pair as Chloe flops onto her butt, even more exhausted than before."
    # [AR] Edit for sentence flow

    stop music fadeout 1.5

    scene black
    with ImageDissolve("transitions/trans_02.png", 0.75, 4, reverse=True)

    "No longer being supported by Chloe's thick shaft, Amy's body gives out and she falls onto her stomach." (textbox="narrator_small", textbox_outline=True)

    roomie "*Huff~*" (textbox="narrator_small", textbox_outline=True)

    "Her belly sloshes as she lands on the squishy bump caused by Chloe's seed." (textbox="narrator_small", textbox_outline=True)
    
    play music "music/somber.ogg" fadein 6.0

    scene image "images/cg/@2/yoga/06.png":
        subpixel True
        zoom 1.9
        xalign 1.0
        yalign 0.7
    with ImageDissolve("transitions/trans_02.png", 0.75, 4, reverse=True)
    
    $ dtb.setTextbox("futa", "right", 100, 100)
    $ dtb.setTextbox("roomie", "right", 700, 100)
    
    roomie "Phew..." (textbox="roomie")

    "With a breathy groan, Amy rolls onto her side to relieve the pressure on her stomach." (textbox="narrator_small")
    # [AR] Comment 4

    futa "Uhm..." (textbox="futa")

    roomie "Yeah? What's—" (textbox="roomie")
    
    "Amy cuts herself off as her voice cracks." (textbox="narrator_small")
    
    show image "images/cg/@2/yoga/06.png":
        parallel:
            ease 3.0 zoom 1.8
        parallel:
            ease 3.0 xalign 0.2
        parallel:
            ease 3.0 yalign 0.0
    with Pause(3.0)

    $ dtb.setTextbox("futa", "right", 700, 650)
    $ dtb.setTextbox("roomie", "left", 1500, 550)
    
    roomie "{i}Ahem,{/i} sorry." (textbox="roomie")
    roomie "What's up?"

    futa "Your shorts..." (textbox="futa")

    roomie "Ah, yeah, you really fucked those up, haha~" (textbox="roomie")
    roomie "I didn't realize you were so strong!"

    futa "I-I'm... really sorry..." (textbox="futa")
    futa "I didn't mean to, I just got caught up in the moment and—"

    roomie "Hey, relax!" (textbox="roomie")

    "Amy tries to sit up, but gets thrown off balance from the added weight on her belly." (textbox="narrator_small")

    roomie "Chloe, I—" (textbox="roomie")

    camera:
        function checkReducedMovement
        pause 0.15

        ease 0.05 yoffset 0
        ease 0.05 yoffset 2
        ease 0.05 yoffset 0
        ease 0.05 yoffset 4
        ease 0.05 yoffset 0
        ease 0.05 yoffset 8
        ease 0.05 yoffset 0
        ease 0.05 yoffset 12

        block:
            ease 0.05 yoffset 0
            ease 0.05 yoffset 16
            repeat 18

        ease 0.075 yoffset 0
    with None

    roomie "Woah...!"

    camera:
        yoffset 0
    with None

    "She waves her arms wildly for a moment, trying to rebalance herself." (textbox="narrator_small")
    
    roomie "Phew, there we go..." (textbox="roomie")
    roomie "Look, we've been living together for, what, ten months now?"
    roomie "Have I ever been upset with you a single time?"

    futa "Well—" (textbox="futa")

    roomie "The time you saw me masturbating doesn't count!" (textbox="roomie")
    
    futa "Eheh, then... no, I guess not." (textbox="futa")

    roomie "Right? Exactly." (textbox="roomie")
    roomie "Trust me, I am {i}very{/i} easy to read."
    roomie "If I'm ever angry or upset or sad or whatever... you'll know, okay?"

    futa "O-Okay." (textbox="futa")
    
    roomie "Now, do I sound angry to you?" (textbox="roomie")

    futa "N-No." (textbox="futa")

    roomie "Do I seem sad?" (textbox="roomie")

    futa "No." (textbox="futa")

    roomie "Upset?" (textbox="roomie")

    futa "No." (textbox="futa")

    roomie "Annoyed?" (textbox="roomie")

    futa "Maybe a little bit?" (textbox="futa")

    roomie "No!!" (textbox="roomie")
    roomie "Wait, fuck."
    roomie "Okay, scratch that last one."

    futa "Eheheh~" (textbox="futa")

    "Chloe lets out a nervous laugh." (textbox="narrator_small")

    roomie "Haha~" (textbox="roomie")

    "Calming down, Amy steadies her voice, a genuine look in her eyes." (textbox="narrator_small")

    roomie "Okay, look, my point is just that you don't need to worry so much." (textbox="roomie")
    roomie "And I know it's not that simple, but I just want you to be happy, you know?"
    roomie "It's kind of a shame that you go from being so excited and energetic to... this?"
    roomie "Like you're afraid you did something wrong."

    futa "..." (textbox="futa")
    futa "I just—"
    futa "I really don't want to stop... being around you."
    futa "Y-You're..."
    futa "...the only friend I've had in years."

    "Chloe looks away, a solemn expression on her face." (textbox="narrator_small")
    "Letting out a sigh, Amy moves onto her knees and opens her arms wide." (textbox="narrator_small")

    roomie "..." (textbox="roomie")
    
    show image "images/cg/@2/yoga/06.png":
        parallel:
            ease 3.0 zoom 1.9
        parallel:
            ease 3.0 xalign 0.22
        parallel:
            ease 3.0 yalign 0.45
    with None

    $ dtb.setTextbox("futa", "right", 700, 250)
    $ dtb.setTextbox("roomie", "left", 1600, 150)

    "With a slightly strained sound, she flops onto Chloe, locking her in a tight embrace." (textbox="narrator_small")

    roomie "Hmn." (textbox="roomie")

    "Nuzzling her face into Chloe's chest, Amy looks up and starts to speak in a whisper." (textbox="narrator_small")

    roomie "Hey." (textbox="roomie")

    futa "H-Hey." (textbox="futa")

    "Amy grins happily up at Chloe's flushed face." (textbox="narrator_small")

    roomie "Don't worry about the shorts, okay?" (textbox="roomie")
    roomie "As for your leggings, they were probably just the wrong choice."
    roomie "I'm sure we'll be able to find something else that works for you."

    futa "Thank you..." (textbox="futa")

    roomie "..." (textbox="roomie")
    roomie "You know..."
    roomie "...my birthday is in a few days."
    
    futa "I-I remember." (textbox="futa")
    futa "November first, r-right?"

    roomie "Uhuh~" (textbox="roomie")

    show image "images/cg/@2/yoga/06.png":
        parallel:
            ease 6.0 zoom 1.8
        parallel:
            ease 6.0 xalign 0.2
        parallel:
            ease 6.0 yalign 0.0
    with None

    $ dtb.setTextbox("futa", "right", 700, 650)
    $ dtb.setTextbox("roomie", "left", 1500, 550)

    "As she speaks, Amy walks her fingers across Chloe's breasts like a tiny stick figure." (textbox="narrator_small")

    roomie "Sooo, did you get me a birthday present yet~?" (textbox="roomie")

    futa "I-I'm sorry, I-I don't know what to get you..." (textbox="futa")

    roomie "Haha, I'm just kidding~" (textbox="roomie")
    roomie "That's okay. I don't really need you to get me anything."
    
    futa "But you did for my birthday and—" (textbox="futa")

    roomie "—and that was my choice!" (textbox="roomie")
    roomie "You shouldn't feel obligated to get me something just because I got you something."
    roomie "That's not how presents are supposed to work~"

    futa "W-Well, I want to get you something!" (textbox="futa")
    futa "You've... done so much for me."
    
    show image "images/cg/@2/yoga/06.png":
        parallel:
            ease 3.0 zoom 1.7
        parallel:
            ease 3.0 xalign 0.6
        parallel:
            ease 3.0 yalign 1.0
    with Pause(3.0)

    $ dtb.setTextbox("futa", "right", 400, 150)
    $ dtb.setTextbox("roomie", "left", 1200, 350)

    roomie "Haha, you mean I've {i}let{/i} you do a lot to me~~" (textbox="roomie")

    futa "T-That too..." (textbox="futa")

    roomie "*Sigh*" (textbox="roomie")
    roomie "Hm..."
    roomie "One of my old high school friends actually invited me to a Halloween party tomorrow."
    # [AR] Edit for flow

    futa "Oh..." (textbox="futa")
    futa "Are you... going?"

    roomie "I haven't really decided yet." (textbox="roomie")
    roomie "Honestly, I haven't seen her in, like, four years at least."
    roomie "But I was thinking... do you maybe wanna come along?"
    
    futa "B-But I wasn't invited." (textbox="futa")

    roomie "Haha, Erica's not really the type to care." (textbox="roomie")
    #roomie "Ah, that's her name, by the way. Erica."
    # [AR] I would honestly delete the above line; it's not necessary, because it's clear who Amy is talking about

    # NOTE TO SELF: I'm gonna cut out the two lines below because they don't really make sense with the conversation.
    #roomie "She was always kind of a big party girl and..."
    #roomie "Well, let's just say that she was {i}very{/i} popular with the boys."

    roomie "I'm sure she'd be more than happy to have another face at the party, but I can text her if you're worried."
    roomie "After I get your cum out of me, that is~"

    show image "images/cg/@2/yoga/06.png":
        parallel:
            ease 3.0 zoom 1.7
        parallel:
            ease 3.0 xalign 0.2
        parallel:
            ease 3.0 yalign 0.0
    with Pause(2.5)

    $ dtb.setTextbox("futa", "right", 700, 650)
    $ dtb.setTextbox("roomie", "left", 1500, 550)

    futa "I... don't know..." (textbox="futa")

    roomie "C'mon, it'll be good for you to get out." (textbox="roomie")
    roomie "And I'll be with you the entire time!"
    
    futa "Well..." (textbox="futa")
    futa "Mm..."
    futa "..."

    "Chloe drifts off into silence." (textbox="narrator_small")

    #roomie "Hm..." 
    roomie "She actually lives a short bus ride away." (textbox="roomie")
    roomie "If it doesn't work out, we can just go back home and..."
    roomie "...maybe I'll give you something for your troubles~"

    futa "O-Okay... I'll d-do it." (textbox="futa")

    roomie "Yes!" (textbox="roomie")
    roomie "Mnnhm~"

    "Amy's embrace tightens as she nuzzles her face back between Chloe's breasts." (textbox="narrator_small")

    show image "images/cg/@2/yoga/06.png":
        parallel:
            ease 3.0 zoom 2.0
        parallel:
            ease 3.0 xalign 0.1
        parallel:
            ease 3.0 yalign 0.15
    with Pause(3.0)

    $ dtb.setTextbox("futa", "right", 1000, 600)
    $ dtb.setTextbox("roomie", "left", 1800, 600)

    futa "Eheh..." (textbox="futa")

    stop music fadeout 6.0

    futa "..."

    "The two lay there for a moment, letting their hearts beat together." (textbox="narrator_small")

    play music "music/relaxing.ogg" fadein 6.0

    roomie "!!" (textbox="roomie")
    roomie "Hey, I just realized."
    
    show image "images/cg/@2/yoga/06.png":
        parallel:
            ease 3.0 zoom 1.0
        parallel:
            ease 3.0 xalign 0.0
        parallel:
            ease 3.0 yalign 0.0
    with None

    $ dtb.setTextbox("futa", "right", 600, 450)
    #$ dtb.setTextbox("roomie", "left", 1000, 400)
    $ dtb.setTextbox("roomie", "left", 1100, 750)

    roomie "You've been lying on the hardwood floor this entire time, haven't you."

    futa "Mm..." (textbox="futa")
    futa "Yeah."

    roomie "Shit, sorry~!" (textbox="roomie")

    scene _bg_living_room_day
    show roomie yoga shorts_belly overlay_sweat arm_back_bent arm_front_belly:
        xalign 0.8
        ypos 1.0
    with ImageDissolve("transitions/trans_04.png", 0.65, 4, reverse=False)

    show roomie:
        ypos 1.0

        parallel:
            ease 0.35 ypos 0.0
        parallel:
            ease 0.35 yoffset -20
        
        ease 0.15 yoffset 0
    with Pause(0.35)

    $ dtb.setTextbox("futa", "right", 750, 800)
    $ dtb.setTextbox("roomie", "left", 1230, 800)

    "Nimbly hopping to her feet, Amy extends a hand to Chloe, pulling her up off the floor." (textbox="narrator_small")
    
    show roomie:
        ypos 0.0
        yoffset 0
    with None

    show futa yoga postsex overlay_sweat giggling:
        xzoom -1.0
        xalign 0.2
        ypos 1.0

        parallel:
            ease 0.35 ypos 0.35
        parallel:
            ease 0.35 yoffset -20
        
        ease 0.1 yoffset 0

        parallel:
            ease 0.35 ypos 0.0
        parallel:
            ease 0.35 yoffset -10
        
        ease 0.1 yoffset 0
    with Pause(0.4)

    futa "Agh." (textbox="futa")

    show futa:
        yoffset 0
        ypos 0.0
    with None

    show roomie grinning arm_back_straight
    with Dissolve(0.25)

    roomie "You okay?" (textbox="roomie") # TODO: Should this potentially just be Chloe being lifted up, going "Agh", maybe a sigh of some kind, then into "You're leaking"? Depends on the takes that come in.

    show futa embarrassed_happy
    with Dissolve(0.25)

    futa "Heheh, yeah, it's not that bad." (textbox="futa")
    
    show futa shocked
    with Dissolve(0.25)

    futa "O-Oh! You're l-leaking!"

    show roomie mystified
    with Dissolve(0.25)

    roomie "Huh?" (textbox="roomie")

    show roomie:
        ease 0.1 yoffset -20
        ease 0.05 yoffset 0
    with None

    show roomie surprised
    with Dissolve(0.15)

    roomie "Oh, shoot!"

    show roomie:
        yoffset 0
    with None

    show roomie:
        xalign -1.0
    with MoveTransition(0.5, time_warp=_warper.easeout)

    "Quickly cupping her crotch with her hands to prevent more of Chloe's seed from spilling out, Amy hurries off to the bathroom with a silly-looking waddle." (textbox="narrator")

    show futa giggling
    with Dissolve(0.25)

    futa "Hahaha~!" (textbox="futa")
    futa "Hahah~"

    stop music fadeout 30.0

    show futa genuine
    with Dissolve(0.25)

    futa "Ahh..."
    futa "*Sigh*"
    futa "(A party, huh...?)"

    stop music fadeout 1.5

    scene black
    with Dissolve(0.75)

    pause 0.35

    scene _bg_bathroom_day
    show roomie yoga shorts_belly overlay_sweat arm_back_straight arm_front_belly:
        xalign 0.7
        yoffset 64
        alpha 0.0
    with Dissolve(0.75)

    show roomie:
        parallel:
            ease 0.5 yoffset 0
        parallel:
            linear 0.5 alpha 1.0
    with None

    $ dtb.setTextbox("futa", "right", 750, 800)
    $ dtb.setTextbox("roomie", "left", 1050, 800)

    play music "music/somber.ogg" fadein 6.0

    roomie "Hahh..." (textbox="roomie")

    show roomie:
        yoffset 0
        alpha 1.0
    with None

    if can_play_sfw():
        play sound "sfx/water_dip.wav"

    show roomie:
        easein 0.5 yoffset 60
    with None
    
    show roomie smiling
    with Dissolve(0.25)
    
    "Amy slides down into the tub." (textbox="narrator_small")
    
    "She moves her hand away from her crotch, letting Chloe's thick seed leak out of her." (textbox="narrator_small")

    show roomie relaxed
    with Dissolve(0.25)

    roomie "*Phew*" (textbox="roomie")
    roomie "Ah, better take these off..."
    
    show roomie:
        ease 0.25 yoffset 35
        ease 0.2 yoffset 60
    with Pause(0.15)

    show roomie belly
    with Dissolve(0.25)

    "Lifting her butt up a bit, Amy slides off the torn yoga shorts, throwing them to the side." (textbox="narrator_small")

    show roomie:
        yoffset 60
    with None

    show roomie smiling
    with Dissolve(0.25)

    roomie "There we go~" (textbox="roomie")
    #roomie "*Sigh*"

    show roomie grinning
    with Dissolve(0.25)

    roomie "..." (textbox="roomie")

    "Amy sits back in the bathtub, her eyes following the dribble of cum as it flows slowly towards the drain." (textbox="narrator_small")
    "She lets out a soft laugh." (textbox="narrator_small")

    roomie "Haha..." (textbox="roomie")

    show roomie relaxed
    with Dissolve(0.25)

    roomie "*Sigh*"   
    
    show roomie thinking_smiling
    with Dissolve(0.25)

    #roomie "(It's weird.)"
    roomie "(It's like... I can't stop smiling when I'm around her.)"
    roomie "(She probably feels the same, right...?)"
    roomie "(Maybe...?)"
    roomie "(I really hope so.)"
    roomie "(But... how do you tell your best friend that you're...)"
    #roomie "..."
    roomie "(...{i}absolutely{/i} in love with her.)"

    "Amy lets her head fall back against the wall." (textbox="narrator_small")

    if can_play_sfw():
        play sound "sfx/headhit.wav"

        pause 0.2

    show roomie smiling
    with Dissolve(0.25)

    roomie "Ow." (textbox="roomie")
    
    "Chuckling, she pats the back of her head where it hit the hard wall behind her." (textbox="narrator_small")

    show roomie grinning
    with Dissolve(0.25)
    
    roomie "Hah~" (textbox="roomie")

    "Suddenly, there's a soft knocking on the bathroom door, and Amy perks up." (textbox="narrator_small")

    if can_play_sfw():
        play sound "sfx/doorknock.wav"

        pause 0.8

    show roomie:
        ease 0.25 yoffset 40
    with None

    show roomie smiling
    with Dissolve(0.25)

    roomie "Come in~!" (textbox="roomie")

    show futa yoga postsex:
        xzoom -1.0
        xalign 0.2
        
        ypos 1.0
        easein 0.75 ypos 0.0
    with Pause(0.75)

    "Pushing it open, Chloe enters, her right hand catching a string of cum drooling from her tip." (textbox="narrator_small")

    show futa:
        ypos 0
    with None
    
    show futa smiling
    with Dissolve(0.25)

    futa "H-Hey, I cleaned up the living room." (textbox="futa")
    
    show roomie grinning
    with Dissolve(0.25)

    roomie "Oh, great!" (textbox="roomie")
    
    show roomie smiling
    with Dissolve(0.25)

    roomie "Thanks, Chloe!"
    roomie "If we're lucky, the floor will remain cumstain-free~"

    show futa giggling
    with Dissolve(0.25)

    futa "Eheheh~" (textbox="futa")

    show futa genuine
    with Dissolve(0.25)

    futa "Uhm, do you... mind if I...?"

    "Chloe gestures awkwardly at the bathtub." (textbox="narrator_small")

    show roomie grinning
    with Dissolve(0.25)

    roomie "Sure, come on in!" (textbox="roomie")
    
    show futa smiling
    with Dissolve(0.25)

    futa "Thank you." (textbox="futa")

    if can_play_sfw():
        play sound "sfx/water_dip.wav"

    scene image "images/cg/@2/yoga/07.png":
        subpixel True
        xalign 0.9
        yalign 0.85
        zoom 1.95

        ease 1.5 xalign 0.95
    with ImageDissolve("transitions/trans_03.png", 0.75, 16, reverse=True)

    $ dtb.setTextbox("futa", "right", 100, 650)
    $ dtb.setTextbox("roomie", "left", 1100, 800)

    "Amy shuffles back to allow for more room as Chloe slides into the bathtub in front of her." (textbox="narrator_small")

    roomie "You know, I think tomorrow's gonna be really great." (textbox="roomie")
    roomie "It's been a while since I've been to a good Halloween party."
    # [AR] Comment 5

    futa "Huh?" (textbox="futa")
    
    show image "images/cg/@2/yoga/07.png":
        parallel:
            ease 3.0 xalign 0.25
        parallel:
            ease 3.0 yalign 0.7
    with Pause(2.0)

    $ dtb.setTextbox("futa", "right", 700, 250)
    $ dtb.setTextbox("roomie", "left", 1800, 700)

    futa "O-Oh, the party, right."
    futa "Uhm, yeah, I think it'll be... f-fun...?"

    roomie "Hm." (textbox="roomie")
    roomie "Not the {i}most{/i} believable you've ever sounded."

    show image "images/cg/@2/yoga/07.png":
        parallel:
            ease 2.0 xalign 0.5
        parallel:
            ease 2.0 yalign 0.5
        parallel:
            ease 2.0 zoom 1.5
    with Pause(1.0)

    $ dtb.setTextbox("futa", "right", 400, 500)
    $ dtb.setTextbox("roomie", "left", 1600, 600)

    futa "S-Sorry, I just... don't know..." (textbox="futa")

    roomie "Eh, it's fine. I get it." (textbox="roomie")
    roomie "But."
    roomie "I think you {i}will{/i} have fun."
    roomie "And hey, you'll get to mingle with some new people."

    futa "Mhm." (textbox="futa")
    
    show image "images/cg/@2/yoga/07.png":
        parallel:
            ease 3.0 xalign 0.9
        parallel:
            ease 3.0 yalign 0.4
        parallel:
            ease 3.0 zoom 1.9
    with Pause(2.0)

    $ dtb.setTextbox("roomie", "left", 1200, 700)

    roomie "..." (textbox="roomie")
    roomie "Say, I was wondering..."
    roomie "When was the last time you went on a date?"
    roomie "I know you've never been in a relationship, but, I mean..."
    roomie "Has anyone ever, like, asked you out?"
    roomie "Uh, sorry, that probably came out wrong."

    show image "images/cg/@2/yoga/07.png":
        parallel:
            ease 2.0 xalign 0.5
        parallel:
            ease 2.0 yalign 0.4
        parallel:
            ease 2.0 zoom 1.6
    with Pause(1.0)

    $ dtb.setTextbox("futa", "right", 400, 500)
    $ dtb.setTextbox("roomie", "left", 1700, 630)

    futa "I-It's okay." (textbox="futa")
    futa "Uhm..."
    futa "O-Once."

    roomie "Really?" (textbox="roomie")
    roomie "Can I ask... what happened?"

    futa "I... turned her down." (textbox="futa")
    
    roomie "Oh, I see. Was she not your type?" (textbox="roomie")

    futa "No, s-she was." (textbox="futa")
    futa "I was just..."

    show image "images/cg/@2/yoga/07.png":
        parallel:
            ease 2.0 xalign 0.35
        parallel:
            ease 2.0 yalign 0.55
        parallel:
            ease 2.0 zoom 1.8
    with None

    $ dtb.setTextbox("futa", "right", 600, 400)
    $ dtb.setTextbox("roomie", "left", 1850, 650)

    "Chloe trails off, her legs shifting a little closer together." (textbox="narrator_small")

    roomie "Oh... right." (textbox="roomie")
    roomie "Well, she sounds like she had good taste!"
    # [AR] Comment 6

    futa "Mm..." (textbox="futa")

    roomie "..." (textbox="roomie")
    roomie "Hey."

    show image "images/cg/@2/yoga/07.png":
        parallel:
            ease 10.0 xalign 0.5
        parallel:
            ease 10.0 yalign 0.5
        parallel:
            ease 10.0 zoom 1.0
    with None

    $ dtb.setTextbox("roomie", "left", 1450, 800)

    "Amy leans forwards in the bath a little, resting her hand on Chloe's."  (textbox="narrator_small")

    stop music fadeout 20.0

    show black:
        alpha 0.0
        ease 6.0 alpha 1.0
    with None

    roomie "I'm sure you'll find someone again." (textbox="roomie")

    scene black
    with Dissolve(0.75)

    roomie "You're... too cute not to."  (textbox="narrator_small", textbox_outline=True)

    # DEMO DEFINITELY NOT AFTER THIS POINT!

    stop music fadeout 3.0

    jump story

label start:
    camera:
        perspective True
    
    stop music fadeout 0.75

    scene black
    with Dissolve(0.75)

    pause 0.25

    # Use jump instead of call to prevent the thread/memory crash
    jump story 

# Create a new label for the ending sequence
label demo_end:

    play sound "sfx/item_click.wav"

    "Thank you for playing the demo of Benefitship: The Hallowed Wiener!" (textbox_variant="centered")

    play sound "sfx/item_click.wav"

    "Wishlist now to be notified when the full visual novel is released." (textbox_variant="centered")

    return