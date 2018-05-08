import re

def validate_phone_number(number):
    # pass 함수에 내용이 없을 경우
    if not re.match(r'^01[016789][1~9]\d{6,7}$', number):
        return False
    return True


print(validate_phone_number('0101234567'))
print(validate_phone_number('010123567'))
print(validate_phone_number('01012345678'))
print(validate_phone_number('01012567'))