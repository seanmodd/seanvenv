import abstra.dashes as ad

"""
Abstra dashes are the simplest way to build custom user interfaces for your APIs.
"""

x = 2
y = 3


def get_sum():
    return x + y


def show_sum():
    # ad.alert(str(get_sum()))
    ad.alert("The sum is: " + str(get_sum()))

# q: create an alert that will get the sum but will show it as: "The sum is: "
# a: ad.alert("The sum is: " + str(get_sum()))
 