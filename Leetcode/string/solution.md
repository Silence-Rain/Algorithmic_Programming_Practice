# Solution of String's Problem

### Easy



### Medium

- \#3 Longest Substring Without Repeating Characters

  Basic idea: 2 pointers, hash table

  - Build up a hash table to record all the letters in current longest substring
  - Set up a slow pointer `i` to represent the beginning of current substring, and a fast pointer `j` as the end
  - If `s[j]` not in the hash table, then current substring `s[i:j]` is a valid substring. Otherwise, remove `s[i]` from the hash table and start with `i + 1`

- \#5 Longest Palindromic Substring

  

### Hard

- \#30 Substring with Concatenation of All Words

  Basic idea: Hash table, 2 pointers

  - Build up a hash table to record the appearance time of each word in `words`, and the length of each word is `w_l`
  - Set up a slow pointer `i` to represent the beginning of current substring, then set up a variable `temp_str` and assign it by each `w_l` letters in order
  - Find `temp_str` in the hash table. If failed, then move `i` ahead. Otherwise, `i` is the index we are looking for

- \#65. Valid Number

  Basic idea: Modularization

  - Design corresponding methods to determine sign, unsigned integer, signed integer, and decimal