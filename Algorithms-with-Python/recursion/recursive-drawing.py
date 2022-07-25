def recursive_symbols(n):
    if n == 0:
        return

    print('*' * n)  # pre-action
    recursive_symbols(n - 1)  # recursive call
    print('#' * n)  # post-action


n = int(input())

recursive_symbols(n)