class Item:
  def __init__(self,value,weight):
    self.value = value
    self.weight = weight


def knap(arr,w):
  arr.sort(key=lambda x:x.value/x.weight, reverse=True)
  finalValue = 0.0
  for i in arr:
    if (i.weight<=w):
      w-=i.weight
      finalValue+= i.value
    else:
      finalValue += (w/i.weight)*i.value
      break
  return finalValue



if __name__ == '__main__':
  w = 50
  arr = [Item(60,10),Item(100,20),Item(120,30)]
  knap1 =  knap(arr,w)
  print(knap1)
