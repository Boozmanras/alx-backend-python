# Python Async Function Project

This project explores asynchronous programming in Python, focusing on coroutines, tasks, and measuring execution time of asynchronous operations.

## Project Overview

The project consists of several Python scripts that demonstrate various aspects of asynchronous programming:

1. `0-basic_async_syntax.py`: Implements a basic asynchronous coroutine.
2. `1-concurrent_coroutines.py`: Demonstrates running multiple coroutines concurrently.
3. `2-measure_runtime.py`: Measures the runtime of asynchronous operations.
4. `3-tasks.py`: Shows how to create asyncio Tasks.
5. `4-tasks.py`: Modifies the concurrent coroutines to use Tasks.

## Requirements

- Python 3.7+
- Ubuntu 18.04 LTS
- pycodestyle 2.5.x

## Files Description

- `0-basic_async_syntax.py`: Contains `wait_random` coroutine that waits for a random delay.
- `1-concurrent_coroutines.py`: Implements `wait_n` function to spawn `wait_random` n times.
- `2-measure_runtime.py`: Includes `measure_time` function to calculate average runtime of `wait_n`.
- `3-tasks.py`: Defines `task_wait_random` function to create an asyncio.Task.
- `4-tasks.py`: Modifies `wait_n` to `task_wait_n` using the task version of `wait_random`.

## Usage

Each file can be run independently. For example:

```bash
./0-main.py
./1-main.py
./2-main.py
./3-main.py
./4-main.py
```

## Learning Objectives

- Understanding asyncio in Python
- Writing asynchronous coroutines
- Running concurrent coroutines
- Creating asyncio Tasks
- Using the random module in an asynchronous context
- Measuring the execution time of asynchronous programs

## Author

<Victor paul>

## License

This project is part of short alx backend software engineering specialisation
