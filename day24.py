thisdict = {
    'brand': 'iMac',
    'version': 'macOS Sierra',
    'year': 2012
}
#--- we use copy() to make a copy of a dic
mydict = thisdict.copy()
print(mydict)

#--- another way to make a copy is dict()
x = dict(thisdict)
print(x)

#--- nested dictionaries
mycourses = {
    'course1' : {
        'name' : 'Net1',
        'num' : 255
    },
    'course2' : {
        'name' : 'SEC',
        'num': 430
    },
    'course3' : {
        'name': 'SEW',
        'num' : 245
    },

}
print(mycourses)

#--- another way is to create dics then contain them in another one
college1 = {
    'name' : 'CTI',
    'year' : 2005
}
college2 = {
    'name' : 'ART',
    'year' : 2004
}
college3 = {
    'name' : 'MATH',
    'year' : 2008
}
University = {
    'college1' : college1,
    'college2' : college2,
    'college3' : college3
}
print(University)

#--- we can also usedict() to make a new dic
y = dict(brand="hp", os="windows", year=2015)
print(y)