# 관거

# pyformat
'{1} {0}'.format('one', 'two')

# f-string python 3.6 new in
name = "홍길동"

print(f'안녕하세요. {name}')

import random

menu = ['김밥천국', '스타벅스', '부대찌개']

launch = random.choice(menu)
print('오늘의 점심은 {}입니다'.format(launch))
print(f'오늘의 점심은 {launch}입니다.')

numbers = list(range(1, 46))
print(numbers)

lotto = random.sample(numbers, 6)
print(f'오늘의 행운의 번호는 {sorted(lotto)} 입니다.')

