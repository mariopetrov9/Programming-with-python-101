# Mixins

## Serializers/Deserializers to and from JSON / XML

In a python module `utils.serializers`, we convert panda objects to JSON / XML, using 'Jsonable' and 'Xmlable' classes:

We have the same idea the other way around - we create panda instances from their respective JSON / XML representations:


### Hints

* For XML, we use the standard library - <https://docs.python.org/3/library/xml.etree.elementtree.html>

## Enumerable

By the `Collection` class, we can do the following:

* Take a variable number or arguments in its contructor - `Collection(1, 2, 3)`
* Implement the **iterator pattern**.
* Implement equality - `Collection(1) == Collection(1)`


In our Collection, we mixin some classes - `Enumerable` and `Exensible` in order to do the following 
operations:

* c = Collection(1, 2, 3)
* c == c.map(lambda x: x)
* 6 == c.reduce(0, lambda x, y: x + y)
* Collection(1, 2) == c.take(2)
* Collection(3) == c.drop(2)
* Collection(0, 0, 0) == Collection(0, 0, 0, 1).take_while(lambda x: x == 0)
* Collection(1) == Collection(0, 0, 0, 1).drop_while(lambda x: x == 0)
* Collection(1).search(1)

The `Extensible` mixing implements a method, that reacts to the `+` operator.

It returns a new **whatever collection that mixes in `Extensible`** with the concatenation.
