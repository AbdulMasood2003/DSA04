def calculate_age_frequency(ages):
    age_frequency = {}
    for age in ages:
        if age in age_frequency:
            age_frequency[age] += 1
        else:
            age_frequency[age] = 1

    return age_frequency

def main():
    customer_ages = [20, 25, 30, 35, 40, 25, 20, 35, 30, 40]
    age_distribution = calculate_age_frequency(customer_ages)
    print("Age\tFrequency")
    for age, frequency in age_distribution.items():
        print(f"{age}\t{frequency}")
if __name__ == "__main__":
    main()
