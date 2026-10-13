"""Pac-Man"""
def eat_ghost(power_pellet_active, touching_ghost):
    """Check the parametres for boolen values"""
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Check the parametres for boolen values"""
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Check the parametres for boolen values"""
    """
        bool: Has the player lose the game?
    """
    return not power_pellet_active and touching_ghost 


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Check the parametres for boolen values"""
    """
        bool: Has the player won the game?
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)

