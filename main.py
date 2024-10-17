def is_criticality_balanced(kelvins, neutrons):
    if kelvins >= 800:
        return False
    if neutrons <= 500:
        return False
    if kelvins * neutrons >= 500000:
        return False
    return True

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percent_value = (generated_power / theoretical_max_power) * 100
    if percent_value >= 80:
        return "zielony"
    if percent_value >= 60:
        return "pomarańczowy"
    if percent_value >= 30:
        return "czerwony"
    return "czarny"

def fail_safe(kelvins, neutrons_per_sec, threshold):
    calc = kelvins * neutrons_per_sec
    if calc < 0.9 * threshold:
        return "LOW"
    if 0.9 * threshold <= calc <= 1.1 * threshold:
        return "NORMAL"
    return "OTHER"

if __name__ == '__main__':
    result = is_criticality_balanced(100, 200)
    print(f'{result}')
