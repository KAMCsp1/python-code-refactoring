# Code Review

## Initial Review

I ran the original script first to see what it does. It printed:

```
Processed Numbers: [3, 4, 9, 8, 15, 12, 21]
Processed Strings: apple BANANA kiwi GRAPEFRUIT CHERRY
```

So it works. The problem is that it's hard to tell why it prints that without going through the code carefully. These are the three main things I noticed.

### 1. The names don't explain anything

`do_math_stuff` and `do_string_stuff` could mean almost anything. Inside the code it gets worse, with `list1`, `list2`, `x` and `s`. I had to trace the loops to work out that `x` was the string being built. Better names would save the next person that effort.

### 2. There's no documentation

None of the functions have docstrings. The rules are only in the code: even numbers get doubled, odd numbers get tripled, and words longer than five letters become uppercase. Someone reading it for the first time wouldn't know if the `> 5` was intentional or a random number.

### 3. Some of the code is longer than it needs to be

`do_math_stuff` creates an empty list and appends to it inside a loop, which is exactly what a list comprehension is for. `do_string_stuff` adds a space after every word and then calls `strip()` to remove the extra one at the end. That's an extra step just to fix something the loop caused, and it would be easy to break if someone edited it.

