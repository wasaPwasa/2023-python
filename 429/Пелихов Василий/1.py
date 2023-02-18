import datetime


my_data = {"Пелихов Василий Владимирович" , 28, 10, 2003}
attestate = {
	"русский": 5,
	"география": 5,
	"алгебра":5,
	"история":5,
	"ОБЖ": 5
	}
family_names = {"Владимир", "Екатерина", "Анастасия"}
kiwa_name = "Маркиз"

mean_mark = sum(attestate.values()) / len(attestate)
print("Mean mark:", mean_mark)

unique_names = []
for name in family_names:
	if name in unique_names:
		continue
    unique_names.append(name)
print(unique_names)
print(*set(family_names)) # (f_names[0], (f_names[1])
print(*bytearray((kiwa_name, 'urf-8'))

today = datetime.datatime.today()
my_bday = datetime.datetime (day = my_data[1],
                             month=my_data[2],
                             year=my_data[3])
print((today - my_bday).days)     

stuff = queue
