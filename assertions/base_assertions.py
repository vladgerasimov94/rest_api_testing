from assertpy import assert_that, soft_assertions
from cerberus import Validator


class BaseAssertions:
    @staticmethod
    def validate_response_by_schema(schema: dict, require_all: bool, response_data: dict | list[dict]):
        def _validate(data_):
            validator = Validator(schema, require_all=require_all)
            is_valid = validator.validate(data_)
            assert_that(is_valid, description=validator.errors).is_true()

        if isinstance(response_data, dict):
            _validate(response_data)
        elif isinstance(response_data, list):
            with soft_assertions():
                for data in response_data:
                    _validate(data)
