from assertions.people_assertions import PeopleAssertions
from clients.people.people_client import people_client
from tests.data.people_response_schemas import schema_1


class TestSchema:
    def test_read_one_operation_has_expected_schema(self):
        person = people_client.read_one_person_by_id(person_id=1)
        PeopleAssertions.validate_response_by_schema(schema=schema_1, require_all=True, response_data=person)

    def test_read_all_operation_has_expected_schema(self):
        persons = people_client.read_all_persons()
        PeopleAssertions.validate_response_by_schema(schema=schema_1, require_all=True, response_data=persons)
