import numpy as np

def cash_flows_calc(par_val, coup, coup_freq, ytm, N):
    cash_flow_list = []
    for t in range(1,N+1):
        if t == N:
            cash_flow_list.append(((par_val*coup)/coup_freq + par_val)/((1+ytm/coup_freq)**t))
        else:
            cash_flow_list.append(((par_val*coup)/coup_freq)/((1+ytm/coup_freq)**t))
    return cash_flow_list


def pricer(par_val, ytm, coup, coup_freq, T):
    bond_price = 0
    N = int(coup_freq*T)
    cash_flows = cash_flows_calc(par_val, coup, coup_freq, ytm, N)
    bond_price = sum(cash_flows)
    return bond_price

def duration(par_val, ytm, coup, coup_freq, T):
    N = int(coup_freq * T)
    cash_flows = cash_flows_calc(par_val, coup, coup_freq, ytm, N)
    mac_dur = 0
    for i in range(len(cash_flows)):
        w = cash_flows[i]/par_val
        mac_dur += w*(i+1)
    print("Macauly Duration: ", mac_dur)
    mod_dur = mac_dur/(1+ytm)
    print("Modified Duration: ", mod_dur)
    return mod_dur

        


