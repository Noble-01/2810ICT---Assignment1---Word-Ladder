# 2810ICT---Assignment1---Word-Ladder
---
**Assignment Description**

This assignment is a small group based assignment that requires a Python program to be
completed that demonstrates understanding of the scripting languages taught in the course.
As part of completing the program, existing functionality will need to be tested to ensure it
is working correctly and new functions will be added to the program. A version control
system shall be used to build the project and create and manage changes to source code over time.

---
**Problem Statement**

The goal of a ladder-gram is to transform a source word into the target word in the least
number of steps. During each step, you must replace one letter in the previous word so that
a new word is formed, but without changing the positions of the other letters. All words
must exist in the supplied dictionary (dictionary.txt). For example, we can achieve the
alchemist's dream of changing “lead” to “gold” in 3 steps (lead->load->goad->gold), or
“hide” to “seek” in 6 steps (hide->side->site->sits->sies->sees->seek).
You have been supplied with a Python program (word_ladder.py) for this problem that was
written by an obviously brilliant Python programmer who unfortunately did not believe in
documentation nor that users would make any mistakes. Even worse, this code has been
modified by a somewhat less talented programmer and it no longer works as efficiently as it
used to.

Your assignment is to:

- Produce a software design document based on the sample template for this
program. In particular you must document each function within the program stating
clearly what they do and how they do it.
- You must modify the Python code so that:
  - ALL possible user input errors are handled correctly.
  - The program performs as it did before the less talented programmer got his
hands on it. In particular it must go from “lead” to “gold” in 3 steps and
“hide” to “seek” in 6 steps.
- You must use the Python unittest module to test the functions of your program and
provide test cases for each function. Note that to facilitate the testing, you can
rewrite the code to make it testable.
- You must make all program changes using a configuration management tool
(BitBucket recommended) such that each change can be tracked and easily undone.
- For full marks, you must add the following functionality to the program:
  - The user can supply a list of words that are not allowed to be used within the
  steps from a start word to a target word.
  - The user has the option of supplying a word that must exist on the path to
  the target word. (HINT: split this into 2 paths, making sure the target word
  doesn’t appear on the first path to the intermediary word )
