with open('day6.txt') as puzzle_file:
    puzzle_input = puzzle_file.read().split('\n')

def most_freq_letter(error_message):
    correct_message = []
    pos = 0
    while pos < len(error_message[0]):
        alpha_dict = {}
        for message in error_message:
            if message[pos] not in alpha_dict.keys():
                alpha_dict[message[pos]] = 1
            else:
                alpha_dict[message[pos]] += 1
        for k, v in alpha_dict.items():
            if v == max(alpha_dict.values()):
                correct_message.append(k)
        pos += 1
    return ''.join(correct_message)

print most_freq_letter(puzzle_input)