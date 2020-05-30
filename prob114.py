#출력하기
x = int(input("입력값 = "))
if x >= 0 and x < 255:
    if x <= 235:
        print(x + 20)
    else:
        print(255)
