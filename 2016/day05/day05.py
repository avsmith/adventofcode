#!/usr/bin/env python

import hashlib

# Original solution for part 1.
# Basis for solution for both
# parts concurrently.
def find_password(word):
    num = 1
    password = ""
    while len(password) < 8:
        string = word + str(num)
        md5string = hashlib.md5(string.encode()).hexdigest()
        if md5string[0:5] == "00000":
            password += md5string[5]
        num += 1
    return password


def find_passwords(word):
    num = 1
    pass1 = ""
    pass2 = "--------"

    # Only need to check 2nd password condition.
    # First will certainly already be completed.
    while "-" in pass2:
        string = word + str(num)
        md5string = hashlib.md5(string.encode()).hexdigest()
        if md5string[0:5] == "00000":
            if len(pass1) < 8:
                pass1 += md5string[5]
            if md5string[5] in "01234567":
                idx = int(md5string[5])
                if pass2[idx] == "-":
                    pass2 = pass2[:idx] + md5string[6] + pass2[idx + 1 :]
        num += 1
    return pass1, pass2


results = find_passwords("wtnhxymk")

print("Part 1:", results[0])
print("Part 2:", results[1])
