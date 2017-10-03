def cmprlist(x, y):
    if x == y:
        print "The lists are the same"
    else:
        print "The lists are not the same"


x = [1,2,5,6,2]
y = [1,2,5,6,2]
cmprlist(x,y)


x= [1,2,5,6,5]
y = [1,2,5,6,5,3]
cmprlist(x,y)



x= [1,2,5,6,5,16]
y = [1,2,5,6,5]
cmprlist(x,y)


x= ['celery','carrots','bread','milk']
y= ['celery','carrots','bread','cream']
cmprlist(x,y)
