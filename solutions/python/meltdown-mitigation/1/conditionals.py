"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Checking veriables for criticality balanced settings"""
    return (temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000) 

print(is_criticality_balanced(750,600))
    

def reactor_efficiency(voltage, current, theoretical_max_power):
    """To measure of reactor efficiency"""
    generated_power = voltage * current
    gen1_power = (generated_power / theoretical_max_power) * 100 

    if gen1_power   >= 80:
        return "green"
    elif gen1_power >= 60:
        return "orange"
    elif gen1_power >= 30:
        return "red"
    else:
        return "black"

#print(reactor_efficiency(200,50,15000))


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    current_value = int(temperature * neutrons_produced_per_second)

    if current_value < 0.9 * threshold:
        return "LOW"
    elif 0.9 * threshold < current_value < 1.1 * threshold:
        return "NORMAL"
    else:
        return "DANGER"
    
#print(fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000))