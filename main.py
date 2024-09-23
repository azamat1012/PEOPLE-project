import file_operations
from faker import Faker
from pathlib import Path
import random
import ast


def main():

    faker = Faker('ru_RU')
    first_name = faker.first_name()
    last_name = faker.last_name()
    job = faker.job()
    town = faker.city()

    with open('HUMANS project/letters_mapping.txt') as file:
        alphabet = file.read()
    alphabet = ast.literal_eval(alphabet)

    random_strength = random.randint(3, 18)
    random_agility = random.randint(3, 18)
    random_endurance = random.randint(3, 18)
    random_intelligence = random.randint(3, 18)
    random_luck = random.randint(3, 18)

    skills = ['Стремительный прыжок',
              'Электрический выстрел',
              'Ледяной удар',
              'Стремительный удар',
              ' Кислотный взгляд',
              'Тайный побег',
              'Ледяной выстрел',
              'Огненный заряд']

    skills = [skill.replace('e', 'e') for skill in skills]

    runic_skills = []
    for skill in skills:
        runic_letter = ""
        for letter in skill:
            if letter in alphabet:
                runic_letter += alphabet[letter]
            else:
                runic_letter += letter
        runic_skills.append(runic_letter)

    random_skills = random.sample(runic_skills, 3)

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'job': job,
        'town': town,
        'strength': random_strength,
        'agility': random_agility,
        'endurance': random_endurance,
        'intelligence': random_intelligence,
        'luck': random_luck,
        'skill_1': random_skills[0],
        'skill_2': random_skills[1],
        'skill_3': random_skills[2],


    }
    print(context)
    current_dir = Path(__file__).parent
    cards_dir = current_dir / 'Cards'
    # Create 'Cards' folder if it doesn't exist
    if not cards_dir.exists():
        cards_dir.mkdir(parents=True, exist_ok=True)
    # Now render the template into the created folder
    file_operations.render_template(
        'HUMANS project/template.svg', f'{cards_dir}/{first_name}_{last_name}.svg', context)


if __name__ == "__main__":
    for i in range(10):
        main()
