# Abstaction Over Forms

An implemention of our own abstraction over forms as a simple python module.

Here is the interface that we need to have:

## BaseField

The main class that we are going to use for all forms looks like is called 'BaseField'.

All other Fields should subclass our `BaseField`


## Form

There is a base `Form` class which is a subclass for our forms. A form is a collection of fields.

Each form has a string representation in HTML format.

We validate our fields by 'is_valid()' method.
