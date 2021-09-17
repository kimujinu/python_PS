import sys

S = sys.stdin.readline().replace("<", ">").split(">")
for i, s in enumerate(S):
    if s == "":
        continue
    if i % 2:
        print(f"<{s}>", end="")
    else:
        print(" ".join(w[::-1] for w in s.split()), end="")
print()
