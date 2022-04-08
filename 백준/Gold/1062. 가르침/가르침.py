from sys import stdin
from itertools import combinations


# bin_dict : a/c/i/t/n을 제외한 알파벳 각각에 임의의 고유 번호를 부여한 딕셔너리
bin_dict = {'b': 20, 'd': 19, 'e': 18, 'f': 17, 'g': 16, 'h': 15, 'j': 14,
            'k': 13, 'l': 12, 'm': 11, 'o': 10, 'p': 9, 'q': 8, 'r': 7,
            's': 6, 'u': 5, 'v': 4, 'w': 3, 'x': 2, 'y': 1, 'z': 0}


# 알파벳 배열을 2진수로 바꾸어주는 함수
def word_to_bin(word):
    answer = 0b0
    for x in word:
        answer = answer | (1 << bin_dict[x])

    return answer


n, k = map(int, stdin.readline().split())
words = []
# 각 입력 단어에 대하여
# 1. 앞의 anta와 뒤의 tica를 슬라이스한 뒤 set로 만들고
# 2. 그중 a/c/i/t/n을 제외한 뒤 words 리스트에 저장
for _ in range(n):
    words.append(set(stdin.readline().rstrip()[4:-4]).difference('a', 'c', 'i', 't', 'n'))

# k가 5 미만이라면 어떤 단어도 만들 수 없음.
if k < 5:
    print(0)
else:
    bin_list = [word_to_bin(x) for x in words]
    max_count = 0

    # 2의 0제곱부터 2의 20제곱까지 저장한 리스트
    power_of_2 = [2 ** i for i in range(21)]

    # 현재 순회 중인 k - 5개의 알파벳 조합(comb)으로
    for comb in combinations(power_of_2, k - 5):
        current = sum(comb)
        count = 0
        for bin_number in bin_list:
            # 현재 순회 중인 단어를 만들 수 있다면
            if bin_number & current == bin_number:
                # count에 1을 더한다.
                count += 1

        # count = comb로 만들 수 있는 단어의 개수
        max_count = max(max_count, count)

    print(max_count)