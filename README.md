# WordCounterPro
This project is an early version of a Python program that counts the lengths of words in a text file. It reflects the initial learning phase of Python and showcases creativity in solving problems with lists and functions.
---
## Overview
The program:
1. Prompts the user to input a file name.
2. Reads the content of the file.
3. Counts the frequency of words based on their lengths.
4. Outputs the results for each word length.
---
## Features
- **Dynamic Longest Word Detection**: Finds the longest word in the file and uses its length as the maximum range for counting.
- **Word Length Tally**: Counts the number of words for each length.
- **File Creation**: If the specified file does not exist, it creates an empty file.
---
## Limitations
- **Punctuation Handling**: Punctuation is not stripped from words, which may affect word length calculations.
- **Case Sensitivity**: The program does not normalize words to lowercase, leading to case-sensitive differences.
- **Error Handling**: While basic error handling is included (e.g., for non-existent files), it could be more robust.
- **Code Style**: The code reflects a beginner's learning journey and could benefit from optimization.
---
## Example Usage
### Input
A text file named `example.txt` with the following content:
Hello world! Python is fun. Isn’t it?
### Output
There are 1 1-letter words in example.txt
There are 2 2-letter words in example.txt
There are 2 3-letter words in example.txt
There are 2 4-letter words in example.txt
There are 1 5-letter words in example.txt
There are 1 6-letter words in example.txt
---
## Personal Notes
This project represents a milestone in learning Python, focusing on:
- Building confidence with file handling.
- Experimenting with word counting logic.
- Preparing for future improvements and optimizations.
---
## Future Plans
This project will serve as a historical record for my programming journey. A more optimized version has already been created, but this version will remain for sentimental value and reflection.
---
## How to Run
1. Save the original code into a file, e.g., `word_counter.py`.
2. Ensure you have a text file to test with (or let the program create one for you).
3. Run the program in a terminal or Python environment:
  ```bash
  python word_counter.py
4. Follow the on-screen prompts to input the file name and view the word length counts.
Lessons Learned
• Iterative Development: Starting with a basic version of the code helped build confidence and allowed for incremental improvements.
• Value of History: This code will remain unoptimized as a record of growth and as a source of inspiration for future work.
