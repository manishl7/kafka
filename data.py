from faker import Faker
fake=Faker()
def get_registered_user():
    return {
        'name':fake.name(),
        'address':fake.address(),
        'created_at':fake.year()
    }

if __name__=='__main__': #this is will run wherever we run the file
    print(get_registered_user())