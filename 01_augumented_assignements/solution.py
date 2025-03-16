# do not change the method name
def main():
    balance = 5000
    print("================== BALANCE ====================\n")
    print(f"Current Balance: ${balance:.1f}")

    deposit = 1000
    print(f"How much do you want to deposit: ${deposit}")
    balance += deposit  
    print(f"Balance Successfully Updated: ${balance:.1f}")

    withdraw = 500
    print(f"How much do you want to withdraw: ${withdraw}")
    fee = withdraw * 0.03
    print("There is a 3% transaction fee on the withdrawal.")
    print(f"Withdrawal: ${withdraw:.1f} - Fee: ${fee:.1f}")
    
    balance -= (withdraw + fee)  
    print(f"Balance Successfully Updated: ${balance:.1f}\n")

    print("============ TRANSACTION COMPLETED ============")
    
    # write your code here with 4 space intentation

# do not change the following lines:    
if __name__ == "__main__":
    main()