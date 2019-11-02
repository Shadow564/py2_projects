form_1 = raw_input("Standard or Intercept: ")
form_2 = raw_input("Standard or Intercept: ")

def s_s():
    a_1 = int(raw_input("1_a: "))
    b_1 = int(raw_input("1_b: "))
    
    c_1 = int(raw_input("1_c: "))
    a_2 = int(raw_input("2_a: "))
    b_2 = int(raw_input("2_b: "))
    c_2 = int(raw_input("2_c: "))
    x = (((b_2 * c_1) - (b_1 * c_2)) / ((a_1 * b_2) - (a_2 * b_1)))
    y =  (c_1 - (a_1 * x)) / b_1
    print x
    print y
    
def s_i(first):
    pass

def i_i():
    pass

if form_1 == "Standard":
    if form_2 == "Standard":
        s_s()
    else:
        s_i(s)
else:
    if form_2 == "Standard":
        s_i(i)
    else:
        i_i()
