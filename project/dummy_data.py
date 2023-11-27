
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup

from faker import Faker
from book.models import Author,Book,Review


def create_Book(n):
    fake=Faker()
    for x in range(n):
        Book.objects.create(
           title=fake.name()
            author=faker.name()
            publication_data =faker.name()
            price=faker.name()
            
        )


def create_Author(n):
    fake=Faker()
    for x in range(n):
        Author.objects.create(
           name=fake.name()
            birth_date=faker.name()
             biography=faker.name()
        )


def create_Review(n):
    fake=Faker()
    for x in range(n):
        Book.objects.create(
           reviewer_name=fake.name()
            content=faker.name()
            book=faker.name()
        )

      





