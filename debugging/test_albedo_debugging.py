from albedo import check_for_new_snow, calc_surface_albedo, ALBEDO_SNOW_FRESH
import pytest_check as check


def test_check_for_new_snow():
    check.is_true(check_for_new_snow(10, 0))
    check.is_false(check_for_new_snow(0, 10))


def test_check_for_new_snow_same():
    check.is_false(check_for_new_snow(10, 10))


def test_calc_surface_albedo_snow_new():
    albedo_snow_old = 0.8
    albedo_ice = 0.6
    check.equal(
        calc_surface_albedo(albedo_snow_old, albedo_ice, 10, 5), ALBEDO_SNOW_FRESH
    )


def test_calc_surface_albedo_snow_old():
    albedo_snow_old = 0.8
    albedo_ice = 0.6
    check.equal(calc_surface_albedo(albedo_snow_old, albedo_ice, 1, 5), albedo_snow_old)


def test_calc_surface_albedo_ice():
    albedo_snow_old = 0.8
    albedo_ice = 0.6
    check.equal(calc_surface_albedo(albedo_snow_old, albedo_ice, 0, 5), albedo_ice)
