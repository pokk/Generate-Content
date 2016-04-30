""" Created by Jieyi on 4/28/16. """

# -*- coding: utf-8 -*-
from nature_language import markov_text
from nature_language.text_analysis import AnalysisWord
from nature_language.word_node import WordNode


class MarkovGraph:
    def __init__(self):
        self._graph = {}
        self._node = {}

    def __str__(self):
        pass

    def add_to_graph(self, prev_node, curr_node):
        if not prev_node:
            self._add_to_graph_dict(curr_node, None)
            return False
        else:
            self._add_to_node_dict(prev_node)
            self._add_to_node_dict(curr_node)
            self._add_to_graph_dict(prev_node, curr_node)

    def _add_to_graph_dict(self, prev_node, curr_node):
        if not self._graph.get(self._tuple_of_node(prev_node)):
            self._graph[self._tuple_of_node(prev_node)] = [self._tuple_of_node(curr_node)]
        else:
            if self._tuple_of_node(curr_node) in self._graph[self._tuple_of_node(prev_node)]:
                return False
            else:
                self._graph[self._tuple_of_node(prev_node)].append(self._tuple_of_node(curr_node))
        return True

    def _add_to_node_dict(self, node):
        if not self._node.get(self._tuple_of_node(node)):
            self._node[self._tuple_of_node(node)] = node
            return True
        return False

    def __dfs(self, graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                stack.extend(graph[vertex] - visited)
        return visited

    @staticmethod
    def _tuple_of_node(node):
        if not node:
            return None
        return node.word, node.pos


def main():
    a = AnalysisWord(markov_text)
    a.analysis()
    l = a.pos_tag()
    m = MarkovGraph()
    prev_node = None

    for w, t in l[:30]:
        current = WordNode(w, t)
        m.add_to_graph(prev_node, current)
        prev_node = current

    print(m._graph)


if __name__ == '__main__':
    main()
