# pytest_assertrepr_compare hook -> return list of strings
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, int) and isinstance(right, int) and op == "==":
        return [
            "Comparing integers:",
            f'  vals: {left} != {right}'
        ]