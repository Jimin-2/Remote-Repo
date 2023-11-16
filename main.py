def check_even():
    try:
        # 사용자로부터 숫자 입력 받기
        number = int(input("숫자를 입력하세요: "))
        
        # 입력한 숫자가 짝수인지 확인
        if number % 2 == 0:
            print(f"{number}은(는) 짝수입니다.")
        else:
            print(f"{number}은(는) 홀수입니다.")
    
    except ValueError:
        print("유효한 숫자를 입력하세요.")

check_even()

def sum_two_numbers(a, b):
    return a + b
