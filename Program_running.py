#prdict the properties (density,self-coefficients and viscosity) of carbonate melts
#Set input variable:T,System,n and targets
from function import Model_predict_1,make_i,Model_predict_2
T=input()
if T is not int:
    print('please enter an integer.')
print("Next write the composition of system (Li2CO3-K2CO3 or Li2CO3-Na2CO3 or Na2CO3-K2CO3):")
System = input()
if System is not 'Li2CO3-K2CO3' or System is not 'Li2CO3-Na2CO3' or System is not 'Na2CO3-K2CO3':
    print("Input format error")
else:
    print("Very good")
print("Next write n:")
n=float(input())
#Set Li2CO3:10 Na2CO3:100 K2CO3:1000 eg:Li2CO3(0.4)-Na2CO3(0.6) Feature:10*100*0.4=450
if "Li" in System and "Na" in System:
    N=10*100*n
elif "Li" in System and "K" in System:
    N=10*1000*n
elif "Na" in System and "K" in System:
    N=100*1000*n
print("Next write your targets (density or self-coefficients or viscosity):")
Target=input()
if Target !=  'self-coefficients':
    result=Model_predict_1(T,System,N,Target)
else:
    print("Which ion (Li+ or Na+ or K+ or CO32-)")
    Target_ion=input()
    i=make_i(System,Target_ion)
    result=Model_predict_2(T,System,N,Target,i)
print(result)