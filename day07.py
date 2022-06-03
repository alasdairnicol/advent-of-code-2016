#!/usr/bin/env python
import itertools
import hashlib
from typing import Generator
from collections import Counter


def contains_abba(word):
    for i in range(len(word) - 3):
        if all(
            [
                word[i] == word[i + 3],
                word[i + 1] == word[i + 2],
                word[i] != word[i + 1],
            ]
        ):
            return True
    return False


def supports_tls(ip):
    words = ip.replace("]", "[").split("[")
    sequences = words[0::2]
    hypernets = words[1::2]
    return any(contains_abba(s) for s in sequences) and not any(
        contains_abba(s) for s in hypernets
    )


def abas_in_word(word):
    abas = []
    for i in range(len(word) - 2):
        if word[i] == word[i + 2] and word[i] != word[i + 1]:
            abas.append(word[i : i + 3])
    return abas


def babs_in_word(word):
    return [f"{x[1]}{x[0]}{x[1]}" for x in abas_in_word(word)]


def supports_ssl(ip):
    words = ip.replace("]", "[").split("[")
    sequences = words[0::2]
    hypernets = words[1::2]
    nested_abas = [abas_in_word(word) for word in sequences]
    abas = {aba for abas in nested_abas for aba in abas}
    nested_babs = [babs_in_word(word) for word in hypernets]
    babs = {bab for babs in nested_babs for bab in babs}
    return bool(abas & babs)


def main():
    ips = list(read_input())

    part_a = len([ip for ip in ips if supports_tls(ip)])
    part_b = len([ip for ip in ips if supports_ssl(ip)])

    print(f"{part_a=}")
    print(f"{part_b=}")


def read_input() -> Generator[str, None, None]:
    with open("day07.txt") as f:
        return (line.strip() for line in f.readlines())


if __name__ == "__main__":
    main()
