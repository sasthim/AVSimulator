from summon import Summon
from collections import Counter
from termcolor import colored

# User inputs
total_gems = 100000000
vip_status = True
shiny_hunter_status = False
super_lucky_status = False
ultra_lucky_status = False
# - - -


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

summon = Summon(
    unit_probabilities,
    vip=vip_status,
    shiny_hunter=shiny_hunter_status,
    super_lucky=super_lucky_status,
    ultra_lucky=ultra_lucky_status
)

results, total_summons, shiny_count = summon.simulate_summons(total_gems)

unit_count = Counter(results)

mythic_string = rainbow_text("Mythic: ")
secret_string = colored(f"Secret: ", 'red')

print(colored("\nSimulation Results:\n", 'cyan', attrs=['bold']))

print(colored(f"Gems spent: ", 'yellow') + f"{total_gems:,.0f}")
print(colored(f"Total summons: ", 'yellow') + f"{total_summons:,.0f}\n")

print(colored("Rare: ", 'blue') + f"{unit_count['Rare']:,.0f}")
print(colored("Epic: ", 'magenta') + f"{unit_count['Epic']:,.0f}")
print(colored("Legendary: ", 'light_yellow') + f"{unit_count['Legendary']:,.0f}")

print(colored(f"{mythic_string}", 'magenta', attrs=["bold"]) + f"{unit_count['Mythic']:,.0f}")
print(colored(f"{secret_string}", 'red', attrs=["bold", "dark"]) + f"{unit_count['Secret']:,.0f}\n")

print(colored(f"Shiny ", 'white', attrs=["bold", "dark"])+ mythic_string + f"{unit_count['Shiny Mythic']:,.0f}")
print(colored(f"Shiny {secret_string}", 'white', attrs=["bold", "dark"]) + f"{unit_count['Shiny Secret']:,.0f}")
print(colored("Shiny units obtained: ", 'white', attrs=["bold", "dark"]) + f"{shiny_count:,.0f}\n")

vip_color = 'green' if vip_status else 'red'
print(colored(f"VIP: ", 'white', attrs=['bold']) + colored(f"{vip_status}", vip_color, attrs=['bold']))

shiny_hunter_color = 'green' if shiny_hunter_status else 'red'
print(colored(f"Shiny Hunter: ", 'white', attrs=['bold']) + colored(f"{shiny_hunter_status}", shiny_hunter_color, attrs=['bold']))

super_lucky_color = 'green' if super_lucky_status else 'red'
print(colored(f"Super Lucky Potion: ", 'white', attrs=['bold']) + colored(f"{super_lucky_status}", super_lucky_color, attrs=['bold']))

ultra_lucky_color = 'green' if ultra_lucky_status else 'red'
print(colored(f"Ultra Lucky Potion: ", 'white', attrs=['bold']) + colored(f"{ultra_lucky_status}\n", ultra_lucky_color, attrs=['bold']))