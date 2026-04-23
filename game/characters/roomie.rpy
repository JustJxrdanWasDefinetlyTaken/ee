# Roomie
layeredimage roomie_casual_1:
    yoffset 20
    subpixel True
    attribute clothed default

    group overlay multiple:
        attribute blush

    group face auto:
        attribute happy default

layeredimage roomie_yoga:
    yoffset 20
    subpixel True

    group arm_back:
        attribute arm_back_straight:
            "roomie_yoga_arm_back_straight"
        attribute arm_back_bent default:
            "roomie_yoga_arm_back_bent"

    attribute base default

    group crotch auto:
        attribute shorts default
        attribute shorts_torn
        attribute shorts_belly
        attribute belly

    group arm_front:
        attribute arm_front_belly:
            "roomie_yoga_arm_front_belly"
        attribute arm_front_bent default:
            "roomie_yoga_arm_front_bent"

    group overlay multiple:
        attribute overlay_blush
        attribute overlay_sweat

    group face auto:
        attribute smiling default
    
layeredimage roomie_casual_3:
    yoffset 20
    subpixel True
    attribute nude default

    group overlay multiple:
        attribute blush
        attribute sweat

    group face auto:
        attribute smile default


image roomie casual_1 = LayeredImageProxy('roomie_casual_1')#, parallax_anim(1.0))
image roomie yoga = LayeredImageProxy('roomie_yoga')#, parallax_anim(1.0))
image roomie casual_3 = LayeredImageProxy('roomie_casual_3')#, parallax_anim(1.0))
