import random
import string

from typing import Final, List, TypeVar

# Declare type variable "T"
T = TypeVar("T")


def generate_integer(min_val: int, max_val: int) -> int:
    """Make a random integer in [min_val, max_val].

    Params:
        min_val (int):
            Minimum value (inclusive).
        max_val (int):
            Maximum value (inclusive).
    """
    assert min_val <= max_val
    return random.randrange(min_val, max_val + 1)


def generate_alphabet(min_val: str = "A", max_val: str = "z") -> str:
    """Make a single English alphabet in [min_val, max_val].

    Params:
        min_val (str):
            A single character indicating the minimum.
        max_val (str):
            A single character indicating the maximum.
    """
    assert 1 == len(min_val)
    assert 1 == len(max_val)

    # List of all English alphabets in the range.
    filtered_letters: Final[List[str]] = list(
        filter(lambda x: min_val <= x <= max_val, string.ascii_letters)
    )

    # It should be non-empty.
    assert filtered_letters

    return random.choice(filtered_letters)


def generate_string(n: int, letters: str = "", blank: bool = False) -> str:
    """Make a string of length n with given letters.

    Params:
        n (int):
            The exact length of the string to make.
        letters (str):
            List of readable characters to use.
            If empty, then use the default value; alphanumeric.
        blank (str):
            Allow the in-between space character ' '.
    """
    if not letters:
        letters = string.ascii_letters + string.digits

    if n == 0:
        return ""
    elif n == 1:
        return random.choice(letters)
    elif n == 2:
        return random.choice(letters) + random.choice(letters)

    if blank:
        # TODO(youngyojun): It seems that consecutive spaces are allowed.
        return (
            random.choice(letters)
            + "".join(random.choice(letters + " ") for _ in range(n - 2))
            + random.choice(letters)
        )
    else:
        return "".join(random.choice(letters) for _ in range(n))


def generate_word(n: int, min_val: str = "A", max_val: str = "z") -> str:
    """Make a word using English alphabets in [min_val, max_val].

    Params:
        n (int):
            The length of the word.
        min_val (str):
            A single character indicating the minimum.
        max_val (str):
            A single character indicating the maximum.
    """
    assert 0 <= n
    return "".join(generate_alphabet(min_val, max_val) for _ in range(n))


def generate_array(n: int, min_val: int, max_val: int) -> List[int]:
    """Make an integer array of length n where every element is in [min_val, max_val].

    Params:
        n (int):
            The length of the array.
        min_val (int):
            Minimum value of the element.
        max_val (int):
            Maximum value of the element.
    """
    return [generate_integer(min_val, max_val) for _ in range(n)]


def generate_2d_array(
    n: int, m: int, min_val: int, max_val: int
) -> List[List[int]]:
    """Make a 'n by m' two-dimensional array using integers in [min_val, max_val].

    Params:
        n (int):
            The length of the first axis.
        m (int):
            The length of the second axis.
        min_val (int):
            Minimum value of the element.
        max_val (int):
            Maximum value of the element.
    """
    return [generate_array(m, min_val, max_val) for _ in range(n)]


def generate_unique_array(n: int, min_val: int, max_val: int) -> List[int]:
    """Make an array of n distinct integers in [min_val, max_val].

    Params:
        n (int):
            The length of the array.
        min_val (int):
            Minimum value of the element.
        max_val (int):
            Maximum value of the element.
    """
    assert 0 <= n
    # The set [min_val, max_val] must have enough integers.
    assert n <= max_val - min_val + 1
    return random.sample(range(min_val, max_val + 1), n)


def generate_subseq(arr: List[T], n: int) -> List[T]:
    """Make a subsequence of the array, whose length is n.

    Params:
        arr (List[T]):
            A base array.
        n (int):
            The length of the subsequence.
    """
    assert 0 <= n
    assert n <= len(arr)
    # Indices of the element for the subsequence.
    indices: Final[List[int]] = sorted(generate_array(n, 0, len(arr) - 1))
    return [arr[i] for i in indices]
