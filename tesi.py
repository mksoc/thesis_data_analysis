import matplotlib.pyplot as plt

def response_rate(answers):
    # Calculate the ratio of yes
    number_of_customers = len([i for i in total_answers if i['customer'] == 'Si'])

    customer_percentage = 100 * (number_of_customers / len(answers))
    print(f'Number of customers: {number_of_customers}/{len(answers)} ({customer_percentage:.1f} %)')

    # Plot yes/no pie chart
    labels = ['Yes', 'No']
    sizes = [number_of_customers, len(answers) - number_of_customers]

    _, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()

def frequency(answers):
    labels = ['1-2', '3-4', '5-6', '7-8', '9+']
    frequency = [
        len([i for i in answers if i['frequency'] == "da 1 a 2 volte l'anno"]),
        len([i for i in answers if i['frequency'] == "da 3 a 4 volte l'anno"]),
        len([i for i in answers if i['frequency'] == "da 5 a 6 volte l'anno"]),
        len([i for i in answers if i['frequency'] == "da 7 a 8 volte l'anno"]),
        len([i for i in answers if i['frequency'] == "più di 9 volte l'anno"]),
    ]

    _, ax = plt.subplots()
    bars = ax.bar(labels, frequency, 0.35)
    ax.bar_label(bars)
    plt.show()

keys = ['customer',
        'frequency',
        'purchase_location',
        'brand_known_for',
        'last_purchase',
        'all_purchases',
        'satisfaction',
        'gender',
        'age',
        'education',
        'profession',
        'place_of_residence',
        'province',
        'self_or_others']
total_answers = []

# Read file and append each answer to list of dict
with open('risposte.tsv', 'r') as answer_file:
    lines = answer_file.readlines()

    for line in lines[1:]:
        values = line.split('\t')
        total_answers.append(dict(zip(keys, values[1:])))

yes_answers = [i for i in total_answers if i['customer'] == 'Si']

# response_rate(answers)
frequency(yes_answers)