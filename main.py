import sys
import pygame


pygame.font.init()
pygame.display.set_caption("Minecraft Server Launcher")
pygame.display.set_icon(pygame.image.load("resources/icon.png"))

width = 960
height = 512
button_color = (0, 0, 0)
button_height = 100
button_width = width // 2 - 20
button_distanse_from_adge = 15
button_y = height // 2 - 10
button_border_radius = 2
small_button_height = button_height // 3
small_button_distanse_from_button = 15
margin_button_of_text = 1
font_path = "resources/minecraft_font.ttf"
font_big = pygame.font.Font(font_path, 36)
font_small = pygame.font.Font(font_path, 24)
dirt_image = pygame.image.load("resources/dirt.png")
dirt_image_resize_amount = 4
big_button_texture = pygame.image.load("resources/big_button_texture.png")
big_button_texture = pygame.transform.scale(big_button_texture, (button_width - button_border_radius * 2, button_height - button_border_radius * 2))
small_button_texture = pygame.image.load("resources/small_button_texture.png")
small_button_texture = pygame.transform.scale(small_button_texture, (button_width - button_border_radius * 2, small_button_height - button_border_radius * 2))
dirt_image = pygame.transform.scale(dirt_image, (dirt_image.get_width() * dirt_image_resize_amount, dirt_image.get_height() * dirt_image_resize_amount))
screen = pygame.display.set_mode((width, height))
surface = pygame.Surface((width, height))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(surface, (0, 0))
    pygame.display.flip()

    for i in range(height // 16):
        for j in range(width // 16):
            surface.blit(dirt_image, dirt_image.get_rect(topleft=(j * 16 * dirt_image_resize_amount, i * 16 * dirt_image_resize_amount)))

    pygame.draw.rect(surface, button_color, (button_distanse_from_adge, button_y - button_height // 2, button_width, button_height))
    pygame.draw.rect(surface, button_color, (width - button_width - button_distanse_from_adge, button_y - button_height // 2, button_width, button_height))
    pygame.draw.rect(surface, button_color, (button_distanse_from_adge, button_y + button_height // 2 + small_button_distanse_from_button, button_width, small_button_height))
    pygame.draw.rect(surface, button_color, (width - button_width - button_distanse_from_adge, button_y + button_height // 2 + small_button_distanse_from_button, button_width, small_button_height))

    surface.blit(big_button_texture, (button_distanse_from_adge + button_border_radius, button_y - button_height // 2 + button_border_radius, button_width - button_border_radius * 2, button_height - button_border_radius * 2))
    surface.blit(big_button_texture, (width - button_width - button_distanse_from_adge + button_border_radius, button_y - button_height // 2 + button_border_radius, button_width - button_border_radius * 2, button_height - button_border_radius * 2))
    surface.blit(small_button_texture, (button_distanse_from_adge + button_border_radius, button_y + button_height // 2 + small_button_distanse_from_button + button_border_radius, button_width - button_border_radius * 2, small_button_height - button_border_radius * 2))
    surface.blit(small_button_texture, (width - button_width - button_distanse_from_adge + button_border_radius, button_y + button_height // 2 + small_button_distanse_from_button + button_border_radius, button_width - button_border_radius * 2, small_button_height - button_border_radius * 2))

    button1_text = font_big.render("Button 1", True, (255, 255, 255))
    button2_text = font_big.render("Button 2", True, (255, 255, 255))
    button3_text = font_small.render("Button 3", True, (255, 255, 255))
    button4_text = font_small.render("Button 4", True, (255, 255, 255))

    surface.blit(button1_text, (button_distanse_from_adge + button_width // 2 - button1_text.get_width() // 2, button_y - button_height // 2 + button_height // 2 - button1_text.get_height() // 2 - margin_button_of_text))
    surface.blit(button2_text, (width - button_width - button_distanse_from_adge + button_width // 2 - button2_text.get_width() // 2, button_y - button_height // 2 + button_height // 2 - button2_text.get_height() // 2))
    surface.blit(button3_text, (button_distanse_from_adge + button_width // 2 - button3_text.get_width() // 2, button_y + button_height // 2 + small_button_distanse_from_button + small_button_height // 2 - button3_text.get_height() // 2 - margin_button_of_text))
    surface.blit(button4_text, (width - button_width - button_distanse_from_adge + button_width // 2 - button4_text.get_width() // 2, button_y + button_height // 2 + small_button_distanse_from_button + small_button_height // 2 - button4_text.get_height() // 2 - margin_button_of_text))
