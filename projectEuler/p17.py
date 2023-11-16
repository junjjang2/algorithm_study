# Number Letter Counts

# how many thousands, hundreds, tens, ones appears in the numbers from 1 to 1000?

# thousand : 1 (1000)
# hundred: 100~999 (900)
# ten: 10, 110, 210, ..., 910 (10)
# twenty : 20~29, 120~129, ..., 920~929 (10*10)
# thirty : 30~39, 130~139, ..., 930~939 (10*10)
# ... 
# ninety : 90~99, 190~199, ..., 990~999 (10*10)
# ... this is naughty.

# convert 1~99 to string
# 1~9: one, two, three, four, five, six, seven, eight, nine
# 10~19: ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
# 20~29: twenty, twenty-one, twenty-two, twenty-three, twenty-four, twenty-five, twenty-six, twenty-seven, twenty-eight, twenty-nine
# ...
# 90~99: ninety, ninety-one, ninety-two, ninety-three, ninety-four, ninety-five, ninety-six, ninety-seven, ninety-eight, ninety-nine
# split number into (hundreds, below hundred)
# mapping and counting
# sum
# annoying...