with open('day10.txt') as puzzle_file:
    puzzle_input = [line.split(' ') for line in puzzle_file.read().split('\n')]

def setup_dicts(instructions):
    exchange = {}
    chips = {}
    outputs = {}
    for instruction in instructions:
        if instruction[0] == 'bot':
            exchange[' '.join(instruction[0:2])] = [' '.join(instruction[5:7]), ' '.join(instruction[10:])]
        for i in range(len(instruction)):
            if instruction[i] == 'bot':
                chips[' '.join(instruction[i:i+2])] = []
            if instruction[i] == 'output':
                outputs[' '.join(instruction[i:i+2])] = []
    return exchange, chips, outputs

bot_exchange, bot_chips, bot_outputs = setup_dicts(puzzle_input)

def exchange_chips(bot, end):
    if len(bot_chips[bot]) == 2:
        if sorted(bot_chips[bot]) == end:
            print bot
        receiving_bots = bot_exchange[bot]
        if not receiving_bots[0].startswith('output'):
            bot_chips[receiving_bots[0]].append(min(bot_chips[bot]))
        else:
            bot_outputs[receiving_bots[0]].append(min(bot_chips[bot]))
        if not receiving_bots[1].startswith('output'):
            bot_chips[receiving_bots[1]].append(max(bot_chips[bot]))
        else:
            bot_outputs[receiving_bots[1]].append(max(bot_chips[bot]))
        bot_chips[bot] = []
        for receiving_bot in receiving_bots:
            if not receiving_bot.startswith('output'):
                exchange_chips(receiving_bot, end)
    if bot_outputs['output 0'] != [] and bot_outputs['output 1'] != [] and bot_outputs['output 2'] != []:
        return bot_outputs['output 0'][0] * bot_outputs['output 1'][0] * bot_outputs['output 2'][0]

def read_instructions(instructions, end):
    for instruction in instructions:
        if instruction[0] == "value":
            bot = ' '.join(instruction[4:])
            bot_chips[bot].append(int(instruction[1]))
            if exchange_chips(bot, end):
                return exchange_chips(bot, end)

print read_instructions(puzzle_input, [17, 61])