# Annual growth of money, with tax deductions considered
invest = 6000 #annual investment
p = invest #principal
r = 6.5 #rate in percent
t = 1 #time in years
startYear = 2019
endYear = 2039
years = range(startYear, endYear) 
for y in years:
    interest = (p * t * r / 100)
    p = p + interest
    p = p - (interest * 10 / 100) #tax deduction on the interest    
    print('Amount at the end of year ', y, ': ', p)        
    p = p + invest #continuing to invest

print('--------------------------------------------')
print('Timespan: ', len(years), ' years')
