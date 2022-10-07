"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    # Your code goes here
    for i in items:
        if str(i) in frequencies:
            frequencies[str(i)]+=1
        else:
            frequencies.update({str(i):1})
    
    return frequencies
