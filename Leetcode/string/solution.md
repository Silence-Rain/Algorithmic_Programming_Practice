# Solution of String's Problems

### Easy



### Medium

- \#3 Longest Substring Without Repeating Characters

  Basic idea: 2 pointers, hash table

  - Build up a hash table to record all the letters in current longest substring
  - Set up a slow pointer `i` to represent the beginning of current substring, and a fast pointer `j` as the end
  - If `s[j]` not in the hash table, then current substring `s[i:j]` is a valid substring. Otherwise, remove `s[i]` from the hash table and start with `i + 1`

- \#5 Longest Palindromic Substring

  Basic idea: 1-pass, use each index as the middle point of palindromic substring

  - Set a variable `maxLen` to record the max length of substring currently
  - For each index, treat it as the middle point of possible palindromic substring, expand the substring to both left and right if both adjacent letters are the same
  - If the right adjacent letter is the same as the middle point's letter, expand the substring to the right
  - If the length between current index and the end of the string is less than `maxLen / 2`, then the longest substring is found

- \#6 ZigZag Conversion

  Basic idea: Remainder

  - The line indices of the next letter have a period of `2 * (numRows - 1)`
  - During the period, the indices have the pattern of `0…n…1`

- \#8 String to Integer (atoi)

  Basic idea: Regular expression

  - Use regular expression to filter the accurate format
  - Use built-in function to complete the conversion
  - Return the result after boundary check

- \#22 Generate Parentheses

  Basic idea: Recursive solution

  - A valid sequence of parentheses must contain the same number (exactly `n`) of `(` and `)`, and must start with `(`

- \#49 Group Anagrams

  Basic idea: Hash table, tuple-shaped key

  - Construct a `char_map` for each word to record the frequency of each letter
  - Use the tuple version of `char_map` as the key of the word in the hash table

- \#71 Simplify Path

  Basic idea: Stack

  - Split the path by `/`
  - Simplify the path according to the rules, then put correct compartment into stack

### Hard

- \#30 Substring with Concatenation of All Words

  Basic idea: Hash table, 2 pointers

  - Build up a hash table to record the appearance time of each word in `words`, and the length of each word is `w_l`
  - Set up a slow pointer `i` to represent the beginning of current substring, then set up a variable `temp_str` and assign it by each `w_l` letters in order
  - Find `temp_str` in the hash table. If failed, then move `i` ahead. Otherwise, `i` is the index we are looking for

- \#65. Valid Number

  Basic idea: Modularization

  - Design corresponding methods to determine sign, unsigned integer, signed integer, and decimal