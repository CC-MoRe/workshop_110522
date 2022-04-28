# Not recommended
# The als is the albedo of snow
als = 0.85

# Recommended
albedo_snow = 0.85

###

albedo_snow = 0.85
ice_albedo = 0.56

albedo_snow = 0.85
albedo_ice = 0.56
surface_temperature_snow = -1.0
surface_temparture_ice = -0.1


### no magic numbers


def albedo_reduction_with_time(albedo, time):
    return albedo * 0.000001 * time


ALBEDO_REDUCTION_PER_SECOND = 0.000001


def albedo_reduction_with_time(albedo, time):
    return albedo * ALBEDO_REDUCTION_PER_SECOND * time


### Do only to one thing
def albedo_reduction_and_display(albedo, time):
    albedo = ALBEDO_REDUCTION_PER_SECOND * time
    return print(f"albedo at {time} is {albedo}")


# Better
def albedo_reduction_with_time(albedo, time):
    return albedo * ALBEDO_REDUCTION_PER_SECOND * time


def display_albedo_at_time(albedo, time):
    return print(f"albedo at {time} is {albedo}")


albedo_at_time = albedo_reduction_with_time(0.2, 100)
display_albedo_at_time(albedo_at_time, 100)


### No boolean flags


def display_albedo_at_time(albedo, time, show_time):
    if show_time:
        return print(f"albedo at {time} is {albedo}")
    else:
        return print(f"albedo is {albedo}")


display_albedo_at_time(0.7, 200, False)
display_albedo_at_time(0.7, 200, True)


def display_albedo(albedo):
    return print(f"albedo is {albedo}")


def display_albedo_at_time(albedo, time):
    return print(f"albedo at {time} is {albedo}")


display_albedo(0.7)
display_albedo_at_time(0.7, 200)


### Typehints


def albedo_reduction_with_time(albedo: float, time: float) -> float:
    """Calculates albedo over time,

    Args:
        albedo (float): Albedo of snow or ice, between 0 and 1
        time (float): Time in seconds

    Returns:
        float: Albedo
    """
    return albedo * ALBEDO_REDUCTION_PER_SECOND * time


albedo_reduction_with_time()
