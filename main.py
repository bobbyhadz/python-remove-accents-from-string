# Remove accents from a String in Python

from unidecode import unidecode

str_with_accents = 'ÂéüÒÑ'

str_without_accents = unidecode(str_with_accents)

print(str_without_accents)  # 👉️ 'AeuON'