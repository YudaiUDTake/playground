import re

result = re.search(pattern=r'猫', string='吾輩は猫である。名前はまだない。')
print(result)

"""
r -> 『生の文字列』として扱う表記
エスケープシークエンス(\)などがただの文字列になる。
"""

print('吾輩は\n猫である。\n名前はまだ無い。')
print(r'吾輩は\n猫である。\n名前はまだ無い。')


print(re.search(pattern='\\\\py.exe', string='C:\\Windows\\py.exe'))
print(re.search(pattern=r'\\py.exe', string='C:\\Windows\\py.exe'))


# OR条件
print(
    re.search(
    pattern=r'吾輩は[猫犬]である。',
    string='吾輩は猫である。名前はまだない。'
))

print(
    re.search(
    pattern=r'吾輩は(猫である|犬だよ)。',
    string='吾輩は猫である。名前はまだ無い。'
    ))

print(
    re.search(
    pattern=r'[3-5]匹の猫',
    string='帰り道に3匹の猫を見かけた。')
)

# 数値範囲の代替

print(
    re.search(
    pattern=r'\d匹の猫',
    string='3匹の猫が公園で寝ていた。'
    ))

# 0回以上の繰り返し *   # 1回以上の繰り返し +  
print(
re.search(
    pattern=r'猫*',
    string='猫猫猫猫猫犬'
))

# 行の先頭を表す ^  # 行の末尾を表す $
print(re.search(pattern=r'^猫', string='猫犬兎'))
