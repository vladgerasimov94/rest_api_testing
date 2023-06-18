from jsonpath_ng import parse


class PeopleHelper:
    @staticmethod
    def search_created_user_in(people, last_name):
        return [person for person in people if person['lname'] == last_name][0]

    @staticmethod
    def search_nodes_using_json_path(people, json_path):
        jsonpath_expr = parse(json_path)
        return [match.value for match in jsonpath_expr.find(people)]
