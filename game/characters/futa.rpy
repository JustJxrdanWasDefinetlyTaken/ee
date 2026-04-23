# Futa
layeredimage futa_casual_1:
    yoffset 20
    subpixel True
    attribute clothed default

    group overlay multiple:
        attribute blush
        attribute sweat

    group face auto:
        attribute happy default

    group overlay multiple:
        attribute bulge
    
layeredimage futa_casual_2:
    yoffset 20
    subpixel True
    attribute nude default

    group overlay multiple:
        attribute overlay_blush

    group face auto:
        attribute embarrassed default

    group overlay multiple:
        attribute penis_flaccid
        attribute penis_erect
        attribute penis_erect_drip

layeredimage futa_yoga:
    yoffset 20
    subpixel True
    attribute base default

    group overlay multiple:
        attribute overlay_blush
        attribute overlay_sweat

    group face auto:
        attribute smiling default

    group crotch auto:
        attribute postsex
        attribute pants default
        attribute pants_erect
    
image futa casual_1 = LayeredImageProxy('futa_casual_1')#, parallax_anim(1.0))
image futa casual_2 = LayeredImageProxy('futa_casual_2')#, parallax_anim(1.0))
image futa yoga = LayeredImageProxy('futa_yoga')#, parallax_anim(1.0))
