def missionaries_and_cannibals(l_m, l_c, r_m, r_c):
  """
  Solves the missionaries and cannibals problem using a recursive backtracking algorithm.

  Args:
    l_m: The number of missionaries on the left bank.
    l_c: The number of cannibals on the left bank.
    r_m: The number of missionaries on the right bank.
    r_c: The number of cannibals on the right bank.

  Returns:
    True if the problem is solved, False otherwise.
  """

  print("Left Bank:", l_m, l_c, "Right Bank:", r_m, r_c)

  if (l_m == 0 and l_c == 0):
    return True

  # Check if the current state is unsafe.

  if (l_c > l_m):
    return False

  # Try moving 2 missionaries and 1 cannibal to the right bank.

  if (l_m >= 2 and l_c >= 1):
    print("Move 2 m and 1 c to the right bank.")
    if missionaries_and_cannibals(l_m - 2, l_c - 1, r_m + 2, r_c):
      return True

  # Try moving 1 missionary and 1 cannibal to the right bank.

  if (l_m >= 1 and l_c >= 1):
    print("Move 1 m and 1 c to the right bank.")
    if missionaries_and_cannibals(l_m - 1, l_c - 1, r_m + 1, r_c):
      return True

  # Try moving 2 cannibals to the right bank.

  if (l_c >= 2):
    print("Move 2 c to the right bank.")
    if missionaries_and_cannibals(l_m, l_c - 2, r_m, r_c + 2):
      return True

  return False


def main():
  """
  Solves the missionaries and cannibals problem.
  """

  l_m = 3
  l_c = 3
  r_m = 0
  r_c = 0

  if missionaries_and_cannibals(l_m, l_c, r_m, r_c):
    print("The problem is solved.")
  else:
    print("The problem cannot be solved.")


if __name__ == "__main__":
  main()
