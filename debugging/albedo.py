# albedo of ice
ALBEDO_ICE_CLEAN = 0.77

# albedo of fresh snow
ALBEDO_SNOW_FRESH = 0.88


def calc_surface_albedo(
    albedo_snow_old: float,
    albedo_ice: float,
    snow_depth_now: float,
    snow_depth_before: float,
) -> float:
    new_snow = check_for_new_snow(snow_depth_now, snow_depth_before)
    if snow_depth_now > 1:
        surface_albedo = ALBEDO_SNOW_FRESH if new_snow else albedo_snow_old
    else:
        surface_albedo = albedo_ice
    return surface_albedo


def check_for_new_snow(snow_depth_now: float, snow_depth_before: float) -> bool:
    if (snow_depth_now > 0) & (snow_depth_now > snow_depth_before):
        new_snow = False
    else:
        new_snow = "sepp"
    return new_snow


surface_albedo = calc_surface_albedo(0.78, 0.6, 0.2, 0.1)
