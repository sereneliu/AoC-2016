import re

with open('day7.txt') as puzzle_file:
    puzzle_input = puzzle_file.read().split('\n')

example_1 = 'abba[mnop]qrst' # supports TLS (abba outside square brackets)
example_2 = 'abcd[bddb]xyyx' # does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets)
example_3 = 'aaaa[qwer]tyui' # does not support TLS (aaaa is invalid; the interior characters must be different)
example_4 = 'ioxxoj[asdfgh]zxcvbn' # supports TLS (oxxo is outside square brackets, even though it's within a larger string)

def split_ip(ip):
    split_ip = re.split('\[|\]', ip)
    hypernet_seq = []
    supernet_seq = []
    for seq in split_ip:
        if '[' + seq + ']' in ip:
            hypernet_seq.append(seq)
        else:
            supernet_seq.append(seq)
    return hypernet_seq, supernet_seq

def contains_abba(seq):
    for i in range(0, len(seq) - 3):
        if seq[i:i+2] == seq[i+3:i+1:-1] and seq[i] != seq[i+1]:
            return True
    return False

def supports_tls(ip):
    hypernet, supernet = split_ip(ip)
    if any(contains_abba(h) for h in hypernet):
        return False
    if any(contains_abba(s) for s in supernet):
        return True
    return False

# print supports_tls(example_1)
# print supports_tls(example_2)
# print supports_tls(example_3)
# print supports_tls(example_4)

def contains_aba(seq):
    aba = []
    for i in range(0, len(seq) - 2):
        if seq[i] == seq[i+2] and seq[i] != seq[i+1]:
            aba.append(seq[i:i+3])
    return aba

example_5 = 'aba[bab]xyz' # supports SSL (aba outside square brackets with corresponding bab within square brackets)
example_6 = 'xyx[xyx]xyx' # does not support SSL (xyx, but no corresponding yxy)
example_7 = 'aaa[kek]eke' # supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different)
example_8 = 'zazbz[bzb]cdb' # supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap)

def supports_ssl(ip):
    hypernet, supernet = split_ip(ip)
    aba_set = {aba[0:2] for s in supernet for aba in contains_aba(s)}
    bab_set = {bab[1::-1] for h in hypernet for bab in contains_aba(h)}
    if aba_set.intersection(bab_set):
        return True
    return False

# print supports_ssl(example_5)
# print supports_ssl(example_6)
# print supports_ssl(example_7)
# print supports_ssl(example_8)

def count_ips(ip_list):
    tls_ips = 0
    ssl_ips = 0
    for ip in ip_list:
        if supports_tls(ip):
            tls_ips += 1
        if supports_ssl(ip):
            ssl_ips += 1
    return tls_ips, ssl_ips

print count_ips(puzzle_input)