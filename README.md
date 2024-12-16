# Unclosed File Bug
This repository demonstrates a common error in Python programming: failing to close files properly.  Improperly closing files can lead to various issues, including resource exhaustion, data loss, and corrupted files. The `bug.py` file contains the buggy code, while the solution is provided in `bugSolution.py`.

## Bug Description
The `function_with_unclosed_file` function opens a file for writing. However, if an exception occurs within the function before reaching the `f.close()` statement, the file remains open, potentially leading to problems.

## Solution
The solution utilizes a `try...finally` block to guarantee that the file is closed, regardless of whether exceptions occur.