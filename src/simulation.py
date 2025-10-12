
import pygame
import datetime
import os
from environment import Environment
from cell import Cell
from food import spawn_food_item
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, FONT_SIZE, TEXT_COLOR, UI_PANEL_HEIGHT

class Simulation:
    def __init__(self):
        self.environment = Environment()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + UI_PANEL_HEIGHT))
        pygame.display.set_caption("MicroLife Evolution Simulator")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)

        self.paused = False
        self.simulation_speed = 1.0 # Multiplier for simulation speed
        self.selected_cell = None

        # Statistics and Logging
        self.simulation_time = 0
        self.stats_history = {
            "time": [],
            "cell_count": [],
            "food_count": [],
            "avg_speed": [],
            "avg_sense_radius": [],
            "avg_energy_efficiency": []
        }
        self.log_file = self._setup_log_file()

    def _setup_log_file(self):
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = os.path.join(log_dir, f"simulation_log_{timestamp}.txt")
        return open(log_path, "w")

    def _log_event(self, event_type, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.log_file.write(f"[{timestamp}] [{event_type}] {message}\n")

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.paused = not self.paused
                self._log_event("CONTROL", f"Simulation {'paused' if self.paused else 'resumed'}")
            elif event.key == pygame.K_UP:
                self.simulation_speed = min(4.0, self.simulation_speed + 0.5)
                self._log_event("CONTROL", f"Simulation speed increased to {self.simulation_speed:.1f}x")
            elif event.key == pygame.K_DOWN:
                self.simulation_speed = max(0.5, self.simulation_speed - 0.5)
                self._log_event("CONTROL", f"Simulation speed decreased to {self.simulation_speed:.1f}x")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if mouse_y >= SCREEN_HEIGHT:  # Click in UI panel
                reset_button_width = 80
                reset_button_height = 30
                reset_button_x = SCREEN_WIDTH - reset_button_width - 10
                reset_button_y = SCREEN_HEIGHT + UI_PANEL_HEIGHT - reset_button_height - 10
                if reset_button_x <= mouse_x <= reset_button_x + reset_button_width and \
                   reset_button_y <= mouse_y <= reset_button_y + reset_button_height:
                    self.reset()
                    self._log_event("USER_ACTION", "Simulation reset")
                    return
            if mouse_y < SCREEN_HEIGHT: # Click in simulation area
                if event.button == 1: # Left click to spawn cell or select
                    if self.paused: # Only select cell when paused
                        self.selected_cell = None
                        for cell in self.environment.cells:
                            if (cell.x - cell.size <= mouse_x <= cell.x + cell.size) and \
                               (cell.y - cell.size <= mouse_y <= cell.y + cell.size):
                                self.selected_cell = cell
                                self._log_event("USER_ACTION", f"Cell selected at ({mouse_x}, {mouse_y})")
                                break
                        # No longer spawning individual cells with left click, only selection when paused
                    # else: # If not paused, no action for left click in simulation area
                    #     pass
                elif event.button == 3: # Right click to spawn food
                    new_food = spawn_food_item(mouse_x, mouse_y)
                    self.environment.food.append(new_food)
                    self._log_event("USER_ACTION", f"New food spawned at ({mouse_x}, {mouse_y})")

    def _collect_stats(self):
        self.simulation_time += 1
        self.stats_history["time"].append(self.simulation_time)
        self.stats_history["cell_count"].append(len(self.environment.cells))
        self.stats_history["food_count"].append(len(self.environment.food))

        if self.environment.cells:
            avg_speed = sum(c.speed for c in self.environment.cells) / len(self.environment.cells)
            avg_sense = sum(c.sense_radius for c in self.environment.cells) / len(self.environment.cells)
            avg_efficiency = sum(c.energy_efficiency for c in self.environment.cells) / len(self.environment.cells)
        else:
            avg_speed = 0
            avg_sense = 0
            avg_efficiency = 0

        self.stats_history["avg_speed"].append(avg_speed)
        self.stats_history["avg_sense_radius"].append(avg_sense)
        self.stats_history["avg_energy_efficiency"].append(avg_efficiency)

    def draw_ui(self):
        # Draw UI panel background
        pygame.draw.rect(self.screen, (50, 50, 50), (0, SCREEN_HEIGHT, SCREEN_WIDTH, UI_PANEL_HEIGHT))

        # Display population count
        cell_count_text = self.font.render(f"Cells: {len(self.environment.cells)}", True, TEXT_COLOR)
        self.screen.blit(cell_count_text, (10, SCREEN_HEIGHT + 10))

        food_count_text = self.font.render(f"Food: {len(self.environment.food)}", True, TEXT_COLOR)
        self.screen.blit(food_count_text, (10, SCREEN_HEIGHT + 30))

        # Display simulation status
        status_text = "PAUSED" if self.paused else f"Speed: {self.simulation_speed:.1f}x"
        status_render = self.font.render(status_text, True, TEXT_COLOR)
        self.screen.blit(status_render, (SCREEN_WIDTH - status_render.get_width() - 10, SCREEN_HEIGHT + 10))

        # Display average traits
        avg_speed = self.stats_history["avg_speed"][-1] if self.stats_history["avg_speed"] else 0
        avg_sense = self.stats_history["avg_sense_radius"][-1] if self.stats_history["avg_sense_radius"] else 0
        avg_efficiency = self.stats_history["avg_energy_efficiency"][-1] if self.stats_history["avg_energy_efficiency"] else 0

        avg_traits_text = self.font.render(f"Avg Speed: {avg_speed:.2f} | Avg Sense: {avg_sense:.2f} | Avg Eff: {avg_efficiency:.2f}", True, TEXT_COLOR)
        self.screen.blit(avg_traits_text, (10, SCREEN_HEIGHT + 50))

        # Display selected cell info
        if self.selected_cell:
            selected_info = self.font.render(f"Selected Cell: Clan {self.selected_cell.clan.id} E:{self.selected_cell.energy:.1f} S:{self.selected_cell.speed:.1f} R:{self.selected_cell.sense_radius:.1f} Eff:{self.selected_cell.energy_efficiency:.1f} Age:{self.selected_cell.age}", True, TEXT_COLOR)
            self.screen.blit(selected_info, (10, SCREEN_HEIGHT + 70))

        # Display clan information
        clan_info_y_start = SCREEN_HEIGHT + 10
        for i, clan in enumerate(self.environment.clans):
            clan_cells = [cell for cell in self.environment.cells if cell.clan.id == clan.id]
            clan_count = len(clan_cells)
            if clan_count > 0:
                clan_avg_speed = sum(c.speed for c in clan_cells) / clan_count
                clan_avg_sense = sum(c.sense_radius for c in clan_cells) / clan_count
                clan_avg_efficiency = sum(c.energy_efficiency for c in clan_cells) / clan_count
                clan_avg_size = sum(c.size for c in clan_cells) / clan_count
                clan_avg_lifespan = sum(c.lifespan for c in clan_cells) / clan_count
            else:
                clan_avg_speed = 0
                clan_avg_sense = 0
                clan_avg_efficiency = 0
                clan_avg_size = 0
                clan_avg_lifespan = 0

            clan_text = self.font.render(f"Clan {clan.id} ({clan_count}): Spd:{clan_avg_speed:.1f} Sen:{clan_avg_sense:.1f} Eff:{clan_avg_efficiency:.1f} Size:{clan_avg_size:.1f} Life:{clan_avg_lifespan:.0f}", True, clan.color)
            self.screen.blit(clan_text, (SCREEN_WIDTH // 2, clan_info_y_start + i * 20))

        # Draw reset button
        reset_button_width = 80
        reset_button_height = 30
        reset_button_x = SCREEN_WIDTH - reset_button_width - 10
        reset_button_y = SCREEN_HEIGHT + UI_PANEL_HEIGHT - reset_button_height - 10
        pygame.draw.rect(self.screen, (100, 100, 100), (reset_button_x, reset_button_y, reset_button_width, reset_button_height))
        reset_text = self.font.render("Reset", True, TEXT_COLOR)
        self.screen.blit(reset_text, (reset_button_x + (reset_button_width - reset_text.get_width()) // 2, reset_button_y + (reset_button_height - reset_text.get_height()) // 2))

    def reset(self):
        """Reset the simulation to initial state."""
        self.environment = Environment()
        self.paused = False
        self.simulation_speed = 1.0
        self.selected_cell = None
        self.simulation_time = 0
        self.stats_history = {
            "time": [],
            "cell_count": [],
            "food_count": [],
            "avg_speed": [],
            "avg_sense_radius": [],
            "avg_energy_efficiency": []
        }
        # Close old log file and create new one
        self.log_file.close()
        self.log_file = self._setup_log_file()
        self._log_event("SYSTEM", "Simulation reset")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self._log_event("SYSTEM", "Simulation quit by user")
                self.handle_input(event)

            if not self.paused:
                self._collect_stats()
                for _ in range(int(self.simulation_speed)):
                    self.environment.update()

            self.screen.fill((0, 0, 0))  # Clear simulation area
            self.environment.draw(self.screen)
            self.draw_ui()

            pygame.display.flip()
            self.clock.tick(FPS)

        self.log_file.close()
        pygame.quit()


