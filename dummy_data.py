import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from faker import Faker
import random
from course.models import Course


Category = ['Programming','Design','Marketing',] 

def seed_course(n):
    fake = Faker()
    for _ in range(n):
        Course.objects.create(
            name = fake.name(),
            subtitle = fake.text(max_nb_chars=100),
            description = fake.text(max_nb_chars=400),
            price = round(random.uniform(20.99,200.99), 2),
            category = Category[random.randint(0,2)],
            reviews = fake.paragraphs()
        )
    
    print(f'seed {n} Courses succssfuly')


seed_course(10)