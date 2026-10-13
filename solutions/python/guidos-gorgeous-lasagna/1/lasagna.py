"""Guido's Gorgeous Lasagna"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(time):
    """Bake Time"""    
    elapsed_bake_time = int(time)
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Preparation Time"""    
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Elapsed Time"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
