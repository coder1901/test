
For all those moving from pass-by-value languages like C/C++, this might be of some help. Let's try out some operations! Let's define a list

```
    >>> a = [1,2,3]
    >>> b = a
    
```

Now, when you do

```
    >>> b[1] = 4 
```

what do you expect a[1] to be? Had it been good old C/C++, we wouldn't have expected a[1] to change to 4, but here it does, reason being, assignment in python implies the assignment of references. That effectively means that the lists **a **and **b **now point to the same address in memory.



```
    >>> id(a)
    46713392
    >>> id(b)
    46713392 
```

So, How do we copy a list, or for that sake any data structure say a tuple or a dictionary? Python has a built-in module named copy for conventional copying operations.

    
```
>>> import copy
>>> a = {'A':1,'B':2}
>>> b = copy.copy(a)
>>> id(b)==id(a)

``` 


As is evident, the copy is copy-by-value and not reference. Let's try out some more examples

```
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [a,b]
>>> d = copy.copy(c)
>>> id(d)==id(c)
False
>>> id(d[0])==id(c[0])
True
>>>

```

See what happened here? So, basically the nested or compounded structures cannot be completely handled by copy. That's why, it's also called a shallow** copy.** Analogically, there does exist a method called **deepcopy** to do the job for you.

```
>>> d = copy.deepcopy(c)
>>> id(d[0]) == id(c[0])
False
>>>
``` 


Evidently, **copy** and **deepcopy** differ in their approach as copy just copies the containers and fills them with references whereas **deepcopy** goes into each nest and recursively copies everything to a brand new reference. These methods work as it is for user-defined instances of classes as well, in case you are wondering. I'll end with some tweaky ways of copying lists.


```
    
>>> a = [1,2,3]
>>> b = a[:]
>>> id(b) == id(a)
False
>>> c = list(a)
>>> id(c) == id(a)
False

```


Hello
