import random

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
            self.adjust_probabilities(1.25)
        if self.ultra_lucky:
            self.adjust_probabilities(1.375)

    def adjust_probabilities(self, multiplier):
        for unit in self.units:
            if unit != 'Rare':
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
        shiny_chance = 0.015
        if self.shiny_hunter:
            shiny_chance *= 2

        if unit in ["Mythic", "Secret"]:
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