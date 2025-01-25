from robot.model.body import Body


class OneFlow:
    ROBOT_LIBRARY_SCOPE = "SUITE"
    ROBOT_LISTENER_API_VERSION = 3

    def _start_test(self, data, result) -> None:
        print("=== test start ===")
        print("db")

    def _end_test(self, data, result) -> None:
        print("=== test finish ===")
        print("db")


def add_skip_exeuction(): ...
