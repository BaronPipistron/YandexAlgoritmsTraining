new_number = input().replace('+7', '8').replace('-', '').replace('(', '').replace(')', '')
pnumber1 = input().replace('+7', '8').replace('-', '').replace('(', '').replace(')', '')
pnumber2 = input().replace('+7', '8').replace('-', '').replace('(', '').replace(')', '')
pnumber3 = input().replace('+7', '8').replace('-', '').replace('(', '').replace(')', '')


def check_pnumber(pnumber, new_number):
    if pnumber == new_number:
        print("YES")
    else:
        print("NO")


def work_number(pnumber, new_number):
    if len(pnumber) == 11:
        check_pnumber(pnumber, new_number)
    elif len(pnumber) == 7:
        pnumber = '8495' + pnumber
        check_pnumber(pnumber, new_number)
    elif len(pnumber) == 8:
        pnumber = '8495' + pnumber[1:]
        check_pnumber(pnumber, new_number)


if len(new_number) == 7:
    new_number = '8495' + new_number
elif len(new_number) == 8:
    new_number = '8495' + new_number[1:]

work_number(pnumber1, new_number)
work_number(pnumber2, new_number)
work_number(pnumber3, new_number)
