import pandas as pd
from faker import Faker

def generate_profiles(number=20):
    # Create object
    fake = Faker()

    # Generate data
    # fake_name = fake.name()
    # fake_text = fake.text()
    # fake_address = fake.address()
    # fake_email = fake.email()
    # fake_date = fake.date()
    # fake_country = fake.country()
    # fake_phone_number = fake.phone_number()
    # fake_random_number = fake.random_number(digits=number)
    number=number
    # Dataframe creation
    fakeDataframe = pd.DataFrame({'date': [fake.date() for i in range(number)],
                                'name': [fake.name() for i in range(number)],
                                'email': [fake.email() for i in range(number)],
                                'number': [ fake.phone_number() for i in range(number) ],
                                'text': [fake.text() for i in range(number)]})
    return fakeDataframe

if __name__ == '__main__':
    fakeDataframe = generate_profiles()
    print(fakeDataframe)
