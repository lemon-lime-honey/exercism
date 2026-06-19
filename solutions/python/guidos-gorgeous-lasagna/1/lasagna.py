EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """
    Return remaining time.

    This function takes a number representing the time already spent baking and calculates the remaining time for the lasagna.
    """
    return(EXPECTED_BAKE_TIME - elapsed_bake_time)

def preparation_time_in_minutes(number_of_layers):
    """
    Return preparation time.

    This function takes a number representing the number of layers and calculates the preparation time for cooking the lasagna.
    """
    return number_of_layers*2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return (number_of_layers*2 + elapsed_bake_time)