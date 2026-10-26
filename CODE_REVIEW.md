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

## Final Review

### Did I fix the three issues?

Yes, all three.

1. **Names:** The functions are now `process_numbers` and `format_words_by_length`, and the variables are `numbers`, `words`, `fruits` and `word`, all in PEP 8 style. To check this, I read `main()` without looking at the rest of the file, and I could understand what it does.
2. **Documentation:** I added a docstring at the top of the file and one for every function, following PEP 257. I ran `help()` on the functions to make sure the docstrings show up properly.
3. **Simpler code:** The number loop is now a list comprehension, and the string function uses `" ".join(...)`, so the `strip()` step isn't needed anymore. I also moved 2, 3 and the word length into named constants. After each change I ran the program and compared the output with the original.

### Are the names clear now?

Yes. You can tell what each function does and what each variable holds just from the name.

### Does every function have documentation?

Yes. All three functions have docstrings, and so does the file itself.

### Is it easier to read and maintain?

I think so. Each function is now a single short statement, and if one of the rules changes, I only need to update one constant.

### Does it still give the expected output?

Yes, the output is exactly the same as before:

```
Processed Numbers: [3, 4, 9, 8, 15, 12, 21]
Processed Strings: apple BANANA kiwi GRAPEFRUIT CHERRY
```
