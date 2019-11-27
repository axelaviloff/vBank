import re

def isCpfValid(cpf):

    if not isinstance(cpf,str):
        return False

    cpf = re.sub("[^0-9]",'',cpf)

    for i in range(1, 10):
        if cpf == str(i)*11:
            return False

    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    """ Calculating the first cpf check digit. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False