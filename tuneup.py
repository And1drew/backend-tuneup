#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Andrew Belanger with demo video"

import timeit
import cProfile
import pstats
import functools


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()

        result = func(*args, **kwargs)
        profiler.disable()
        ps = pstats.Stats(profiler).strip_dirs().sort_stats("cumulative")
        ps.print_stats(10)
        return result

    return inner


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies.sort()
    duplicates = [m1 for m1, m2 in zip(movies[1:], movies[:-1]) if m1 == m2]
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    timer = timeit.Timer(
        stmt="find duplicate_movies('movie.txt')",
        setup='from__main__ import find_duplicate_movies'
        )
    runs_per_repeat = 50
    num_repeats = 100
    result = timer.repeat(repeat=num_repeats, number=runs_per_repeat)
    best_time = min(result) / float(runs_per_repeat)
    print("best time  {}, repeat {} runs per repeat: {} sec".format(
        num_repeats, best_time
        ))


def main():
    """Computes a list of duplicate movie entries"""

    result = find_duplicate_movies('./movies.txt')
    # timeit_helper()

    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
