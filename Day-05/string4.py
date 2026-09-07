#String Methods
s1='stuDENts are good'
print(s1.lower())
print(s1.upper())
print(s1.capitalize())
print(s1.title())
print(s1.swapcase())


# checking string method.
s1='stuDENts are good'
print(s1.islower())
print(s1.isupper())
print(s1.isalnum())
print(s1.isalpha())
print(s1.isdigit())
print(s1.isspace())
print(' '.isspace())

#
s1='stuDENts are good'
print(list(s1))
print(s1.split('#'))
print(s1.split())
print(' '.join(s1.split()))

#replaceing string.
s='i love python'
print(s.replace('python','DSA'))
print(s)

#strips(removing space)
s='          python   Programming             '
print(s.strip())# remove total space except middle.
print(s.lstrip())#remove left side space.
print(s.rstrip())#remove right side space.