import pygame
import random
import sys

pygame.init()

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 760

PLAY_SIZE = 600
CELL_SIZE = 20
GRID_SIZE = PLAY_SIZE // CELL_SIZE

PLAY_X = (WINDOW_WIDTH - PLAY_SIZE) // 2
PLAY_Y = 100

SNAKE_SPEED = 10

BACKGROUND_COLOR = (15, 23, 42)
PLAY_AREA_COLOR = (25, 36, 56)
BORDER_COLOR = (71, 85, 105)

SNAKE_COLOR = (74, 222, 128)
SNAKE_HEAD_COLOR = (34, 197, 94)

FOOD_COLOR = (239, 68, 68)

TEXT_COLOR = (241, 245, 249)
SECONDARY_TEXT_COLOR = (148, 163, 184)

BUTTON_COLOR = (30, 41, 59)
BUTTON_SELECTED_COLOR = (37, 99, 235)
BUTTON_HOVER_COLOR = (51, 65, 85)

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font_title = pygame.font.SysFont("arial", 52, bold=True)
font_large = pygame.font.SysFont("arial", 36, bold=True)
font_medium = pygame.font.SysFont("arial", 25, bold=True)
font_small = pygame.font.SysFont("arial", 18)


def draw_text(text, font, color, x, y, center=True):
    surface = font.render(text, True, color)

    if center:
        rect = surface.get_rect(center=(x, y))
    else:
        rect = surface.get_rect(topleft=(x, y))

    screen.blit(surface, rect)


def draw_button(text, rect, selected=False, hovered=False):
    if selected:
        color = BUTTON_SELECTED_COLOR
    elif hovered:
        color = BUTTON_HOVER_COLOR
    else:
        color = BUTTON_COLOR

    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=14
    )

    pygame.draw.rect(
        screen,
        BORDER_COLOR,
        rect,
        width=2,
        border_radius=14
    )

    draw_text(
        text,
        font_medium,
        WHITE,
        rect.centerx,
        rect.centery
    )


def generate_food(snake):
    snake_positions = set(snake)
    available_cells = []

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            position = (x, y)

            if position not in snake_positions:
                available_cells.append(position)

    if not available_cells:
        return None

    return random.choice(available_cells)


def start_screen():
    selected_option = 0

    button_width = 300
    button_height = 65
    button_x = (WINDOW_WIDTH - button_width) // 2

    start_button = pygame.Rect(
        button_x,
        390,
        button_width,
        button_height
    )

    quit_button = pygame.Rect(
        button_x,
        475,
        button_width,
        button_height
    )

    buttons = [
        start_button,
        quit_button
    ]

    while True:
        mouse_position = pygame.mouse.get_pos()

        for index, button in enumerate(buttons):
            if button.collidepoint(mouse_position):
                selected_option = index

        screen.fill(BACKGROUND_COLOR)

        draw_text(
            "SNAKE",
            font_title,
            SNAKE_COLOR,
            WINDOW_WIDTH // 2,
            170
        )

        draw_text(
            "Modern Classic Snake Game",
            font_small,
            SECONDARY_TEXT_COLOR,
            WINDOW_WIDTH // 2,
            220
        )

        decoration_y = 285

        for i in range(6):
            color = SNAKE_HEAD_COLOR if i == 5 else SNAKE_COLOR

            pygame.draw.rect(
                screen,
                color,
                (
                    225 + i * 35,
                    decoration_y,
                    28,
                    28
                ),
                border_radius=7
            )

        pygame.draw.circle(
            screen,
            FOOD_COLOR,
            (470, decoration_y + 14),
            11
        )

        draw_button(
            "Start Game",
            start_button,
            selected_option == 0,
            start_button.collidepoint(mouse_position)
        )

        draw_button(
            "Quit Game",
            quit_button,
            selected_option == 1,
            quit_button.collidepoint(mouse_position)
        )

        draw_text(
            "UP / DOWN to select",
            font_small,
            SECONDARY_TEXT_COLOR,
            WINDOW_WIDTH // 2,
            580
        )

        draw_text(
            "ENTER to confirm",
            font_small,
            SECONDARY_TEXT_COLOR,
            WINDOW_WIDTH // 2,
            610
        )



        draw_text(
            "made by: abdulaziz alyousef",
            font_small,
            SECONDARY_TEXT_COLOR,
            WINDOW_WIDTH // 2,
            715
        )

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    selected_option -= 1

                    if selected_option < 0:
                        selected_option = 1

                elif event.key == pygame.K_DOWN:
                    selected_option += 1

                    if selected_option > 1:
                        selected_option = 0

                elif event.key == pygame.K_RETURN:

                    if selected_option == 0:
                        return

                    if selected_option == 1:
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    if start_button.collidepoint(event.pos):
                        return

                    if quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

        clock.tick(60)


def end_screen(score, win=False):
    selected_option = 0

    button_width = 300
    button_height = 65
    button_x = (WINDOW_WIDTH - button_width) // 2

    try_again_button = pygame.Rect(
        button_x,
        390,
        button_width,
        button_height
    )

    quit_button = pygame.Rect(
        button_x,
        475,
        button_width,
        button_height
    )

    buttons = [
        try_again_button,
        quit_button
    ]

    while True:
        mouse_position = pygame.mouse.get_pos()

        for index, button in enumerate(buttons):
            if button.collidepoint(mouse_position):
                selected_option = index

        screen.fill(BACKGROUND_COLOR)

        if win:
            draw_text(
                "YOU WIN!",
                font_title,
                SNAKE_COLOR,
                WINDOW_WIDTH // 2,
                170
            )

            draw_text(
                "You filled the entire board!",
                font_small,
                SECONDARY_TEXT_COLOR,
                WINDOW_WIDTH // 2,
                225
            )

        else:
            draw_text(
                "GAME OVER",
                font_title,
                FOOD_COLOR,
                WINDOW_WIDTH // 2,
                170
            )

            draw_text(
                "The snake has crashed.",
                font_small,
                SECONDARY_TEXT_COLOR,
                WINDOW_WIDTH // 2,
                225
            )

        draw_text(
            f"Score: {score}",
            font_large,
            TEXT_COLOR,
            WINDOW_WIDTH // 2,
            310
        )

        draw_button(
            "Try Again",
            try_again_button,
            selected_option == 0,
            try_again_button.collidepoint(mouse_position)
        )

        draw_button(
            "Quit",
            quit_button,
            selected_option == 1,
            quit_button.collidepoint(mouse_position)
        )

        draw_text(
            "UP / DOWN to select",
            font_small,
            SECONDARY_TEXT_COLOR,
            WINDOW_WIDTH // 2,
            580
        )

        draw_text(
            "ENTER to confirm",
            font_small,
            SECONDARY_TEXT_COLOR,
            WINDOW_WIDTH // 2,
            610
        )



        draw_text(
            "made by: abdulaziz alyousef",
            font_small,
            SECONDARY_TEXT_COLOR,
            WINDOW_WIDTH // 2,
            715
        )

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    selected_option -= 1

                    if selected_option < 0:
                        selected_option = 1

                elif event.key == pygame.K_DOWN:
                    selected_option += 1

                    if selected_option > 1:
                        selected_option = 0

                elif event.key == pygame.K_RETURN:

                    if selected_option == 0:
                        return

                    if selected_option == 1:
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    if try_again_button.collidepoint(event.pos):
                        return

                    if quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

        clock.tick(60)


def draw_game(snake, food, score):
    screen.fill(BACKGROUND_COLOR)

    draw_text(
        f"Score: {score}",
        font_medium,
        TEXT_COLOR,
        PLAY_X,
        45,
        center=False
    )

    draw_text(
        "SNAKE",
        font_medium,
        SNAKE_COLOR,
        WINDOW_WIDTH - 95,
        58
    )

    play_rect = pygame.Rect(
        PLAY_X,
        PLAY_Y,
        PLAY_SIZE,
        PLAY_SIZE
    )

    pygame.draw.rect(
        screen,
        PLAY_AREA_COLOR,
        play_rect,
        border_radius=8
    )

    pygame.draw.rect(
        screen,
        BORDER_COLOR,
        play_rect,
        width=3,
        border_radius=8
    )

    grid_color = (30, 43, 64)

    for x in range(
        PLAY_X + CELL_SIZE,
        PLAY_X + PLAY_SIZE,
        CELL_SIZE
    ):
        pygame.draw.line(
            screen,
            grid_color,
            (x, PLAY_Y),
            (x, PLAY_Y + PLAY_SIZE)
        )

    for y in range(
        PLAY_Y + CELL_SIZE,
        PLAY_Y + PLAY_SIZE,
        CELL_SIZE
    ):
        pygame.draw.line(
            screen,
            grid_color,
            (PLAY_X, y),
            (PLAY_X + PLAY_SIZE, y)
        )

    if food is not None:
        food_x, food_y = food

        food_center_x = (
            PLAY_X
            + food_x * CELL_SIZE
            + CELL_SIZE // 2
        )

        food_center_y = (
            PLAY_Y
            + food_y * CELL_SIZE
            + CELL_SIZE // 2
        )

        pygame.draw.circle(
            screen,
            FOOD_COLOR,
            (food_center_x, food_center_y),
            CELL_SIZE // 2 - 3
        )

    for index, segment in enumerate(snake):
        x, y = segment

        segment_rect = pygame.Rect(
            PLAY_X + x * CELL_SIZE + 2,
            PLAY_Y + y * CELL_SIZE + 2,
            CELL_SIZE - 4,
            CELL_SIZE - 4
        )

        if index == 0:
            pygame.draw.rect(
                screen,
                SNAKE_HEAD_COLOR,
                segment_rect,
                border_radius=6
            )

        else:
            pygame.draw.rect(
                screen,
                SNAKE_COLOR,
                segment_rect,
                border_radius=5
            )

    draw_text(
        "made by: abdulaziz alyousef",
        font_small,
        SECONDARY_TEXT_COLOR,
        WINDOW_WIDTH // 2,
        730
    )

    pygame.display.flip()


def game():
    center_x = GRID_SIZE // 2
    center_y = GRID_SIZE // 2

    snake = [
        (center_x, center_y),
        (center_x - 1, center_y),
        (center_x - 2, center_y)
    ]

    direction = (1, 0)
    next_direction = direction

    food = generate_food(snake)

    score = 0

    move_timer = 0
    move_delay = 1000 // SNAKE_SPEED

    while True:
        delta_time = clock.tick(60)
        move_timer += delta_time

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    if direction != (0, 1):
                        next_direction = (0, -1)

                elif event.key == pygame.K_DOWN:
                    if direction != (0, -1):
                        next_direction = (0, 1)

                elif event.key == pygame.K_LEFT:
                    if direction != (1, 0):
                        next_direction = (-1, 0)

                elif event.key == pygame.K_RIGHT:
                    if direction != (-1, 0):
                        next_direction = (1, 0)

        if move_timer >= move_delay:
            move_timer = 0

            direction = next_direction

            head_x, head_y = snake[0]

            new_head = (
                head_x + direction[0],
                head_y + direction[1]
            )

            new_x, new_y = new_head

            if (
                new_x < 0
                or new_x >= GRID_SIZE
                or new_y < 0
                or new_y >= GRID_SIZE
            ):
                return score, False

            eating_food = new_head == food

            if eating_food:
                body_to_check = snake
            else:
                body_to_check = snake[:-1]

            if new_head in body_to_check:
                return score, False

            snake.insert(0, new_head)

            if eating_food:
                score += 1

                food = generate_food(snake)

                if food is None:
                    return score, True

            else:
                snake.pop()

        draw_game(
            snake,
            food,
            score
        )


def main():
    start_screen()

    while True:
        score, win = game()
        end_screen(score, win)


if __name__ == "__main__":
    main()