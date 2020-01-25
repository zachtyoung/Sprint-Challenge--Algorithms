#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - Linear time- becuase the run time will grow as the input size increases


b)O(n^2) - because the run time will grow exponentially as the input size increaes because of the nested loop


c)O(n) since its just an additional loop per n increase

## Exercise II
First attempt answer : Starting on the first floor, drop an egg. Keep moving up floors until it breaks. Wherever floor it breaks is f. O(n)


Second attempt answer: "optimized" We can use a binary search easily since the floors are already sorted. I still stand by my first answer even though it might be "brute force". Becuase due to laws of nature the in the case of buildings, the amount of floors in a building will not reach a number that a binary search will have a significant advantage on run time. 

Nonethless to implement a binary search we would want to find the midpoint by subtracting the min floor from the max floor. We then check if the egg breaks at the midpoint and if does then repeat for the first half of the floors. If it does not break then repeat for the second half of the floors. We eventually find the max floor we can drop the egg from and it not break. The time complexity is O(log n). But in this case I still don't see a significant total runtime reduction given the relatively small amount of floors on can find in even the tallest buidlings. 

