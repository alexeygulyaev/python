# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
# - его длина не менее 88 символов;
# - он содержит как минимум одну заглавную букву (верхний регистр);
# - он содержит как минимум одну строчную букву (нижний регистр);
# - он содержит хотя бы одну цифру.

def is_password_good(password):
    upper = 0
    digit = 0
    lower = 0
    if len(password) >= 8:
        for i in password:
            if i.isupper():
                upper += 1
            if i.isdigit():
                digit += 1
            if i.islower():
                lower += 1

    if upper >= 1 and digit >= 1 and lower >= 1:
        return True
    else:
        return False


txt = input()

print(is_password_good(txt))