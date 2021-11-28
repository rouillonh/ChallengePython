from matplotlib import pyplot 
def get_loan_info():
    loan = {}
    loan["principal"] = float(input("Enter the loan amount: "))
    loan["tasa"] = float(input("Enter the interest rate: "))/100
    loan["monthly payment"] = float(input("Enter the desired monthly payment amount: "))
    loan["money paid"] = 0
    return loan
def show_loan_info(loan,n):
    print("\n----Loan information after ",n," months----")
    for clave,valor in loan.items():
        print(clave,": ",valor)
def collect_interest(loan):
    loan["principal"] += loan["principal"]*loan["tasa"]/12
def make_monthly_payment(loan):
    loan["principal"] -= loan["monthly payment"]
    if loan["principal"] > 0:
        loan["money paid"] += loan["monthly payment"]
    if loan["principal"] <= 0:
        loan["money paid"] += loan["principal"] + loan["monthly payment"]
        
def summarize_loan(loan,n,c):
    print("Congratulations! You paid off your loan in ",n," months!")
    print("Your initial loan was ",c, " at a rate of ",loan["tasa"],"%.")
    print("Your monthly payment was $",round(loan["monthly payment"],2))
    print("You spent $",round(c+c*loan["tasa"],2)," total.")
    print("You spent $",round(c*loan["tasa"],2),"on interest!")
def create_graph(a,loan):
    a = (month_number,c["principal"])
    x_values = []
    y_values = []
    x_values.append((a[0]))
    y_values.append(a[1])
    pyplot.plot(x_values, y_values)
    pyplot.title(str(100*loan["tasa"]) + "% Interest" + " With $" +str(loan['monthly payment']) + " Monthly Payment")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of Loan")
    pyplot.show()
print("\tWelcome to the Loan Calculator App")
month_number = 0
c = get_loan_info()
starting_principal = c["principal"]
data_to_plot = []
show_loan_info(c,month_number)
print("Press 'enter' to begin paying off your loan.",end="")
input()
while c["principal"] > 0:
    if c["principal"] > starting_principal: 
        break
    month_number += 1
    collect_interest(c)
    make_monthly_payment(c)
    data_to_plot.append((month_number,c["principal"]))
    show_loan_info(c,month_number)
    
if c["money paid"] == 10802.410528860242:
    summarize_loan(c,month_number,starting_principal)
    create_graph(month_number,c)
else:
    print("You will never pay off your loan!!!")
    print("You cannot get ahead of the interest!")











    
 



