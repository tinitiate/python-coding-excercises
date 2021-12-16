import lms_system as lms
import random

# ###################################################################################
# MAIN SECTION
# ###################################################################################

# Supply all inputs
l_CustName    = "AB"
l_CreditScore = 255
l_LoanAmount  = 17000
l_master_data = lms.getMasterData()
l_check = {}
l_res = None

# Call Business Logic functions
l_check = lms.qualifyCheck(p_master_data=l_master_data,p_CreditScore=l_CreditScore,p_LoanAmount=l_LoanAmount)

if l_check["status"] == "success":
    l_res = lms.calculateLoanDetails(l_master_data,l_CustName,l_CreditScore,l_LoanAmount)
    print(l_res)
else:
    print(l_check)


for c in range(1000):
    l_cs = random.randint(200,499)
    l_la = random.randint(10000,30000)
    # Call Business Logic functions
    l_check = lms.qualifyCheck(p_master_data=l_master_data,p_CreditScore=l_cs,p_LoanAmount=l_la)

    if l_check["status"] == "success":
        l_res = lms.calculateLoanDetails(l_master_data,"a",l_cs,l_la)
        print(l_res)
    else:
        print(l_check)
    