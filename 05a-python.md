# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are very similar in function, both are arrays of elements.  However the important distinction is that Tuples are immutable, and cannot be changed.

Tuples can be used as keys in ditionaries and lists cannot.



---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists can contain multiple of the same element, eg. (a,b,c,a)

Set elements must be unique, so a set of the above list would be  (a,b,c)

Sets are faster if you are just trying to find a unique value, but lists are faster if your iterating over the list

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda functions are anonymous functions that essentially allow you to create a 'temporary' function.  This way you can create a function within another function without having to create a whole separate function. Lambda functions can only be one line

As an example you could have a list of words ['this', 'iS', 'a', 'List']

Then you can use the sorted function which takes a key (which is another fucntion) that will iterate through the list and perform an operation

key= lambda word.lower()

This function would allow you to iterate through the list, and ouput the sorted list after lowercasing each element in the list

The advantage of a lambda function here is that you can write it in-line with the rest of the sorted function, rather than having to create a separate function and call it

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehension allows you to iterate through a list and perform a function on each element.  'Map' a function that works the same as list comprehension that takes a function and a list as parameters, then iterates the function over the list and gives you the output.

An example for a list comp. and it's map counterpart:

numlist = [1...10]

squared_list = [n*n for n in numlist]

This will iterate though numlist and square each element

Map version:

squared_list = map(lambda n: n*n, numlist)

These do the same, but the list comprehension is a bit eaiser to read.

Filter will iterate through a list and return a value if it meets the 'if' requirement.  For example:

even_numbers = filter(lambda n: n%2==0, numlist)

Would return all the even numbers (or numbers that have a remainder of 0 when divded by 2)

This can be done in list comprehension

In summary list comprehension > map/filter > for loop (in these cases)

Dictionary comprehension would allow you to iterate through a list and create a dictionary from it

Set comprehension allows you to iterate through a list and create a set

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





