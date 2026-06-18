"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    return (temperature < 800)*(neutrons_emitted > 500)*(temperature*neutrons_emitted < 500000)

def reactor_efficiency(voltage, current, theoretical_max_power):
    efficiency = ((voltage * current) / theoretical_max_power) * 100
    if efficiency >= 80:
        result = 'green'
    elif efficiency >= 60:
        result = 'orange'
    elif efficiency >= 30:
        result = 'red'
    else:
        result = 'black'
    return result

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    number = temperature * neutrons_produced_per_second
    if number < (threshold * 0.9):
        result = 'LOW'
    elif number < (threshold * 1.1):
        result = 'NORMAL'
    else:
        result = 'DANGER'
    return result
