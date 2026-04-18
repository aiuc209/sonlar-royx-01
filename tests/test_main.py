import pytest

def replace_with_sorted_digits(nums):
    return [int(''.join(sorted(str(num), reverse=True))) for num in nums]

@pytest.mark.parametrize("nums, expected", [
    ([123, 456, 789], [321, 654, 987]),
    ([111, 222, 333], [111, 222, 333]),
    ([987, 654, 321], [987, 654, 321]),
    ([0, 1, 2], [0, 1, 2]),
    ([9, 8, 7], [9, 8, 7]),
])

def test_replace_with_sorted_digits(nums, expected):
    assert replace_with_sorted_digits(nums) == expected
