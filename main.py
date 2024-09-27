"""
This module generates character profiles.

It saves profiles as SVG files using provided templates.
"""

import ast
import os
import random


from faker import Faker

import file_operations


def main():
    """Generate a character profile and save it as an SVG file."""
    faker = Faker('ru_RU')
    first_name = faker.first_name()
    last_name = faker.last_name()
    job = faker.job()
    town = faker.city()

    with open('letters_mapping.txt') as file:
        alphabet = ast.literal_eval(file.read())

    stats = {stat: random.randint(3, 18) for stat in
             ['strength', 'agility', 'endurance', 'intelligence', 'luck']}

    skills = [
        'Стремительный прыжок',
        'Электрический выстрел',
        'Ледяной удар',
        'Стремительный удар',
        'Кислотный взгляд',
        'Тайный побег',
        'Ледяной выстрел',
        'Огненный заряд'
    ]

    runic_skills = []

    for skill in skills:
        runic_letter = ""
        for letter in skill:
            runic_letter += alphabet.get(letter, letter)
        runic_skills.append(runic_letter)

    selected_skills = random.sample(runic_skills, k=3)

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'job': job,
        'town': town,
        'strength': stats['strength'],
        'agility': stats['agility'],
        'endurance': stats['endurance'],
        'intelligence': stats['intelligence'],
        'luck': stats['luck'],
        'skill_1': selected_skills[0],
        'skill_2': selected_skills[1],
        'skill_3': selected_skills[2],
    }
    cards_dir = os.path.join(os.path.dirname(__file__), 'Cards')

    os.makedirs(cards_dir, exist_ok=True)

    file_operations.render_template(
        'template.svg',
        f'{cards_dir}/{first_name} {last_name}.svg',
        context
    )


if __name__ == "__main__":
    for _ in range(10):
        main()
