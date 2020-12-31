<p align="center">
  <a href="https://medium.com/hackernoon/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed#6698">
    <h1 align="center"> Sliding Window </h1>
  </a>
  <img src="https://media.giphy.com/media/5xaOcLSiHjl31yG4ZNK/giphy.gif" width="1000" />
</p>

Following ***are some ways you can identify that the given problem might require a sliding window:***
* The problem input is a linear data structure such as a linked list, array, or string
* You’re asked to find the longest/shortest substring, subarray, or a desired value
* There is an apparent naive or brute force solution that runs in O(N²), O(2^N) or some other large time complexity.

![Types of Sliding Windows](https://user-images.githubusercontent.com/11432315/103430665-407e1f00-4b7b-11eb-9096-1dab9d473b4c.png )

Fast/Slow:

* Fast pointer will grow your window under a certain condition and slow pointer will shrink if certain conditions are met. 
* ex Minimum window substring, Bit flip, Consecutive subarray sum

Fast/Catch-up:

* Fast pointer will expand window under a certain condition and slow pointer will immediately meet with fast pointer if certain conditions are met. 
* ex Max consecutive sum, Buy and sell stocks

Fast/Lagging

* The slow pointer is simply referencing one or two indices behind the fast pointer and it’s keeping track of some choice you’ve made.
* House robber

Front/Back

* front and back pointers will shrink to find the maximum value of something within an array. 
* ex Rain water, Sorted two sum

Examples:

* Maximum sum subarray of size ‘K’
* Longest substring with ‘K’ distinct characters
* String anagrams

