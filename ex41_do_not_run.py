# learning to speak object-oriented

class # tells python to make a new type of thing.

object # Two meanings: the most basic type of thing, and instance of some thing.

instance # what you get when you tell python to create a class.

def # how you define a function inside a class.

self # inside the functions in a class, self is a variable for the instance/object
# being accessed.

inheritance # the concept that one class can inherit traits from another class
# much like and your parents.

composition # the concept that a class can be composed of other classes as parts
# much like how a car has wheels

atribute # a property classes have that are from composition and are usually
# variable.

is-a # a phrase to say that something inherits from another, as in a "salmon"
# is-a "fish".

has-a # a phrase to say that something is composed of other things or has a trait
# as in "a salmon has-a mouth".

class X(Y) Make a class named X that is-a Y.

class X(object): def__init__(self, J)  class x has-a__init__ that take self
and J paramaters.

class X(object): def M(self, J) "class X has-a function named M that takes self",
"and J paramaters"

foo = X() "Set foo to an instance of class X"
foo.M(J) "From foo, get the M function, and call it with paramaters self J."
foo.K = Q "From foo, get the K attribute, and set it to Q."

# In each of these, where you see X, Y, M, J, K, Q, and foo, you can treat those
# like blank spots. For example, I can also write these senteces as follows:

1. "Make a calss named ??? that is-a Y."
2. "class ??? has-a__init__that tae self and ??? paramaters."
3. "class ??? has-a function named ??? that takes self and ??? parameters."
4. "Set ??? to an instance of class ???."
5. "From ???, get the ??? function, and call it with self=??? and parameters ???."
6. "From ???, get the ??? attribute, and set it to ???."
