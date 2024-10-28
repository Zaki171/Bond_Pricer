

def pricer(par_val, ytm, coup, coup_freq, T):
    bond_price = 0
    N = int(coup_freq*T)
    for t in range(1,N+1):
        if t == N:
            bond_price += ((par_val*coup)/coup_freq + par_val)/((1+ytm/coup_freq)**t)
        else:
            bond_price += ((par_val*coup)/coup_freq)/((1+ytm/coup_freq)**t)
    return bond_price

print(pricer(1000, 0.15, 0.1, 1, 20))
print(pricer(1000, 0.15, 0.1, 2, 5))

print(pricer(1000, 0.065, 0.05, 1, 20)-pricer(1000, 0.065, 0.05, 1, 17))

print(pricer(1000, 0.12, 0.06, 2, 2))
