import re


def solution(new_id):
    answer = ''
    while answer != new_id:
        answer = new_id
        # 1
        new_id = new_id.lower()

        # 2
        for char in new_id:
            if char.isalnum():
                continue
            elif char in ['-', '_', '.']:
                continue
            else:
                new_id = new_id.replace(char, '')

        # 3
        p = re.compile('[.]+')
        new_id = p.sub('.', new_id)

        # 4
        if new_id.startswith('.'):
            new_id = new_id[1:]
        elif new_id.endswith('.'):
            new_id = new_id[:-1]

        # 5
        if len(new_id) == 0:
            new_id = 'a'

        # 6
        if len(new_id) >= 16:
            new_id = new_id[:15]

        # 7
        if len(new_id) <= 2:
            while len(new_id) < 3:
                new_id += new_id[-1]

        if new_id == answer:
            break

    return answer


