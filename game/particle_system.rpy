init python:
    import random
    
    # Modified version of Ren'Py SnowBlossom particle system.
    # Uses subpixeling for movement.
    # Fixes pop-in.
    # Fixes particles not being removed offscreen.
    @renpy.pure
    class CParticles(renpy.display.displayable.Displayable, NoRollback):
        """
        Supports particle motion, using the old API.
        """

        __version__ = 1

        nosave = [ 'particles' ]

        def after_upgrade(self, version):
            if version < 1:
                self.sm = SpriteManager(update=self.update_callback, predict=self.predict_callback)

        def after_setstate(self):
            self.particles = None

        def __init__(self, factory, **properties):
            """
            @param factory: A factory object.
            """

            super(CParticles, self).__init__(**properties)

            self.sm = SpriteManager(update=self.update_callback, predict=self.predict_callback)

            self.factory = factory
            self.particles = None

        def update_callback(self, st):
            global persistent
            if persistent.particles == "none":
                if self.particles is not None:
                    self.sm.destroy_all()
                    self.particles = None
                return 0

            particles = self.particles

            if st == 0 or particles is None:
                self.sm.destroy_all()
                particles = [ ]

            add_parts = self.factory.create(particles, st)

            new_particles = [ ]

            for sprite, p in particles:
                update = p.update(st)

                if update is None:
                    sprite.destroy()
                    continue

                x, y, _t, d = update

                if d is not sprite.cache.child:
                    sprite.set_child(d)

                sprite.x = x
                sprite.y = y

                new_particles.append((sprite, p))

            if add_parts:
                for p in add_parts:
                    update = p.update(st)

                    if update is None:
                        continue

                    x, y, _t, d = update

                    if d is None:
                        continue

                    sprite = self.sm.create(d)
                    sprite.x = x
                    sprite.y = y

                    new_particles.append((sprite, p))

            self.particles = new_particles

            return 0

        def predict_callback(self):
            return self.factory.predict()

        def render(self, w, h, st, at):
            #return renpy.display.render.render(self.sm, w, h, st, at) # ORIGINAL
            return renpy.display.render.render(self.sm, w, h, at, at) # Uses "at" as "st" to prevent pop-in

        def visit(self):
            return [ self.sm ]

    @renpy.pure
    class CSnowBlossomFactory(NoRollback):
        rotate = False

        def __setstate__(self, state):
            self.start = 0
            vars(self).update(state)
            self.init()

        def __init__(self, image, count, xspeed, yspeed, border, start, fast, rotate=False):
            self.image = renpy.easy.displayable(image)
            self.count = count
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border
            self.start = start
            self.fast = fast
            self.rotate = rotate
            self.init()

        def init(self):
            self.starts = [ random.uniform(0, self.start) for _i in range(0, self.count) ]  # W0201
            self.starts.append(self.start)
            self.starts.sort()

        def create(self, particles, st):
            def ranged(n):
                if isinstance(n, tuple):
                    return random.uniform(n[0], n[1])
                else:
                    return n

            if (st == 0) and not particles and self.fast:
                rv = [ ]

                for _i in range(0, self.count):
                    rv.append(CSnowBlossomParticle(self.image,
                                                ranged(self.xspeed),
                                                ranged(self.yspeed),
                                                self.border,
                                                st,
                                                random.uniform(0, 100),
                                                fast=True,
                                                rotate=self.rotate))
                return rv

            if particles is None or len(particles) < self.count:

                # Check to see if we have a particle ready to start. If not,
                # don't start it.
                if particles and st < self.starts[len(particles)]:
                    return None

                return [ CSnowBlossomParticle(self.image,
                                            ranged(self.xspeed),
                                            ranged(self.yspeed),
                                            self.border,
                                            st,
                                            random.uniform(0, 100),
                                            fast=False,
                                            rotate=self.rotate) ]

        def predict(self):
            return [ self.image ]

    @renpy.pure
    class CSnowBlossomParticle(NoRollback):
        def __init__(self, image, xspeed, yspeed, border, start, offset, fast, rotate):

            # safety.
            if yspeed == 0:
                yspeed = 1

            self.image = image
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border
            self.start = start
            self.offset = offset
            self.rotate = rotate

            if not rotate:
                sh = renpy.config.screen_height
                sw = renpy.config.screen_width
            else:
                sw = renpy.config.screen_height
                sh = renpy.config.screen_width

            if self.yspeed > 0:
                self.ystart = -border
            else:
                self.ystart = sh + border

            travel_time = (2.0 * border + sh) / abs(yspeed)

            xdist = xspeed * travel_time

            x0 = min(-xdist, 0)
            x1 = max(sw + xdist, sw)

            self.xstart = random.uniform(x0, x1)

            if fast:
                self.ystart = random.uniform(-border, sh + border)
                self.xstart = random.uniform(0, sw)

        def update(self, st):
            to = st - self.start

            xpos = self.xstart + to * self.xspeed
            ypos = self.ystart + to * self.yspeed

            # Y deletion
            if not self.rotate:
                sh = renpy.config.screen_height
            else:
                sh = renpy.config.screen_width

            if ypos > sh + self.border:
                return None

            if ypos < -self.border:
                return None
        
            # X deletion
            if not self.rotate:
                sw = renpy.config.screen_width
            else:
                sw = renpy.config.screen_height

            if xpos > sw + self.border:
                return None

            if xpos < -self.border:
                return None
            
            # New positions
            if not self.rotate:
                return xpos, ypos, to + self.offset, self.image
            else:
                return ypos, xpos, to + self.offset, self.image

    # NOTE: This @renpy.pure is SUPER impotrant.
    @renpy.pure
    def CSnowBlossom(d,
                    count=10,
                    border=50,
                    xspeed=(20, 50),
                    yspeed=(100, 200),
                    start=0,
                    fast=False,
                    horizontal=False):
        """
        :doc: sprites_extra

        The snowblossom effect moves multiple instances of a sprite up,
        down, left or right on the screen. When a sprite leaves the screen, it
        is returned to the start.

        `d`
            The displayable to use for the sprites.

        `border`
            The size of the border of the screen. The sprite is considered to be
            on the screen until it clears the border, ensuring that sprites do
            not disappear abruptly.

        `xspeed`, `yspeed`
            The speed at which the sprites move, in the horizontal and vertical
            directions, respectively. These can be a single number or a tuple of
            two numbers. In the latter case, each particle is assigned a random
            speed between the two numbers. The speeds can be positive or negative,
            as long as the second number in a tuple is larger than the first.

        `start`
            The delay, in seconds, before each particle is added. This can be
            allows the particles to start at the top of the screen, while not
            looking like a "wave" effect.

        `fast`
            If true, particles start in the center of the screen, rather than
            only at the edges.

        `horizontal`
            If true, particles appear on the left or right side of the screen,
            rather than the top or bottom.
            """

        # If going horizontal, swap the xspeed and the yspeed.
        if horizontal:
            xspeed, yspeed = yspeed, xspeed

        return CParticles(CSnowBlossomFactory(image=d,
                                            count=count,
                                            border=border,
                                            xspeed=xspeed,
                                            yspeed=yspeed,
                                            start=start,
                                            fast=fast,
                                            rotate=horizontal))
