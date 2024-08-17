# loss and profit is measured as selling price - cost price  if sp>cp profit and if sp<cp loss
cp = float(input('enter the cost price : '))
sp = float(input('enter the selling price : '))

print(f'profit of {sp-cp} and profit% is {((sp-cp)/cp)*100}%' if sp>cp 
      else f'loss of {cp-sp} and loss% is {((cp-sp)/cp)*100}%')
