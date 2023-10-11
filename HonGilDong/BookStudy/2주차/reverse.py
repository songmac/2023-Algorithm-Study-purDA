from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
  n = len(a)
  for i in range(n // 2):
    a[i]. a[n-i-1] = a[n-i-1], a[i]
