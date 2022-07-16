"""
File:    spider_web.py
Author:  Antionne Andries
Date:    11/24/2021
Section: 36
E-mail:  a345@umbc.edu
Description: DESCRIPTION OF WHAT THE PROGRAM DOES
"""
import random


def spider_web(web_map, starting_place, destination):
    visited = []
    path = spider_web_rec(web_map, starting_place, destination, visited)

    if path:
        return "Found a path: " + str(path)
    else:
        return "No path found"


def spider_web_rec(web_map, starting_place, destination, visited):
    if destination == starting_place:
        base = [destination]
        return base
    else:
        for node in visited:
            if starting_place == node:
                return None
        visited.append(starting_place)
        for node in web_map.get(starting_place):
            if node not in visited:
                path = spider_web_rec(web_map, node, destination, visited)
                final_list = [starting_place]
                final_list += path
                return final_list


def make_spider_web(num_nodes, seed=0):
    if seed:
        random.seed(seed)

    web_map = {}

    for i in range(1, num_nodes + 1):
        web_map[f'Node {i}'] = []

    for i in range(1, num_nodes + 1):
        sample = random.sample(list(range(i, num_nodes + 1)), random.randint(1, num_nodes - i + 1))
        for x in sample:
            if i != x:
                web_map[f'Node {i}'].append(f'Node {x}')
                web_map[f'Node {x}'].append(f'Node {i}')
    return web_map


if __name__ == '__main__':
    num_nodes, seed = [int(x) for x in input('Input num_nodes, seed: ').split(',')]
    the_web = make_spider_web(num_nodes, seed)
    print(spider_web(the_web, 'Node 1', f'Node {num_nodes}'))

