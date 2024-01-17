import pygame
import sys
import subprocess
import os
import webbrowser


pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Minecraft Server Launcher")
pygame.display.set_icon(pygame.image.load("resources/icon.png"))

width_default = 960
height_default = 512
width = width_default
height = height_default
white = (255, 255, 255)
black = (0, 0, 0)
button1_color = black
button2_color = black
button3_color = black
button4_color = black
button_height = 100
button_width_default = width_default // 2 - 20
button_width = button_width_default
space_between_buttons_and_center_width = 5
button_border_radius = 2
small_button_height = button_height // 3
small_button_distanse_from_button = 10
margin_buttom_of_text = 1
font_path = "resources/minecraft_font.ttf"
font_big = pygame.font.Font(font_path, 36)
font_small = pygame.font.Font(font_path, 20)
font_for_button_results = pygame.font.Font(font_path, 22)
button1_text = font_big.render("Start server", True, white)
button2_text = font_big.render("Change world", True, white)
button3_text = font_small.render("Open server folder", True, white)
button4_text = font_small.render("Open documentation", True, white)
dirt_image = pygame.image.load("resources/dirt.png")
dirt_image_resize_amount = 4
dirt_image_size = 16
big_button_texture = pygame.transform.scale(pygame.image.load("resources/big_button_texture.png"), (button_width - button_border_radius * 2, button_height - button_border_radius * 2))
small_button_texture = pygame.transform.scale(pygame.image.load("resources/small_button_texture.png"), (button_width - button_border_radius * 2, small_button_height - button_border_radius * 2))
dirt_image = pygame.transform.scale(dirt_image, (dirt_image.get_width() * dirt_image_resize_amount, dirt_image.get_height() * dirt_image_resize_amount))
click_sound = pygame.mixer.Sound("resources/click.ogg")
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
surface = pygame.Surface((width, height))


while True:
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    width = screen.get_size()[0]
    height = screen.get_size()[1]
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    surface = pygame.Surface((width, height))
    button_y = height // 2 - 10
    button1_3_x = width // 2 - button_width - space_between_buttons_and_center_width
    button2_4_x = width // 2 + space_between_buttons_and_center_width
    button1_2_y = button_y - button_height // 2
    button3_4_y = button_y + button_height // 2 + small_button_distanse_from_button

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif mouse_x > button1_3_x and mouse_x < button1_3_x + button_width and mouse_y > button1_2_y and mouse_y < button1_2_y + button_height:
            button1_color = white
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play(0)
                result = subprocess.run(["sh", "sh/start-server.sh"], stdout=subprocess.PIPE)
                button1_text = font_for_button_results.render(result.stdout.decode()[:-1], True, (white))
                if result.stdout.decode()[:-1] == "Server started":
                    subprocess.Popen(["(cd ../ && java -jar server.jar)"], shell=True)
        elif mouse_x > button2_4_x and mouse_x < button2_4_x + button_width and mouse_y > button1_2_y and mouse_y < button1_2_y + button_height:
            button2_color = white
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play(0)
                result = subprocess.run(["sh", "sh/change-world.sh"], stdout=subprocess.PIPE)
                button2_text = font_for_button_results.render(result.stdout.decode()[:-1], True, (white))
        elif mouse_x > button1_3_x and mouse_x < button1_3_x + button_width and mouse_y > button3_4_y and mouse_y < button3_4_y + button_height:
            button3_color = white
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play(0)
                os.system("open ..")
        elif mouse_x > button2_4_x and mouse_x < button2_4_x + button_width and mouse_y > button3_4_y and mouse_y < button3_4_y + button_height:
            button4_color = white
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play(0)
                webbrowser.open("https://slavchik.net/all/MCSL")
        else:
            button1_color = black
            button2_color = black
            button3_color = black
            button4_color = black
            button1_text = font_big.render("Start server", True, (white))
            button2_text = font_big.render("Change world", True, (white))
            button3_text = font_small.render("Open server folder", True, (white))
            button4_text = font_small.render("Open documentation", True, (white))
            button_width = button_width_default

    for h in range(height // dirt_image_size):
        for w in range(width // dirt_image_size):
            surface.blit(dirt_image, dirt_image.get_rect(topleft=(w * dirt_image_size * dirt_image_resize_amount, h * dirt_image_size * dirt_image_resize_amount)))


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
