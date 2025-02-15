# CMPS 2200  Recitation 02

**Name (Team Member 1):Anh Pham________________  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO: your answer goes here**
For $f(n) = 1$, we only add 1 to total work, which is a small constant amount of work. We do about n steps of work across all levels in total so the asymptotic behavior is $O(n)$.

For $f(n) = \log n$, since a = 2, each level doubles the number of recursive calls. there are logn levels since the problem keeps halving n at each level. however, at each level, there is slightly more work than just log n. So the total work when summing all the levels is O(log n + c) where c is summation of i2^i, where i represents the level of recursion.

For $f(n) = n$, since each level does about O(n) work, and there are O(log n) levels due to halving, the total work sums up to O(nlogn)

For f(n) = 1, the curve grows linearly, confirming W(n) = O(n)
For f(n) = logn, the curve grows slightly faster than O(logn) but such slower than O(n), confirming our total work. 
For f(n) = n, the curve confirms O(nlogn) with a gradual super-linear growth. 

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**TODO: your answer goes here**

For $c < \log_b a$, the recursion contributes more work than f(n) so the total work is root dominated. The recurrence behaves like $O(n^\log_b a)$, where the splitting determines the complexity.

For $c > \log_b a$, f(n) contributes more work than the recursion so the recursive part is negligible and is leaf dominated. Hence the big O is $n^c$.

For $c = \log_b a$, Here, the work done at each level is balanced with each recursive call. There is an extra logn work to account for contributions across levels, so the total work is $O(n^c \log n)$

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**

For f(n) = 1, since span is assuming we have infinite processors, we only count the depth of the tree, hence S(n) = O(log n)

For f(n) = log n, after splitting the problem, each level does a little extra work of log n. Since each level adds a small delay, the total delay accumulates over time, making big O(log^2 n).

For f(n) = n, since each step depends on finishing the previous one, you can't speed this up in parallel. Since you have to compute in full sequential way, and is as long as the total work. Hence O(n)

