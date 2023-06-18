from assertpy import assert_that

from clients.people.people_client import people_client


class PeopleAssertions:
    @staticmethod
    def assert_people_have_person_with_first_name(response, first_name):
        assert_that(response.as_dict).extracting('fname').is_not_empty().contains(first_name)

    @staticmethod
    def assert_person_is_present(is_new_user_created):
        assert_that(is_new_user_created).is_not_empty()

    @staticmethod
    def assert_all_persons_contains_person_id(is_expected: bool, person_id):
        all_persons_fresh = people_client.read_all_persons().as_dict
        all_ids = [person["person_id"] for person in all_persons_fresh]
        if is_expected:
            assert_that(all_ids).contains(person_id)
        else:
            assert_that(all_ids).does_not_contain(person_id)
