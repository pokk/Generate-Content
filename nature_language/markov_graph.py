""" Created by Jieyi on 4/28/16. """

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx

from nature_language import markov_text
from nature_language.text_analysis import AnalysisWord
from nature_language.word_node import WordNode


class MarkovGraph:
    def __init__(self):
        self._graph_set = {}
        self._node_set = {}
        self._edge_set = {}
        self._graph = nx.DiGraph()

    def __str__(self):
        pass

    def add_to_graph(self, prev_node, curr_node):
        """
        Add the current word into graph.

        :param prev_node: the previous word node.
        :param curr_node: the current word node.
        """

        if not prev_node:
            self._add_to_graph_dict(curr_node, None)
            return False
        else:
            self._add_to_node_dict(prev_node)
            self._add_to_node_dict(curr_node)
            self._add_to_graph_dict(prev_node, curr_node)

    def draw_graph(self):
        """
        Draw the graph.
        """

        # Add the connection status.
        for w in self._graph_set:
            for v in self._graph_set[w]:
                if v:
                    self._graph.add_edge(w[0], v[0])

        # Positions for all nodes.
        pos = nx.spring_layout(self._graph)
        nx.draw_networkx_nodes(self._graph, pos, node_size=700, node_color="white")
        nx.draw_networkx_edges(self._graph, pos, width=2, alpha=0.5, edge_color='black')
        nx.draw_networkx_labels(self._graph, pos, font_size=15, font_family='monospace')

        plt.axis('off')
        plt.show()  # Display

    def _add_to_graph_dict(self, prev_node, curr_node):
        """
        Add a node into graph set.

        :param prev_node: the previous word node.
        :param curr_node: the current word node.
        :return: true: insert success, false: it's already in the dictionary.
        """

        if not self._graph_set.get(self._tuple_of_node(prev_node)):
            self._graph_set[self._tuple_of_node(prev_node)] = [self._tuple_of_node(curr_node)]
        else:
            if self._tuple_of_node(curr_node) in self._graph_set[self._tuple_of_node(prev_node)]:
                return False
            else:
                self._graph_set[self._tuple_of_node(prev_node)].append(self._tuple_of_node(curr_node))
        return True

    def _add_to_node_dict(self, node):
        """
        Add a node to dictionary.

        :param node: a class including word and tag
        :return: true: success, false: insert fail
        """

        if not self._node_set.get(self._tuple_of_node(node)):
            self._node_set[self._tuple_of_node(node)] = node
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
        """
        Create a tuple set of the word node.

        :param node: the current word node.
        :return: None: input a null parameter; otherwise, a tuple of the word and the pos.
        """

        if not node:
            return None
        return node.word, node.pos


def main():
    a = AnalysisWord(markov_text)
    a.analysis()
    l = a.pos_tag()
    m = MarkovGraph()
    prev_node = None

    for w, t in l[:10]:
        current = WordNode(w, t)
        m.add_to_graph(prev_node, current)
        prev_node = current

    m.draw_graph()


if __name__ == '__main__':
    main()
