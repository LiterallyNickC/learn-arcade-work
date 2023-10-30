import arcade

arcade.open_window(800, 600, "City Skyline at dawn")

arcade.set_background_color(arcade.color.ORANGE_RED)

arcade.start_render()


arcade.draw_circle_filled(400, 100, 400, arcade.color.RED)
arcade.draw_circle_filled(400, 100, 375, arcade.color.ORANGE)

arcade.draw_rectangle_filled(0,0,1600,400, arcade.color.RED_DEVIL)
arcade.draw_rectangle_filled(0,0,1600,375, arcade.color.RED_ORANGE)

arcade.draw_rectangle_filled(700,0,200,800, arcade.color.BATTLESHIP_GREY)
arcade.draw_rectangle_filled(100,0,250,600, arcade.color.BATTLESHIP_GREY)
arcade.draw_rectangle_filled(400,0,150,600, arcade.color.BATTLESHIP_GREY)
arcade.draw_rectangle_filled(400,0,650,500, arcade.color.BATTLESHIP_GREY)

arcade.draw_rectangle_filled(200,0,200,700, arcade.color.BLACK)
arcade.draw_rectangle_filled(500,0,200,500, arcade.color.BLACK)
arcade.draw_rectangle_filled(700,0,150,600, arcade.color.BLACK)
arcade.draw_rectangle_filled(100,0,150,500, arcade.color.BLACK)

arcade.finish_render()

arcade.run()