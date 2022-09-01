from faker import Faker
from src.infra.config import DBConnectionHandler

from src.infra.entities import Pets as PetsEntity
from src.infra.entities.pets import AnimalTypes
from .pet_repository import PetRepository

faker = Faker()
pet_repository = PetRepository()
db_connection_handle = DBConnectionHandler()


def test_insert_pet():
    """Test to insert a pet in the database"""

    name = faker.name()
    specie = "CAT"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    new_pet = pet_repository.insert_pet(name=name, specie=specie, age=age, user_id=user_id)

    engine = db_connection_handle.get_engine()
    query = engine.execute(f"SELECT * FROM pets WHERE id = {new_pet.id}").fetchone()

    assert query is not None
    assert new_pet.id == query.id
    assert new_pet.name == query.name
    assert new_pet.specie == query.specie
    assert new_pet.age == query.age
    assert new_pet.user_id == query.user_id

    engine.execute(f"DELETE FROM pets WHERE id = {new_pet.id}")


def test_select_pet():
    """Should select a pet in Pets table and compare it"""

    pet_id = faker.random_number(digits=4)
    user_id = faker.random_number()
    specie = "CAT"
    name = faker.name()
    age = faker.random_number(digits=1)

    specie_mock = AnimalTypes("CAT")
    data = PetsEntity(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)

    engine = db_connection_handle.get_engine()
    engine.execute(f"INSERT INTO pets (id, name, specie, age, user_id) VALUES ({pet_id}, '{name}', '{specie}', {age}, {user_id})")

    query_pets_one = pet_repository.select_pet(pet_id=pet_id)
    query_pets_two = pet_repository.select_pet(user_id=user_id)
    query_pets_three = pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

    assert query_pets_one is not None
    assert query_pets_two is not None
    assert query_pets_three is not None

    assert data in query_pets_one
    assert data in query_pets_two
    assert data in query_pets_three

    engine.execute(f"DELETE FROM pets WHERE id = {pet_id}")
