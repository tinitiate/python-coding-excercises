

# Function to Return master data
# 
# ###################################################################################
# getMasterData
# ###################################################################################
def getMasterData():

    return [
     {"cs_start":100,"cs_end":199,"loan_amt_start":10000,"loan_amt_end":19999,"interest":5  ,"duration":65}
    ,{"cs_start":400,"cs_end":499,"loan_amt_start":10000,"loan_amt_end":19999,"interest":3.5,"duration":65}
    ,{"cs_start":200,"cs_end":299,"loan_amt_start":10000,"loan_amt_end":19999,"interest":4.5,"duration":65}
    ,{"cs_start":300,"cs_end":399,"loan_amt_start":10000,"loan_amt_end":19999,"interest":4  ,"duration":65}
    ]
# END getMasterData
# ###################################################################################


# ###################################################################################
# qualifyCheck
# ###################################################################################
def qualifyCheck(p_master_data,p_CreditScore,p_LoanAmount):

    l_all_cs = []
    l_all_loan_amt = []
    l_reject=0

    for c in p_master_data:
        l_all_cs.append(c["cs_start"])
        l_all_cs.append(c["cs_end"])
        l_all_loan_amt.append(c["loan_amt_start"])
        l_all_loan_amt.append(c["loan_amt_end"])

    if p_CreditScore < min(l_all_cs) or p_CreditScore > max(l_all_cs):
        # print("Credit Score Too Low or Too High")
        return { "status":"rejected"
                 ,"reason":"Credit Score Too Low or Too High"}
    #
    elif p_LoanAmount < min(l_all_loan_amt) or p_LoanAmount > max(l_all_loan_amt):
        # print("Requested loan amount Too Low or Too High")
        return { "status":"rejected"
                 ,"reason":"Requested loan amount Too Low or Too High"}
    #
    else:
        return { "status":"success"
                 ,"reason":"Requested loan amount and Credit Score qualified."}
# END qualifyCheck
# ###################################################################################



# ###################################################################################
# calculateLoanDetails
# ###################################################################################
def calculateLoanDetails(p_master_data,p_cust_name,p_CreditScore,p_LoanAmount):
    
    l_total_amount = None
    
    for c in p_master_data:
        #print(c)
        if l_CreditScore >= c["cs_start"] and l_CreditScore <= c["cs_end"] and l_LoanAmount >= c["loan_amt_start"] and l_LoanAmount <= c["loan_amt_end"]:

            l_total_amount = l_LoanAmount + (l_LoanAmount/100)*c["interest"]
            
            return { "status":"success"
                     ,"CustName":p_cust_name
                     ,"CreditScore":p_CreditScore
                     ,"LoanAmount":p_LoanAmount
                     ,"TotalAmount":l_total_amount
                     ,"Interest":c["interest"] 
                     ,"Duration":c["duration"]}
    
    return { "status":"error"
             ,"CustName":p_cust_name
             ,"CreditScore":p_CreditScore
             ,"LoanAmount":p_LoanAmount
             ,"TotalAmount":0
             ,"Interest":0
             ,"Duration":0}
# End calculateLoanDetails
# ###################################################################################



# ###################################################################################
# MAIN SECTION
# ###################################################################################

# Supply all inputs
l_CustName    = "A"
l_CreditScore = 350
l_LoanAmount  = 13000
l_master_data = getMasterData()
l_check = {}
l_res = None

# Call Business Logic functions
l_check = qualifyCheck(p_master_data=l_master_data,p_CreditScore=l_CreditScore,p_LoanAmount=l_LoanAmount)

if l_check["status"] == "success":
    l_res = calculateLoanDetails(l_master_data,l_CustName,l_CreditScore,l_LoanAmount)
    print(l_res)
else:
    print(l_check)


"""
Interest = %
Duration = 72
TotalAmout = LoanAmount + (LoanAmount/100)*Interest
"""
