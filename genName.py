from faker import Faker

def generate_random_name():
    fake = Faker('ru_RU')  # Указываем локаль для русских фамилий и имен
    return f"{fake.last_name()} {fake.first_name()}"


def generate_random_email():
    fake = Faker()
    ans = fake.email()
    return f"{ans}"[0: len(ans) - 11] + "gmail.com"

