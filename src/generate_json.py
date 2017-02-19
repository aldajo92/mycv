import json

school = [{'name': 'Colegio Domingo Faustino Sarmiento', 'city': 'Tierralta-Cordoba', 'year': 2004},
          {'name': 'I.E Marco Fidel Suarez', 'city': 'Bello - Antioquia', 'year': 2009}
          ]

university = {
    'name': 'Universidad Nacional de Colombia',
    'city': 'Medellin',
    'profession': 'Control Engineering',
    'finished': False,
    'year': 2010
}

idioms = {
    'Spanish': {'talk': True, 'write': True},
    'English': {'talk': True, 'write': True},
}

skills = {
    'programming languages': ['Android (Java)', 'Java', 'C/C++', 'Javascript', 'Python', 'Matlab'],
    'frameworks': ['node_js'],
    'GNU/LINUX': True,
    'Agile Methodologies': ['scrum', 'kanban'],
    'soft skills': 'please contact me... I want know you'
}

work_experience = [
    {'workplace': 'Huge Inc',
     'city': 'Medellin',
     'position': 'Android Developer',
     'boss': 'Peter Van Dirk',
     'date': '01/04/2016 - 17/02/2017',
     'contact': {'phone': '(57-4)604 55 35', 'e-mail': 'mde@hugeinc.com'}
     },
    {'workplace': 'Ubidots',
     'city': 'Medellin',
     'position': 'Hardware Developer',
     'boss': 'Agustin Pelaez',
     'date': '26/01/2015 - 20/03/2015',
     'contact': {'phone': '312 834 4182', 'e-mail': 'info@ubidots.com'}
     },
    {'workplace': 'Universidad Nacional de Colombia',
     'city': 'Medellin',
     'position': 'Teacher Assistant',
     'boss': 'Alcides Montoya',
     'date': '12/02/2013 - 17/08/2013',
     'contact': {'phone': '(57-4)430 93 27', 'e-mail': ''}
     }
]

other_works = [
    {'type': 'hackathon',
     'by': 'Huge Inc',
     'Name': 'Huge Change',
     'Date': '17/01/2017',
     'place': 'Ruta-N',
     'city': 'Medellin'},
    {'type': 'hackathon',
     'by': 'Huge Inc',
     'Name': '(Winner) AI Challenge',
     'Date': '20/10/2016',
     'place': 'Ruta-N',
     'city': 'Medellin'},
    {'type': 'presentation',
     'by': 'MedellinJS',
     'Name': 'Control PID con NodeJS',
     'Date': '08/12/2015',
     'place': 'Ruta-N',
     'city': 'Medellin'},
    {'type': 'presentation',
     'by': 'Python Medellin',
     'Name': 'Robotica con Python',
     'Date': '16/12/2015',
     'place': 'Atomhouse',
     'city': 'Medellin'},
    {'type': 'Online presentation',
     'by': 'platzi.com',
     'Name': 'Programacion de robots con Nodejs',
     'Date': '20/02/2015',
     'place': 'video conference',
     'city': 'Medellin'},
    {'type': 'community',
     'by': 'Alejandro Gomez (myself)',
     'Name': 'Robotica Medellin',
     'Date': '17/02/2015',
     'place': 'Medellin',
     'city': 'Medellin'},
    {'type': 'presentation',
     'by': 'Python Medellin',
     'Name': 'Robotica y Nodejs',
     'Date': '18/02/2015',
     'place': 'Ruta-N',
     'city': 'Medellin'},
    {'type': 'competition',
     'by': 'UN-Robots',
     'Name': 'Competidor Sumo 3kg',
     'Date': '11/04/2014',
     'place': 'Universidad Nacional de Colombia',
     'city': 'Bogota'}
]

personal_references = [
    {'name': 'Alejandro Daelli',
     'workplace': 'Huge Inc',
     'position': 'Project Manager',
     'contact': {'phone': '316 419 6018', 'e-mail': 'adaelli@hugeinc.com'},
     'profession': 'Manager'},
    {'name': 'Marc Ammann',
     'workplace': 'Huge Inc',
     'position': 'Technical Director',
     'contact': {'phone': '(+1)917 705 2379', 'e-mail': 'mmammann@gmail.com'},
     'profession': 'Engineer '},
    {'name': 'Edgar Aguirre',
     'workplace': 'Huge Inc',
     'position': 'Lead',
     'contact': {'phone': '301 662 2731', 'e-mail': 'eaguirre@hugeinc.com'},
     'profession': 'Software Engineer'},
    {'name': 'Federico Ortega',
     'workplace': 'Huge Inc',
     'position': 'Office Manager',
     'contact': {'phone': '310 290 3881', 'e-mail': 'fortega@hugeinc.com'},
     'profession': 'Software Engineer'},
    {'name': 'Jose Daniel Pena',
     'workplace': 'htm.com.co',
     'position': 'Founder',
     'contact': {'phone': '300 779 0360', 'e-mail': 'josedaniel@htm.com.co'},
     'profession': 'Software Engineer'},
    {'name': 'Adrian Estrada',
     'workplace': 'NodeSource',
     'position': 'Support Developer',
     'contact': {'phone': '300 780 40 32', 'e-mail': 'edsadr@gmail.com'},
     'profession': 'Software Engineer'}
]

school_json = json.dumps(school, sort_keys=True, indent=4, separators=(',', ': '))
university_json = json.dumps(university, sort_keys=False, indent=4, separators=(',', ': '))
idioms_json = json.dumps(idioms, sort_keys=True, indent=4, separators=(',', ': '))
work_experience_json = json.dumps(work_experience, sort_keys=False, indent=4, separators=(',', ': '))
other_works_json = json.dumps(other_works, sort_keys=False, indent=4, separators=(',', ': '))
skills_json = json.dumps(skills, sort_keys=False, indent=4, separators=(',', ': '))
personal_references_json = json.dumps(personal_references, sort_keys=False, indent=4, separators=(',', ': '))

print school_json
print university_json
print idioms
print work_experience_json
print other_works_json
print skills_json
print personal_references_json
