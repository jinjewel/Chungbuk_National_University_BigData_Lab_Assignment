num_year = '2016'
num_month = '01'
# num_day = '03'
for num_day in range(1, 31):
    if len(str(num_day)) == 1:
        num_day = '0' + str(num_day)
    num_date = str(num_year) + "-" + str(num_month) + "-" + str(num_day)
    print(num_date)