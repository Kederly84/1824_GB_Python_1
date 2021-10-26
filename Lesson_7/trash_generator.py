# Примитивный генератор мусора для заданий 7_4 и 7_5
import os
import random
from string import ascii_lowercase, digits

extensions = ['.bin', '.py', '.txt', '.css', '.txt']
letters = ''.join([ascii_lowercase, digits])
folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trash')
if not os.path.exists(folder):
    os.mkdir(folder)
for _ in range(10 ** 2):
    name = ''.join(random.sample(letters, random.randint(5, 10)))
    ext = random.sample(extensions, 1)
    f_ext = ext[0]
    content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 6)))
    with open(os.path.join(folder, f'{name}{f_ext}'), 'wb') as f:
        f.write(content)
