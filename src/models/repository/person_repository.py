from src.models.settings.connection import db_connection_handler
from src.models.entities.person import Person

class PersonRepository:

    def insert_person(self, personInfo) -> bool:
        with db_connection_handler as database:
            try:
                person = ( 
                    Person(
                        name=personInfo.get("name"),
                        documento=personInfo.get("document"),
                        age=personInfo.get("age"),
                        phone=personInfo.get("phone")
                    )
                )

                database.session.add(person)
                database.session.commit()

                return True
            except Exception as ex:
                database.session.rollback()
                raise ex

    def get_person(self, person_id: int):
        with db_connection_handler as database:
            try:
                person = (
                    database
                    .session
                    .query(Person)
                    .filter(Person.id == person_id)
                    .one()
                )

                return person
            except Exception as ex:
                return None
        

    def get_all_person():
        pass

    def update_person():
        pass

    def delete_person(self, person_id):
        with db_connection_handler as database:
            try:
                person = (
                    database
                    .session
                    .query(Person)
                    .filter(Person.id == person_id)
                    .one()
                )

                database.session.delete(person)
                database.session.commit()

            except Exception as ex:
                database.session.rollback()
                raise ex