from typing import List
from src.infra.config import DBConnectionHandler
from src.domain.models import Pets
from src.infra.entities import Pets as PetsEntity


class PetRepository:
    """Class to manage Pet Repository"""

    @staticmethod
    def insert_pet(name: str, specie: str, age: int, user_id: int) -> Pets:
        """Insert a pet in the database
        :param - name: name of the pet
            - especie: Enum with especie acepted
            - age: age of the pet
            - user_id: id of the owner (FK)
        :return - tuple with new pet inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsEntity(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    id=new_pet.id, name=new_pet.name, specie=new_pet.specie.value, age=new_pet.age, user_id=new_pet.user_id
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None

    @staticmethod
    def select_pet(pet_id: int = None, user_id: int = None) -> List[Pets]:
        """
        Select data in PetsRepository entity by id and/or user_id
        :param - pet_id: id of the pet registry
               - user_id: id of the user owner
        :return - List with Pets selected
        """

        try:
            query_data = None

            if pet_id and not user_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(PetsEntity).filter_by(id=pet_id).one()
                    query_data = [data]

            elif not pet_id and user_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(PetsEntity).filter_by(user_id=user_id).all()
                    query_data = data

            elif pet_id and user_id:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(PetsEntity).filter_by(id=pet_id, user_id=user_id).one()
                    query_data = [data]

            return query_data
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
