import json
from uuid import uuid4

import requests
from assertpy.assertpy import assert_that, soft_assertions
from jsonpath_ng import parse

from assertions.people_assertions import PeopleAssertions
from clients.people.people_client import people_client
from config import BASE_URI
from helpers.people_helper import PeopleHelper


class TestPeople:
    def test_read_all_has_kent(self) -> None:
        response = people_client.read_all_persons()
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(requests.codes.ok)
            PeopleAssertions.assert_people_have_person_with_first_name(response, first_name='Kent')

    def test_new_person_can_be_added(self):
        last_name, response = people_client.create_person()
        assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.no_content)

        peoples = people_client.read_all_persons().as_dict
        is_new_user_created = PeopleHelper.search_created_user_in(peoples, last_name)
        PeopleAssertions.assert_person_is_present(is_new_user_created)

    def test_created_person_can_be_deleted(self):
        persons_last_name, _ = people_client.create_person()

        people = people_client.read_all_persons().as_dict
        new_person_id = PeopleHelper.search_created_user_in(people, persons_last_name)['person_id']

        response = people_client.delete_person(new_person_id)
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
        PeopleAssertions.assert_all_persons_contains_person_id(is_expected=False, person_id=new_person_id)

    def test_person_can_be_added_with_a_json_template(self, create_data):
        people_client.create_person(create_data)

        response = people_client.read_all_persons()
        people = response.as_dict

        result = PeopleHelper.search_nodes_using_json_path(people, json_path="$.[*].lname")

        expected_last_name = create_data['lname']
        assert_that(result).contains(expected_last_name)
