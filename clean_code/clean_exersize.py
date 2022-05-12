# albedo of ice
ali = 0.77

# albedo of fresh snow
alsf = 0.88


def calc_surface_albedo(albedo_snow_old, albedo_ice, snow_depth_now, snow_depth_before):
    # check for new snow
    if (snow_depth_now > 0) & (snow_depth_now > snow_depth_before):
        new_snow = True
    else:
        new_snow = False
    # asign surface albedo
    if (snow_depth_now > 0) & new_snow:
        # new snow
        return alsf
    elif (snow_depth_now > 0) & (not new_snow):
        return albedo_snow_old
    elif snow_depth_now == 0:
        return albedo_ice


surface_albedo = calc_surface_albedo(0.78, 0.6, 0.2, 0.1)
print(surface_albedo)
