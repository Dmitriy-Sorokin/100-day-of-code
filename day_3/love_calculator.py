name1 = "Kanye West"
name2 = "Kim Kardashian"

common_name = (name1 + name2).lower()
nt = common_name.count("t")
nr = common_name.count("r")
nu = common_name.count("u")
ne = common_name.count("e")

ntl = common_name.count("l")
nro = common_name.count("o")
nuv = common_name.count("v")
nee = common_name.count("e")

fin_count_true = nt + nr + nu + ne
fin_count_love = ntl + nro + nuv + nee
all_counter = str(fin_count_true) + str(fin_count_love)
int_count = int(all_counter)
print(int_count)

if int_count < 10 or int_count > 90:
    print(f"Your score is {int_count}, you go together like coke and mentos.")
elif 40 < int_count < 50:
    print(f"Your score is {int_count}, you are alright together.")
else:
    print(f"Your score is {int_count}.")
