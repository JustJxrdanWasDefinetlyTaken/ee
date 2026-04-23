transform anim_particle_bathroom:
    subpixel True
    alpha 0.15
    zoom renpy.random.uniform(0.4, 0.6)
    rotate renpy.random.randint(0, 180)

    parallel:
        ease 6.0 rotate renpy.random.randint(0, 180)
        ease 6.0 rotate renpy.random.randint(0, 180)
        repeat

transform anim_particle_bathroom_far:
    subpixel True
    alpha 0.25
    zoom renpy.random.uniform(0.15, 0.3)
    rotate renpy.random.randint(0, 128)

    parallel:
        ease 6.0 rotate renpy.random.randint(0, 180)
        ease 6.0 rotate renpy.random.randint(0, 180)
        repeat

image particle_bathroom = CSnowBlossom(At("images/particles/particle_bathroom.png", anim_particle_bathroom), border=64, count=20, start=2.0, fast=True, yspeed=(-25, -15), xspeed=(-30, 30), horizontal=False)
image particle_bathroom_far = CSnowBlossom(At("images/particles/particle_bathroom.png", anim_particle_bathroom_far), border=64, count=50, start=2.0, fast=True, yspeed=(-10, -5), xspeed=(-15, 15), horizontal=False)