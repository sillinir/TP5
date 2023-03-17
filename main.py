"""
Rayna Sillini
TP5
Dessiner avec la librairie Arcade
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "TP5"


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "TP5")

    arcade.set_background_color(arcade.color.EERIE_BLACK)

    arcade.start_render()
    # DESSINER SOL
    arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4, SCREEN_WIDTH, SCREEN_HEIGHT / 2,
                                 arcade.color.DARK_GRAY)
    # DESSINER PLANETES
    arcade.draw_circle_filled(300, 600, 90, arcade.color.GUPPIE_GREEN)
    arcade.draw_circle_outline(300, 600, 90, arcade.color.BRUNSWICK_GREEN, 2)
    arcade.draw_arc_filled(400, SCREEN_HEIGHT / 2, 235, 235, arcade.csscolor.PURPLE, 0, 180)
    arcade.draw_arc_outline(400, SCREEN_HEIGHT / 2, 235, 235, arcade.csscolor.INDIGO, 0, 180, 2)
    arcade.draw_circle_filled(80, 500, 90, arcade.color.ORANGE_PEEL)
    arcade.draw_circle_outline(80, 500, 90, arcade.color.BURNT_ORANGE)
    arcade.draw_circle_filled(725, 470, 60, arcade.color.BLUE_SAPPHIRE)
    arcade.draw_circle_outline(725, 470, 60, arcade.color.MIDNIGHT_BLUE)

    # DESSINER PANNEAU
    line_list = [(100, 320), (100, 100)]
    arcade.draw_lines(line_list, arcade.color.GOLD, 3)
    y = SCREEN_HEIGHT / 2 + 40
    arcade.draw_triangle_filled(100, y + 60,
                                50, y - 20,
                                150, y - 20,
                                arcade.color.YELLOW)
    arcade.draw_text("moon", 80, 350, arcade.color.BLACK)
    arcade.draw_text("shuttle", 78, 330, arcade.color.BLACK)

    # DESSINER FUSEE
    arcade.draw_rectangle_filled(650, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2,
                                 arcade.color.GRAY)
    arcade.draw_ellipse_filled(650, SCREEN_HEIGHT / 2, 130, 170, arcade.color.LIGHT_BLUE)
    arcade.draw_ellipse_outline(650, SCREEN_HEIGHT / 2, 130, 170, arcade.color.DENIM, 2)
    points = [(650, 600), (540, 450), (760, 450)]
    arcade.draw_polygon_filled(points, arcade.color.RED_DEVIL)
    arcade.draw_triangle_filled(660, 150,
                                520, 30,
                                550, 150,
                                arcade.color.RED_DEVIL)
    arcade.draw_triangle_filled(750, 150,
                                780, 30,
                                640, 150,
                                arcade.color.RED_DEVIL)
    arcade.finish_render()

    arcade.run()


main()
