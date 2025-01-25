from robot.running import Keyword


class OneFlowSuite:
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        self.failed_test_case: str = ""

    def _start_test(self, data, result) -> None:
        if result.parent.has_setup and not result.parent.setup.passed:
            data.setup = self._SkipExecutionKeywordOnly()
        if self.failed_test_case:
            data.setup = self._SkipExecutionKeywordOnly()

    def _end_test(self, data, result) -> None:
        if result.parent.has_setup and not result.parent.setup.passed:
            result.skipped = True
        elif result.status == "FAIL":
            self.failed_test_case = data.name

    def _SkipExecutionKeywordOnly(self):
        return Keyword(
            name="Skip",
            args=[
                f"Test skipped becuase previous test case failed: {self.failed_test_case}"
            ],
        )
