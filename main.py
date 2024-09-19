import random
import sys
from collections import Counter
from termcolor import colored
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')  # Define a localidade para português do Brasil

class Summon:
    def __init__(self, units, cost_per_summon=50, vip=False, shiny_hunter=False, super_lucky=False, ultra_lucky=False):
        self.units = units
        self.base_cost_per_summon = cost_per_summon
        self.cost_per_summon = cost_per_summon * 0.8 if vip else cost_per_summon
        self.total_probability = sum(units.values())
        self.shiny_hunter = shiny_hunter
        self.super_lucky = super_lucky
        self.ultra_lucky = ultra_lucky

        if self.super_lucky:
            self.adjust_probabilities(1.25)  # 25% increase in rare unit chances
        if self.ultra_lucky:
            self.adjust_probabilities(1.375)  # 37.5% increase in rare unit chances

    def adjust_probabilities(self, multiplier):
        for unit in self.units:
            if unit != 'Rare':  # Increase only for rarer units (except 'Rare')
                self.units[unit] *= multiplier
        self.total_probability = sum(self.units.values())

    def summon_unit(self):
        choice = random.uniform(0, self.total_probability)
        cumulative = 0

        for unit, probability in self.units.items():
            cumulative += probability
            if choice <= cumulative:
                return unit

    def apply_shiny_chance(self, unit):
        shiny_chance = 0.015  # 1.5% chance for Mythic and Secret to be shiny
        if self.shiny_hunter:
            shiny_chance *= 2  # Increase shiny chance by 100% if Shiny Hunter is active

        if unit in ["Mythic", "Secret"]:  # Only Mythic and Secret can be shiny
            return f"Shiny {unit}" if random.random() < shiny_chance else unit
        return unit

    def simulate_summons(self, total_gems):
        number_of_summons = total_gems // self.cost_per_summon
        results = []
        shiny_results = 0

        for _ in range(int(number_of_summons)):
            unit = self.summon_unit()
            final_unit = self.apply_shiny_chance(unit)
            if "Shiny" in final_unit:
                shiny_results += 1
            results.append(final_unit)

        return results, number_of_summons, shiny_results

def rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    colored_text = ''.join(
        colored(char, colors[i % len(colors)], attrs=["bold"]) for i, char in enumerate(text)
    )
    return colored_text

unit_probabilities = {
    'Rare': 75.496,
    'Epic': 20,
    'Legendary': 4,
    'Mythic': 0.5,
    'Secret': 0.004
}

# User inputs
total_gems = 100000000
vip_status = True
shiny_hunter_status = False
super_lucky_status = False
ultra_lucky_status = False
# ----

summon = Summon(
    unit_probabilities,
    vip=vip_status,
    shiny_hunter=shiny_hunter_status,
    super_lucky=super_lucky_status,
    ultra_lucky=ultra_lucky_status
)

results, total_summons, shiny_count = summon.simulate_summons(total_gems)

# Count the occurrences of each unit
unit_count = Counter(results)

# Display the results using termcolor
print(colored("\nSimulation Results:\n", 'cyan', attrs=['bold']))

print(colored(f"Gems spent: ", 'yellow') + f"{total_gems:,.0f}")
print(colored(f"Total summons: ", 'yellow') + f"{total_summons:,.0f}\n")

print(colored("Rare: ", 'blue') + f"{unit_count['Rare']:,.0f}")
print(colored("Epic: ", 'magenta') + f"{unit_count['Epic']:,.0f}")
print(colored("Legendary: ", 'light_yellow') + f"{unit_count['Legendary']:,.0f}")
mythic_string = rainbow_text("Mythic")
print(colored(f"{mythic_string}: ", 'magenta', attrs=["bold"]) + f"{unit_count['Mythic']:,.0f}")
print(colored("Secret: ", 'red', attrs=["bold", "dark"]) + f"{unit_count['Secret']:,.0f}\n")

print(colored(f"Shiny ", 'white', attrs=["bold", "dark"]) + f"{mythic_string}: " + f"{unit_count['Shiny Mythic']:,.0f}")
print(colored("Shiny Secret: ", 'white', attrs=["bold", "dark"]) + f"{unit_count['Shiny Secret']:,.0f}")
print(colored("Shiny units obtained: ", 'white', attrs=["bold", "dark"]) + f"{shiny_count:,.0f}\n")

# ... (restante do seu código)

# Display VIP status with color based on value
vip_color = 'green' if vip_status else 'red'
print(colored(f"VIP: ", 'white', attrs=['bold']) + colored(f"{vip_status}", vip_color, attrs=['bold']))

# Display Shiny Hunter status with color based on value
shiny_hunter_color = 'green' if shiny_hunter_status else 'red'
print(colored(f"Shiny Hunter: ", 'white', attrs=['bold']) + colored(f"{shiny_hunter_status}", shiny_hunter_color, attrs=['bold']))

# Display Super Lucky Potion status with color based on value
super_lucky_color = 'green' if super_lucky_status else 'red'
print(colored(f"Super Lucky Potion: ", 'white', attrs=['bold']) + colored(f"{super_lucky_status}", super_lucky_color, attrs=['bold']))

# Display Ultra Lucky Potion status with color based on value
ultra_lucky_color = 'green' if ultra_lucky_status else 'red'
print(colored(f"Ultra Lucky Potion: ", 'white', attrs=['bold']) + colored(f"{ultra_lucky_status}\n", ultra_lucky_color, attrs=['bold']))