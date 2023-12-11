#write functions here, don't add input('') statements here!
def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    indices = []
    length = len(dna_string1)
    sub_len = len(dna_string2)

    for i in range(length - sub_len + 1):
        if dna_string1[i:i + sub_len] == dna_string2:
            indices.append(i + 1)

    return tuple(indices)


def check_dna_string(input_string):
    return len(input_string)-1 > 8 and len(input_string)-1 <= 16


def check_substring(input_string):
    return len(input_string) == 4