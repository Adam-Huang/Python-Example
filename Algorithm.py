
def interestsum(unitin,rate,num):
    reslut = 0
    while num > 1:
        reslut = reslut + (unitin * rate) ** num
        num -= 1
    return reslut

if __name__ == '__main__':
    result = interestsum(7000,1.0003,num=60)
    print(result)
