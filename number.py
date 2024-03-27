import pygame
import random
import os
import time

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

BLACK = (0, 175, 0)
TABLE_COLOR = (0, 128, 0)  # Green color for the table

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Callbridge Card Game")


#number
font = pygame.font.Font(None, 36)
def display_text(number, x, y):
    text_surface = font.render(str(number), True, (255, 255, 255))
    screen.blit(text_surface, (x, y)) 



def load_card_images(scale_factor=0.2):
    cards = {}
    suits = ['spades', 'diamonds', 'clubs', 'hearts']
    values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    for suit in suits:
        for value in values:
            img_path = os.path.join('cards', suit, f'{value}.jpg')
            card_image = pygame.image.load(img_path)
            card_image = pygame.transform.scale(card_image, (int(card_image.get_width() * scale_factor), int(card_image.get_height() * scale_factor)))
            cards[(value, suit)] = card_image
    return cards

def create_shuffled_deck():
    deck = []
    suits = ['spades', 'diamonds', 'clubs', 'hearts']
    values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    for value in values:
        for suit in suits:
            deck.append((value, suit))
    random.shuffle(deck)
    return deck


def deal_cards(deck, num_players):
    value_order = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    sorted_deck = sorted(deck, key=lambda card: (card[1], value_order.index(card[0])))
    hands = [[] for _ in range(num_players)]
    for i, card in enumerate(sorted_deck):
        hands[i % num_players].append(card)
    random.shuffle(hands)
    return hands

card_images = load_card_images()

deck = create_shuffled_deck()

num_players = 4

player_hands = deal_cards(deck, num_players)


running = True

#number
number_to_display = 0
clock = pygame.time.Clock()
clicked = False
start = time.time()
end = 0
fps = 0
frames = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #number
        elif event.type == pygame.MOUSEBUTTONDOWN:
            number_to_display += 1
            clicked = True

    screen.fill(BLACK)
    table_width = 400
    table_height = 300
    table_x = (SCREEN_WIDTH - table_width) / 1.90
    table_y = (SCREEN_HEIGHT - table_height) / 2.85
    pygame.draw.rect(screen, TABLE_COLOR, (table_x, table_y, table_width, table_height))
    
    card_width, card_height = card_images[('2', 'spades')].get_size()
    padding = 40
    for i, hand in enumerate(player_hands):
        for j, card in enumerate(hand):
            card_image = card_images[card]
            if i == 0:  #East
                x = (SCREEN_WIDTH / 11)
                y = (SCREEN_HEIGHT / 2.75) - ((len(hand) - 1) * padding / 2) + (j * padding)
                screen.blit(pygame.transform.rotate(card_image, 90), (x, y))
            elif i == 1:  #West
                x = (SCREEN_WIDTH - card_height - (SCREEN_WIDTH / 15))
                y = (SCREEN_HEIGHT / 2.75) - ((len(hand) - 1) * padding / 2) + (j * padding)
                screen.blit(pygame.transform.rotate(card_image, -90), (x, y))
            elif i == 2:  #North
                x = (SCREEN_WIDTH / 2.14) - ((len(hand) - 1) * padding / 2) + (j * padding)
                y = (SCREEN_HEIGHT / 1.55)
                screen.blit(card_image, (x, y))
            else:  #South
                x = (SCREEN_WIDTH / 2.14) - ((len(hand) - 1) * padding / 2) + (j * padding)
                y = (SCREEN_HEIGHT / 20)
                screen.blit(card_image, (x, y))
    card_imag = pygame.image.load('2.jpg')
    card_imag1 = pygame.image.load('6.jpg')
    card_imag2 = pygame.image.load('J.jpg')
    card_imag3 = pygame.image.load('A.jpg')
    card_img = pygame.transform.scale(card_imag, (int(card_imag.get_width() * 0.2), int(card_imag.get_height() * 0.2)))
    card_img1 = pygame.transform.scale(card_imag1, (int(card_imag1.get_width() * 0.2), int(card_imag1.get_height() * 0.2)))
    card_img2 = pygame.transform.scale(card_imag2, (int(card_imag2.get_width() * 0.2), int(card_imag2.get_height() * 0.2)))
    card_img3 = pygame.transform.scale(card_imag3, (int(card_imag3.get_width() * 0.2), int(card_imag3.get_height() * 0.2)))
    screen.blit(card_img, (450, 335))
    screen.blit(card_img1, (350, 275))
    screen.blit(card_img2, (450, 185))
    screen.blit(card_img3, (550, 275))

    if clicked:
        # fps = clock.get_fps()
        display_text("FPS: {:.2f}".format(fps), 10, 10)
        
    
    display_text("Number: {}".format(number_to_display), 800, 650)

    pygame.display.update()
    end = time.time()
    frames += 1
    if (end - start) >= 1:
        fps = frames
        frames = 0
        start = time.time()
