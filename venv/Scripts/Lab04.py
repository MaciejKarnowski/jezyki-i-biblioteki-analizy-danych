import collections

patterns = ["abc", "aab", "cba","abca"]
text = "aaabcab"

AdjList = []


def create_empty_trie():
    AdjList.append({'value': '', 'next_states': [], 'fail_state': 0, 'output': []})  # Tworzenie tablicy stanów


def find_next_state(current_state, value):
    for node in AdjList[current_state]["next_states"]:
        if AdjList[node]["value"] == value:
            return node
    return None


def add_keyword(patterns):
    current_state = 0
    j = 0
    pattern = patterns.lower()  # zamiana patternu na male litery
    child = find_next_state(current_state, pattern[j])
    while child is not None:
        current_state = child
        j = j + 1
        if j < len(pattern):
            child = find_next_state(current_state, pattern[j])
        else:
            break
    for i in range(j, len(pattern)):
        node = {'value': pattern[i], 'next_states': [], 'fail_state': 0, 'output': []}
        AdjList.append(node)
        AdjList[current_state]["next_states"].append(len(AdjList) - 1)
        current_state = len(AdjList) - 1
    AdjList[current_state]["output"].append(pattern)


def add_keywords(patterns):
    for pattern in patterns:
        add_keyword(pattern)


def set_fail_transitions():
    q = collections.deque()
    child = 0
    for node in AdjList[0]["next_states"]:
        q.append(node)
        AdjList[node]["fail_state"] = 0
    while q:
        r = q.popleft()
        for child in AdjList[r]["next_states"]:
            q.append(child)
            state = AdjList[r]["fail_state"]
            while find_next_state(state, AdjList[child]["value"]) is None and state != 0:
                state = AdjList[state]["fail_state"]
            AdjList[child]["fail_state"] = find_next_state(state, AdjList[child]["value"])
            if AdjList[child]["fail_state"] is None:
                AdjList[child]["fail_state"] = 0
            AdjList[child]["output"] = AdjList[child]["output"] + AdjList[AdjList[child]["fail_state"]]["output"]


def init_trie(patterns):  # Nasza funckja build, oczywiście można wrzucić caly kod zawarty w funkcjach, ale nie ma w tym sensu.
    create_empty_trie()
    add_keywords(patterns)
    set_fail_transitions()


def get_patterns_found(text):
    text = text.lower()
    current_state = 0
    patterns_found = []

    for i in range(len(text)):
        while find_next_state(current_state, text[i]) is None and current_state != 0:
            current_state = AdjList[current_state]["fail_state"]
        current_state = find_next_state(current_state, text[i])
        if current_state is None:
            current_state = 0
        else:
            for j in AdjList[current_state]["output"]:
                patterns_found.append({"index": i - len(j) + 1, "word": j})
    return patterns_found


init_trie(patterns)
print(get_patterns_found(text))
