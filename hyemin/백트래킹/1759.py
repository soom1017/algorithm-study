'''

1. 자음 리스트, 모음 리스트로 분리
2. 자음 리스트에서 2개 뽑고, 모음 리스트에서 1개 뽑음
3. consonants[자음idx + 2:]와 vowels[모음idx + 1] 리스트에서 L - 3개의 글자를 뽑음
4. 결과 리스트에 append

-> 이렇게 하는 경우 자음에 뒷순서 글자가 싹다 몰린 경우 순서대로 출력 불가 (전체 결과 리스트를 정렬해서 보여줘야 함)

'''

vowel = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
letters = input().split()
letters.sort()

result = []

def is_pw(pw):
    vow_cnt, con_cnt = 0, 0

    for letter in pw:
        if letter in vowel:
            vow_cnt += 1
        else:
            con_cnt += 1

    return vow_cnt >= 1 and con_cnt >= 2

def back_tracking(pw_letter_cnt, letter_idx):
    # 만들어진 암호가 유효한지 검사
    if pw_letter_cnt == L:
        if is_pw(result):
            print("".join(result))
        return
    
    # 아직 L길이가 안됐을 때, 계속해서 정렬된 letters의 글자를 추가하면서 암호를 백트래킹으로 만듦
    for i in range(letter_idx, C):
        result.append(letters[i]) # 만드는 암호에 새로운 letter 추가
        back_tracking(pw_letter_cnt + 1, i + 1) # 백트래킹 수행
        result.pop() # L 길이의 문자열이 다 만들어진 경우, 맨 마지막에 넣었던 letter를 뺌(사전순으로 만들어짐)

back_tracking(0, 0)