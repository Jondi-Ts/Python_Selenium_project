


class Verifications:
    @staticmethod
    def verify_equals(actual, expected):
        assert actual == expected, f"Expected '{expected}', but got '{actual}'"

    def verify_true(expression):
        assert expression, f"Expected 'True', but got 'False'"

    def verify_false(expression):
        assert not expression, f"Expected 'False', but got 'True'"

    def verify_in(item, container):
        assert item in container, f"'{item}' not found in {container}"

    def verify_not_in(item, container):
        assert item not in container, f"'{item}' found in {container} but it shouldn't be"

