


def main(types, length=12):
    import random
    import string

    chars = ''

    if '小文字' in types:
        chars += string.ascii_lowercase
    if '大文字' in types:
        chars += string.ascii_uppercase
    if '数字' in types:
        chars += string.digits
    if '記号' in types:
        chars += string.punctuation

    if chars == '':
        return '文字種類を選択してください'

    return ''.join(random.choice(chars) for _ in range(length))  # _ とは使わない変数