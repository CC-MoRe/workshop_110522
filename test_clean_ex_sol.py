from clean_ex_sol import check_for_new_snow
import pytest_check as check


def test_check_for_new_snow():
    check.is_false(check_for_new_snow(0, 0))
    check.is_true(check_for_new_snow(1, 0))
