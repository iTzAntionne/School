def permutations(string):
    if len(string) == 1:
        return string

    recursive_perms = []
    for c in string:
        for perm in permutations(string.replace(c, '', 1)):
            recursive_perms.append(c+perm)

    return set(recursive_perms)


if __name__ == "__main__":
    print(permutations("aabb"))
