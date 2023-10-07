secret = "whatisup"
triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]


def recoverSecret(triplets):
    letters = set()

    before = {}
    after = {}

    start_letters = []

    for triplet in triplets:
        for i in range(0, len(triplet)):
            if triplet[i] not in before:
                before[triplet[i]] = set()
            if triplet[i] not in after:
                after[triplet[i]] = set()

            cur_before = set(triplet[:i])
            cur_after = set(triplet[i+1:])

            before[triplet[i]].update(cur_before)
            after[triplet[i]].update(cur_after)

            letters.add(triplet[i])

    for letter in letters:
        if len(before[letter]) == 0:
            start_letters.append(letter)

    # print(start_letters)

    ans = ""
    visited = set()

    def dfs(letter):
        nonlocal ans

        if letter in visited:
            return

        visited.add(letter)

        for next_after in after[letter]:
            dfs(next_after)

        ans = letter + ans

    for start_letter in start_letters:
        dfs(start_letter)

    return ans


print(recoverSecret(triplets))
