import math

class Fraction:
    '''Fraction class with numerator and denominator'''
    def __init__(self,top,bottom):
        self.num=top #constuctor, defines Fraction object to have internal data object(num) as part of state
        self.den=bottom
        #to create instance of this class, we must invoke the instructor, call the function

    def __str__(self):
        '''Overrides original __str__ function to show string representation of function'''
        return str(self.num)+'/'+str(self.den)
    
    def __add__(self, other):
        '''Adding two fractions by finding a common denominator'''
        newnum = self.num*other.den + self.den*other.num
        newden = self.den*other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den*other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self,other):
        ''' Overriding default __eq__ function to focus on values(deep equality)'''
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum == secondnum
    
    def __mul__(self, other):
        newnum = self.num*other.num
        newden = self.den*other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __truediv__(self, other):
        #div is divided into floordiv and truediv
        newnum = self.num*other.den
        newden = self.den*other.num
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __lt__(self,other):	
        firstnum = self.num*other.den
        secondnum = self.den*other.num
        return firstnum < secondnum

    def __le__(self,other):	
        firstnum = self.num*other.den
        secondnum = self.den*other.num
        return firstnum <= secondnum

    def __gt__(self,other):	
        firstnum = self.num*other.den
        secondnum = self.den*other.num
        return firstnum > secondnum

    def __ge__(self,other):	
        firstnum = self.num*other.den
        secondnum = self.den*other.num
        return firstnum >= secondnum
    
    def __ne__(self,other):	
        firstnum = self.num*other.den
        secondnum = self.den*other.num
        return firstnum != secondnum

       
def gcd(m,n):
    '''finds greatest common divisor'''
    while (m%n != 0):
        common = m % n
        m = n
        n = common
    return n
