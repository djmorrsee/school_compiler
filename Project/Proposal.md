# Project Proposal

## John Bucuvalas and Daniel Morrissey

### The Problem

Because of the ambiguous nature of python's dynamic typing, simple expressions
in our host language have translated into sometimes monumental syntax trees 
in the target language. For example:

	`5 + 3`
	
should be a simple translation, but due to the requirement of type checking, 
the naive compilation could end up with a mess of compares and conditionals, all 
to simply evaluate `8`

### Our Approach

We will take on the class of optimizations that fall under the title of 
constant folding and propogation. This generally looks like this:

	x = 3 + 11
	y = x + 3
	return y + 5
	
Would be simplified to:

	x = 14			// Folding
	y = x + 3		
	return y + 5
	
And then to:

	x = 14
	y = 14 + 3		// Propogation
	return y + 5
	
These steps can be repeated indefinitely, optionally removing dead assignments:

	return 22
	
And if that was a function, the function call could potentially be replaced with the 
evaluated expression:

	def foo():
		return 5
		
	x = foo()
	
Would simply become:

	x = 5

### What makes it interesting

**Dynamic Typing**

Python's dynamic typing leads to interesting challenges with constant folding and 
propogation. We will likely be required to implement compile time type checking in 
order for folding to work properly. 

**How Simple?**

How much we decide to propogate enables us to do some experimentation with our procedure.
We've seen that function calls can be propogated away, and the same can be done with 
conditional statements and loops.  

### Measuring Up

Our goals is to decrease the number of run time statements in our 
compiled results. Once we are satisfied with our course compiler, we will branch it,
and use it as a benchmark.

From there, folding and propogation phases will be added before the explication phase.

Number of statements executed at runtime can be determined readily via 
various debugging tools available.
