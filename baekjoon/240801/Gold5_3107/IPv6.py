'''
IPv6의 주소 : 36자리의 16진수를 4자리씩, 각 그룹은 :을 통해 구분
ex) 2001:0db8:85a3:0000:0000:8a2e:0370:7334
주소 축약 방법
1. 각 그룹의 앞지리의 0의 전체 또는 일부 생략 가능
    ex) 2001:db8:85a3:0:00:8a2e:370:7334
2. 0으로만 이뤄져있는 그룹의 경우 한 개 이상 연속된 그룹을 골라 ::로 대체 가능
   but, 이 규칙은 한 번만 사용 가능
    ex) 2001:db8:85a3::8a2e:370:7334

축약형 IPv6 주소 -> 원래 IPv6으로 복원하는 프로그램
'''

simple_ipv6 = input()

list_ipv6 = simple_ipv6.split(':')
result = ''

# ::1 or 1:: 인 경우, 앞 or 뒤의 공백이 2개 생김 -> 제거
if list_ipv6[0] == '':
    list_ipv6 = list_ipv6[1:]
elif list_ipv6[-1] == '':
    list_ipv6 = list_ipv6[:-1]

for i in range(len(list_ipv6)):
    if list_ipv6[i] == '':
        result += ('0000:' * (8 - len(list_ipv6) + 1)) # 부족한 개수만큼 0000 채우기
    else:
        result += (list_ipv6[i].zfill(4) + ':')

print(result[:-1])