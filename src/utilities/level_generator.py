import pygame
import tkinter as tk
from tkinter import filedialog
from config import BOARD_SIZE, TILE_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT

tk.Tk().withdraw()


# Función para mostrar el cuadro de diálogo de guardar archivo
def save_file_dialog(current_filename=None):
    if not current_filename:
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        return file_path
    else:
        return current_filename  # Devuelve el nombre de archivo existente para sobrescribirlo


def save_level(file_path, placed_objects, name="no_name"):
    with open(file_path, 'w') as file:

        with open("src/levels/level.template", "r") as templ_fle:
            level_content = templ_fle.read()

        # Ejemplo de cómo escribir los objetos colocados en el archivo
        for obj_type, pos in placed_objects.items():

            if obj_type == "froggy":
                _froggy_ = f"Froggy({pos[0]}, {pos[1]})"
            elif obj_type == "door":
                _door_ = f"Door({pos[0]}, {pos[1]})"
            elif obj_type == "bottles":
                _bottles_ = "[" + ", ".join(f"Bottle({p[0]}, {p[1]})" for p in placed_objects["bottles"]) + "]"
            elif obj_type == "rocks":
                _rocks_ = "[" + ", ".join(f"Rock({p[0]}, {p[1]})" for p in placed_objects["rocks"]) + "]"

        level_content = level_content.replace("_froggy_", _froggy_)
        level_content = level_content.replace("_door_", _door_)
        level_content = level_content.replace("_bottles_", _bottles_)
        level_content = level_content.replace("_rocks_", _rocks_)
        level_content = level_content.replace("_name_", name)

        file.write(level_content)


def remove_all_but(entity, objects, x, y):
    for k in objects.keys():
        if k != entity:
            if isinstance(objects[k], list):
                if (x, y) in objects[k]:
                    objects[k].remove((x, y))
            elif objects[k] == (x,y):
                objects[k] = None


def editor():
    # Initialize Pygame
    pygame.init()

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Load images
    froggy_img = pygame.image.load("assets/images/froggy.png")
    door_img = pygame.image.load("assets/images/closed_door.png")
    rock_img = pygame.image.load("assets/images/rock.png")
    bottle_img = pygame.image.load("assets/images/filled_bottle.png")
    remove_img = pygame.image.load("assets/images/remove.png")

    # Scale images
    froggy_img = pygame.transform.scale(froggy_img, (TILE_SIZE, TILE_SIZE))
    door_img = pygame.transform.scale(door_img, (TILE_SIZE, TILE_SIZE))
    rock_img = pygame.transform.scale(rock_img, (TILE_SIZE, TILE_SIZE))
    bottle_img = pygame.transform.scale(bottle_img, (TILE_SIZE, TILE_SIZE))

    # Game elements
    elements = {"1": froggy_img, "2": door_img, "3": rock_img, "4": bottle_img, "5": remove_img}
    selected_element = None
    placed_objects = {"froggy": None, "door": None, "bottles": [], "rocks": []}

    current_filename = None  # Variable para almacenar el nombre del archivo actual


    # Grid
    grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # Setup window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Level Editor")

    # Button class
    class Button:
        def __init__(self, x, y, width, height, text=None, color=WHITE):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text
            self.color = color

        def draw(self, win):
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
            if self.text:
                font = pygame.font.SysFont("comicsans", 40)
                text = font.render(self.text, 1, BLACK)
                win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        def is_over(self, pos):
            return self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height


    # Initialize buttons
    buttons = {
        "new": Button(50, WINDOW_HEIGHT - 60, 100, 50, "NEW"),
        "open": Button(200, WINDOW_HEIGHT - 60, 100, 50, "OPEN"),
        "save": Button(350, WINDOW_HEIGHT - 60, 100, 50, "SAVE"),
        "exit": Button(500, WINDOW_HEIGHT - 60, 100, 50, "EXIT")
    }

    # Main loop
    run = True
    while run:
        screen.fill(WHITE)

        # Draw grid
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                rect = pygame.Rect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 1)

        # Place froggy
        if placed_objects["froggy"] is not None:
            x, y = placed_objects["froggy"]
            screen.blit(froggy_img, (x * TILE_SIZE, y * TILE_SIZE))

        # Place door
        if placed_objects["door"] is not None:
            x, y = placed_objects["door"]
            screen.blit(door_img, (x * TILE_SIZE, y * TILE_SIZE))

        # Place rocks
        for pos in placed_objects["rocks"]:
            x, y = pos
            screen.blit(rock_img, (x * TILE_SIZE, y * TILE_SIZE))

        # Place bottles
        for pos in placed_objects["bottles"]:
            x, y = pos
            screen.blit(bottle_img, (x * TILE_SIZE, y * TILE_SIZE))

        # Draw buttons
        for button in buttons.values():
            button.draw(screen)

        if selected_element == "5":  # '5' es el código para "remove"
            # Define un cursor personalizado de cruz o usa uno predefinido
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)  # Ejemplo con un cursor predefinido
        else:
            # Vuelve al cursor predeterminado
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

            # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Check if a button is clicked
                for key, button in buttons.items():
                    if button.is_over(pos):
                        if key == "new":
                            grid = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
                            placed_objects = {"froggy": None, "door": None, "bottles": [], "rocks": []}
                        elif key == "open":
                            # Add your logic to open a file
                            pass
                        elif key == "save":
                            file_path = save_file_dialog(current_filename)
                            if file_path:  # Si el usuario no canceló el cuadro de diálogo
                                save_level(file_path, placed_objects)
                                current_filename = file_path  # Actualiza el nombre del archivo actual

                            pass
                        elif key == "exit":
                            run = False
                        break
                else:  # Handle clicks on the grid
                    x, y = pos[0] // TILE_SIZE, pos[1] // TILE_SIZE
                    if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE:
                        if selected_element == "1":  # Froggy
                            placed_objects["froggy"] = (x, y)
                            remove_all_but("froggy", placed_objects, x, y)

                        elif selected_element == "2":  # Door
                            placed_objects["door"] = (x, y)
                            remove_all_but("door", placed_objects, x, y)

                        elif selected_element == "3":  # Rock
                            placed_objects["rocks"].append((x, y))
                            remove_all_but("rocks", placed_objects, x, y)

                        elif selected_element == "4":  # Bottle
                            placed_objects["bottles"].append((x, y))
                            remove_all_but("bottles", placed_objects, x, y)

                        elif selected_element == "5":  # Remove
                            if (x, y) == placed_objects["froggy"]:
                                placed_objects["froggy"] = None
                            elif (x, y) == placed_objects["door"]:
                                placed_objects["door"] = None
                            elif (x, y) in placed_objects["rocks"]:
                                placed_objects["rocks"].remove((x, y))
                            elif (x, y) in placed_objects["bottles"]:
                                placed_objects["bottles"].remove((x, y))
                            grid[x][y] = None
                        else:
                            grid[x][y] = selected_element

            if event.type == pygame.KEYDOWN:
                if event.unicode in elements:
                    selected_element = event.unicode

        # Update display
        pygame.display.flip()

    pygame.quit()
