transform anim_particle_living_room:
    subpixel True
    alpha 0.15
    zoom renpy.random.uniform(0.4, 0.6)
    rotate renpy.random.randint(0, 180)

    parallel:
        ease 6.0 rotate renpy.random.randint(0, 180)
        ease 6.0 rotate renpy.random.randint(0, 180)
        repeat

transform anim_particle_living_room_far:
    subpixel True
    alpha 0.25
    zoom renpy.random.uniform(0.15, 0.3)
    rotate renpy.random.randint(0, 128)

    parallel:
        ease 6.0 rotate renpy.random.randint(0, 180)
        ease 6.0 rotate renpy.random.randint(0, 180)
        repeat

image particle_living_room = CSnowBlossom(At("images/particles/particle_living_room.png", anim_particle_living_room), border=64, count=20, start=2.0, fast=True, yspeed=(-25, -15), xspeed=(-30, 30), horizontal=False)
image particle_living_room_far = CSnowBlossom(At("images/particles/particle_living_room.png", anim_particle_living_room_far), border=64, count=50, start=2.0, fast=True, yspeed=(-10, -5), xspeed=(-15, 15), horizontal=False)