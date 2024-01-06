import sys
import pygame


pygame.font.init()
pygame.display.set_caption("Minecraft Server Launcher")
pygame.display.set_icon(pygame.image.load("resources/icon.png"))

width = 960
height = 512
button1_color = (0, 0, 0)
button2_color = (0, 0, 0)
button3_color = (0, 0, 0)
button4_color = (0, 0, 0)
button_height = 100
button_width = width // 2 - 20
button_distanse_from_edge = 15
button_y = height // 2 - 10
button_border_radius = 2
small_button_height = button_height // 3
small_button_distanse_from_button = 15
button1_3_x = button_distanse_from_edge
button2_4_x = width - button_width - button_distanse_from_edge
button1_2_y = button_y - button_height // 2
button3_4_y = button_y + button_height // 2 + small_button_distanse_from_button
margin_buttom_of_text = 1
font_path = "resources/minecraft_font.ttf"
font_big = pygame.font.Font(font_path, 36)
font_small = pygame.font.Font(font_path, 20)
button1_text = font_big.render("Start server", True, (255, 255, 255))
button2_text = font_big.render("Change world", True, (255, 255, 255))
button3_text = font_small.render("Open server folder", True, (255, 255, 255))
button4_text = font_small.render("Open documentation", True, (255, 255, 255))
dirt_image = pygame.image.load("resources/dirt.png")
dirt_image_resize_amount = 4
big_button_texture = pygame.transform.scale(pygame.image.load("resources/big_button_texture.png"), (button_width - button_border_radius * 2, button_height - button_border_radius * 2))
small_button_texture = pygame.transform.scale(pygame.image.load("resources/small_button_texture.png"), (button_width - button_border_radius * 2, small_button_height - button_border_radius * 2))
dirt_image = pygame.transform.scale(dirt_image, (dirt_image.get_width() * dirt_image_resize_amount, dirt_image.get_height() * dirt_image_resize_amount))
screen = pygame.display.set_mode((width, height))
surface = pygame.Surface((width, height))


while True:
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif mouse_x > button1_3_x and mouse_x < button1_3_x + button_width and mouse_y > button1_2_y and mouse_y < button1_2_y + button_height:
            button1_color = (255, 255, 255)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("1")
        elif mouse_x > button2_4_x and mouse_x < button2_4_x + button_width and mouse_y > button1_2_y and mouse_y < button1_2_y + button_height:
            button2_color = (255, 255, 255)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("2")
        elif mouse_x > button1_3_x and mouse_x < button1_3_x + button_width and mouse_y > button3_4_y and mouse_y < button3_4_y + button_height:
            button3_color = (255, 255, 255)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("3")
        elif mouse_x > button2_4_x and mouse_x < button2_4_x + button_width and mouse_y > button3_4_y and mouse_y < button3_4_y + button_height:
            button4_color = (255, 255, 255)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("4")
        else:
            button1_color = (0, 0, 0)
            button2_color = (0, 0, 0)
            button3_color = (0, 0, 0)
            button4_color = (0, 0, 0)



    for i in range(height // 16):
        for j in range(width // 16):
            surface.blit(dirt_image, dirt_image.get_rect(topleft=(j * 16 * dirt_image_resize_amount, i * 16 * dirt_image_resize_amount)))


    pygame.draw.rect(surface, button1_color, (button1_3_x, button1_2_y, button_width, button_height))
    pygame.draw.rect(surface, button2_color, (button2_4_x, button1_2_y, button_width, button_height))
    pygame.draw.rect(surface, button3_color, (button1_3_x, button3_4_y, button_width, small_button_height))
    pygame.draw.rect(surface, button4_color, (button2_4_x, button3_4_y, button_width, small_button_height))

    surface.blit(big_button_texture, (button1_3_x + button_border_radius, button1_2_y + button_border_radius, button_width - button_border_radius * 2, button_height - button_border_radius * 2))
    surface.blit(big_button_texture, (button2_4_x + button_border_radius, button1_2_y + button_border_radius, button_width - button_border_radius * 2, button_height - button_border_radius * 2))
    surface.blit(small_button_texture, (button1_3_x + button_border_radius, button3_4_y + button_border_radius, button_width - button_border_radius * 2, small_button_height - button_border_radius * 2))
    surface.blit(small_button_texture, (button2_4_x + button_border_radius, button3_4_y + button_border_radius, button_width - button_border_radius * 2, small_button_height - button_border_radius * 2))

    surface.blit(button1_text, (button1_3_x + (button_width - button1_text.get_width()) // 2, button_y - button_height // 2 + button_height // 2 - button1_text.get_height() // 2 - margin_buttom_of_text))
    surface.blit(button2_text, (button2_4_x + (button_width - button2_text.get_width()) // 2, button_y - button_height // 2 + button_height // 2 - button2_text.get_height() // 2))
    surface.blit(button3_text, (button1_3_x + (button_width - button3_text.get_width()) // 2, button_y + button_height // 2 + small_button_distanse_from_button + small_button_height // 2 - button3_text.get_height() // 2 - margin_buttom_of_text))
    surface.blit(button4_text, (button2_4_x + (button_width - button4_text.get_width()) // 2, button_y + button_height // 2 + small_button_distanse_from_button + small_button_height // 2 - button4_text.get_height() // 2 - margin_buttom_of_text))
