total_electrons = int(input())

shells = []

for shell in range(1, total_electrons + 1):
    max_electrons_in_current_shell = 2 * shell ** 2
    if total_electrons >= max_electrons_in_current_shell:
        shells.append(max_electrons_in_current_shell)
        total_electrons -= max_electrons_in_current_shell
        if total_electrons == 0:
            break
    else:
        shells.append(total_electrons)
        break
print(shells)
