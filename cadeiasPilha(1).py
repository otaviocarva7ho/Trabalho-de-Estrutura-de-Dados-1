def push(p, v):
    p.append(v)


def pop(p):
    return p.pop()


def vazia(p):
    return False if p else True


def formaCadeiaCorreta1(cadeia):
    qtdc = 0
    for crt in cadeia:
        if crt.lower() != 'a' and crt.lower() != 'b' and crt.lower() != 'c':
            return False
        if crt.lower() == 'c':
            qtdc += 1

    if qtdc != 1:
        return False

    return True
def formaCadeiaCorreta(cadeia):
    qtdc = 0
    for crt in cadeia:
        if crt.lower() not in 'abc':
            return False
        if crt.lower() == 'c':
            qtdc += 1

    if qtdc != 1:
        return False

    return True


def verificaCadeia(cadeia):
    formaCadeia = True
    aux = []
    i = 0
    if not formaCadeiaCorreta(cadeia):
        return False
    for i in range(len(cadeia)):
        if cadeia[i] != 'c':
            push(aux, cadeia[i])
        else:
            break

    for j in range(i + 1, len(cadeia)):
        if not vazia(aux):
            v = pop(aux)
            if v != cadeia[j]:
                formaCadeia = False
                break
        else:
            formaCadeia = False
            break

    if not vazia(aux):
        formaCadeia = False

    return formaCadeia


cadeia = "ababcabab"
print(f' {cadeia} formaCadeia: {verificaCadeia(cadeia)}')
cadeia = "ababcbaba"
print(f' {cadeia} formaCadeia: {verificaCadeia(cadeia)}')
cadeia = "ababcbab"
print(f' {cadeia} formaCadeia: {verificaCadeia(cadeia)}')
cadeia = "ababcbabaa"
print(f' {cadeia} formaCadeia: {verificaCadeia(cadeia)}')
cadeia = "ababcbabac"
print(f' {cadeia} formaCadeia: {verificaCadeia(cadeia)}')