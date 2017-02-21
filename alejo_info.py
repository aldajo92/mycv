import json

my_name_text = 'Hello!! My name is Alejandro Daniel Jose Gomez Florez\n'

my_summary = 'I like creating something out of nothing. My motivation is to learn continuously with the purpose to help people in different ways. When I work with teams with a variety of people with different perceptions and motivations, I can learn importance to receive feedback and interact with them when the goal is to give new solutions with lines of codes. I want to be a part of the social change with the technology, because smiles, happy moments, hopes and illusions can come from unexpected moments, and from unexpected sources.\n'

general_info = {'id': '1020448476',
                'date-of-birth': '20/06/1992',
                'place-of-birth': 'Medellin, Antioquia',
                'civil-status': 'Single',
                'phone': '300 633 8327',
                'e-mail': 'alejodiscovery20@gmail.com',
                'github': 'aldajo92',
                'linkedin': 'aldajo92'}

school = [{'name': 'Colegio Domingo Faustino Sarmiento', 'city': 'Tierralta-Cordoba', 'year': 2004},
          {'name': 'I.E Marco Fidel Suarez', 'city': 'Bello', 'year': 2009}
          ]

university = {
    'name': 'Universidad Nacional de Colombia',
    'city': 'Medellin',
    'profession': 'Control Engineering',
    'year': 2010
}

idioms = {
    'Spanish': {'talk': True, 'write': True},
    'English': {'talk': True, 'write': True},
}

skills = {
    'programming languages': ['Java', 'C/C++', 'Javascript', 'Python 2.7', 'Matlab'],
    'GNU/LINUX': True,
    'Agile Methodologies': ['scrum', 'kanban'],
    'Social skills': 'please contact me... I want to know you',
    'Git': ['github', 'bitbucket', 'gitlab', 'stash'],
    'embedded systems': ['Arduino', 'BeagleBone', 'Raspberry Pi', 'Nvidia Jetson']
}

programming_language_details = {
    'Java-Android': {
        'ides': ['Android-Studio', 'eclipse'],
        'libraries': ['RxAndroid', 'ButterKnife', 'Dagger', 'Retrofit', 'OpenCV', 'Picasso', 'Calligraphy']
    },
    'Java': {
        'ides': ['IntelliJ', 'NetBeans', 'Eclipse'],
        'frameworks': ['Spring'],
        'libraries': ['Dagger', 'Retrofit', 'OpenCV', 'SerialPort']
    },
    'Javascript':
        {'environments': 'nodeJS',
         'ides': ['Sublime', 'Visual Studio'],
         'frameworks': ['Express'],
         'libraries': ['OpenCV', 'Johnny-five', 'Serial', 'OpenCV', 'Request']
         },
    'Python':
        {'ides': 'Pycharm',
         'libraries': ['OpenCV', 'Numpy', 'Matplot', 'pyserial', 'json', 'requests', 'socket']
         },
    'Matlab':
        {'ides': ['matlab', 'octave', 'scilab']}
}

work_experience = [
    {'workplace': 'Huge Inc',
     'city': 'Medellin',
     'position': 'Android Developer',
     'boss': 'Peter Van Dirk',
     'date': '01/04/2016 - 17/02/2017',
     'contact': {'phone': '(57-4)604 55 35', 'e-mail': 'mde@hugeinc.com'},
     "description": "Developing apps with Android (Java) and supporting hardware projects. Part of the Huge Academy initiative to teach technology for underprivileged child."
     },
    {'workplace': 'HTM',
     'city': 'Medellin',
     'position': 'Developer',
     'boss': 'Jose Daniel Pena',
     'date': '05/01/2016 - 15/03/2016',
     'contact': {'phone': '300 779 0360', 'e-mail': 'josedaniel@htm.com.co'},
     'description': 'Developing a program running with NodeJS on a Raspberry Pi to send sensor information with a custom protocol to a remote server.'
     },
    {'workplace': 'Gora',
     'city': 'Medellin',
     'position': 'Teacher',
     'boss': 'Thomas King',
     'date': '06/04/2015 - 12/12/2015',
     'contact': {'phone': '(57-4)311 57 65', 'e-mail': 'thomas@gora.space'},
     'description': 'Teaching how electronics works with a Raspberry pi and Arduino to create scripts in python'
     },
    {'workplace': 'Ubidots',
     'city': 'Medellin',
     'position': 'Hardware Developer',
     'boss': 'Agustin Pelaez',
     'date': '26/01/2015 - 20/03/2015',
     'contact': {'phone': '312 834 4182', 'e-mail': 'info@ubidots.com'},
     'description': 'Developing Hardware to collect data from sensors and send them to the Ubidots platform.'
     },
    {'workplace': 'Universidad Nacional de Colombia',
     'city': 'Medellin',
     'position': 'Teacher Assistant',
     'boss': 'Alcides Montoya',
     'date': '12/02/2013 - 17/08/2013',
     'contact': {'phone': '(57-4)430 93 27', 'e-mail': '-'},
     'description': 'Helping to students to understand physics with programs made in Java and teaching to make simulations with the Swing library.'
     }
]

other_works = [
    {'type': 'hackathon',
     'by': 'Huge Inc',
     'Name': 'Huge Change',
     'Date': '17/01/2017',
     'place': 'Ruta-N',
     'city': 'Medellin',
     'description': 'Part of the Skywalkers team where we created a platform using node.js (server side), python (client side with a Raspberry pi ) and a ios app (client side) to help blind people to navigate in the street with an external hardware.'},
    {'type': 'hackathon',
     'by': 'Huge Inc',
     'Name': '(Winner) AI Challenge',
     'Date': '20/10/2016',
     'place': 'Ruta-N',
     'city': 'Medellin',
     'description': 'Part of the Mercury team where we created a platform using node.js (server side on a Raspberry pi) and a ios app (client side) to help people to save water using a gamification methodology in a smart shower.'},
    {'type': 'presentation',
     'by': 'MedellinJS',
     'Name': 'Control PID con NodeJS',
     'Date': '08/12/2015',
     'place': 'Ruta-N',
     'city': 'Medellin',
     'description': 'Combination with a math model feedback on a differential robot to show math applied on this one using a Beaglebone and NodeJS.'},
    {'type': 'presentation',
     'by': 'Python Medellin',
     'Name': 'Robotica con Python',
     'Date': '16/12/2015',
     'place': 'Atomhouse',
     'city': 'Medellin',
     'description': 'Presentation about tools and libraries to develop robots with the power of python.'},
    {'type': 'Online presentation',
     'by': 'platzi.com',
     'Name': 'Programacion de robots con Nodejs',
     'Date': '20/02/2015',
     'place': 'video conference',
     'city': 'Medellin',
     'description': 'Presentation about tools and libraries to develop robots with the power of NodeJS.'},
    {'type': 'community/founder',
     'by': 'me',
     'Name': 'Robotica Medellin',
     'Date': '17/02/2015',
     'place': 'Medellin',
     'city': 'Medellin',
     'description': 'Talks and workshop every months in Ruta-N and other places in medellin to share the robotics knowledge.'},
    {'type': 'presentation',
     'by': 'MedellinJS',
     'Name': 'Robotica y Nodejs',
     'Date': '18/02/2015',
     'place': 'Ruta-N',
     'city': 'Medellin',
     'description': 'Presentation about tools and libraries to develop robots with the power of NodeJS.'},
    {'type': 'competition',
     'by': 'UN-Robots',
     'Name': 'Competidor Sumo 3kg',
     'Date': '11/04/2014',
     'place': 'Universidad Nacional de Colombia',
     'city': 'Bogota',
     'description': 'We made an autonomous robot to battle in a sumo category.'}
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
     'profession': 'Electronic Engineer'},
    {'name': 'Adrian Estrada',
     'workplace': 'NodeSource',
     'position': 'Support Developer',
     'contact': {'phone': '300 780 40 32', 'e-mail': 'edsadr@gmail.com'},
     'profession': 'Software Engineer'}
]

general_info_json = json.dumps(general_info, sort_keys=True, indent=4, separators=(',', ': '))
skills_json = json.dumps(skills, sort_keys=False, indent=4, separators=(',', ': '))
school_json = json.dumps(school, sort_keys=True, indent=4, separators=(',', ': '))
university_json = json.dumps(university, sort_keys=False, indent=4, separators=(',', ': '))
idioms_json = json.dumps(idioms, sort_keys=True, indent=4, separators=(',', ': '))
work_experience_json = json.dumps(work_experience, sort_keys=False, indent=4, separators=(',', ': '))
other_works_json = json.dumps(other_works, sort_keys=False, indent=4, separators=(',', ': '))
personal_references_json = json.dumps(personal_references, sort_keys=False, indent=4, separators=(',', ': '))
programming_language_details_json = json.dumps(programming_language_details, sort_keys=False, indent=4,
                                               separators=(',', ': '))


def my_name():
    return my_name_text


def general_info():
    return general_info_json


def skills():
    return skills_json


def programming_language():
    return programming_language_details_json


def idioms():
    return idioms_json


def school_info():
    return school_json


def university_info():
    return university_json


def experience():
    return work_experience_json


def other_works():
    return other_works_json


def personal_references():
    return personal_references_json


def summary():
    return my_summary
