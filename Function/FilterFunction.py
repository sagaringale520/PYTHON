#Filter FUnction

item=[1000,2000,3000,4000,5000]

distApply=filter(lambda x:x>=2500,item)

print(type(distApply))
gt_list=list(distApply)

print(gt_list)