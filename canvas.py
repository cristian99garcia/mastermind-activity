#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017, Cristian García <cristian99garcia@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from ball_box import BallBox
from origin_box import OriginBox
from center_box import CenterBox

import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class GridBalls(Gtk.Grid):

    def __init__(self):
        Gtk.Grid.__init__(self)

        self.balls = {}
        self.level = None

        self.reset()
        self.show_all()

    def clear(self):
        del self.balls
        self.balls = {}
        self.level = 0

        for x in range(0, 4):
            self.balls[x] = [None] * 10

    def reset(self):
        self.clear()

        x = -1
        y = 0

        for i in range(0, 40):
            x += 1

            if x >= 4:
                x = 0
                y += 1

            box = BallBox()
            self.attach(box, x, y, 1, 1)

            self.balls[x][9 - y] = box

        self.set_drag_level()
        self.show_all()

    def set_ball(self, x, y, ballid):
        self.balls[x][y].set_ball(ballid)

    def set_drag_level(self):
        for x in range(0, 4):
            for y in range(0, 9):
                ball = self.balls[x][y]
                ball.set_dest_drag(y == self.level)


class Canvas(Gtk.VBox):

    def __init__(self):
        Gtk.VBox.__init__(self)

        hbox = Gtk.HBox()
        self.pack_start(hbox, True, True, 0)

        finishbox = Gtk.VBox()
        hbox.pack_start(finishbox, True, True, 0)

        centerbox = CenterBox()
        hbox.pack_start(centerbox, True, True, 0)

        self.grid = GridBalls()
        centerbox.pack_start(self.grid, True, True, 0)

        originbox = OriginBox()
        self.pack_end(originbox, True, False, 0)

        self.show_all()


if __name__ == "__main__":
    win = Gtk.Window()
    win.set_title("Mastermind")
    win.connect("destroy", Gtk.main_quit)

    canvas = Canvas()
    win.add(canvas)

    win.show_all()
    Gtk.main()
