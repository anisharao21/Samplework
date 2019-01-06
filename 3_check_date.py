# validate a given date
# 2015 : not leap
# 2016 : leap
# 1900 : not leap
# 2000 : leap
# divisible by 4 and not by 100
#	or
# by 400
days  = [ None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
line = input("enter date as dd-mm-yyyy : ")
(dd, mm, yy) = line.split("-")
dd = int(dd); mm = int(mm); yy = int(yy)
if yy % 4 == 0 and yy % 100 != 0 \
	or yy % 400 == 0 :
	days[2] = 29
#if mm < 1  or mm > 12 : # ok
#if not 1 <= mm <= 12 :
if mm not in range(1, 12 + 1) :
	print("invalid month")
elif not 1 <= dd <= days[mm] :
	print("invalid date")
else:
	print("valid")
