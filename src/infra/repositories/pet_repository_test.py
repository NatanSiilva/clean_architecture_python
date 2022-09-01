from faker import Faker
from src.infra.config import DBConnectionHandler
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
