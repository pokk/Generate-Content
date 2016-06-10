""" Created by Jieyi on 4/28/16. """

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import networkx as nx

from nature_language import test_text
from nature_language.text_analysis import AnalysisWord
from nature_language.word_node import WordNode


class MarkovGraph:
    def __init__(self):
        # the structure of graph set is {(word, pos): [WordNode, WordNode], (word, pos): [WordNode], ...}.
        self._graph_set_detail = {}
        # the structure of graph set is a normal graph set. ex: {word: [word, word, word], word: [word], ...}.
        self._graph_set = {}
        self._node_set = {}
        self._edge_set = {}
        self._graph = nx.DiGraph()  # this is direct graph.

    def __str__(self):
        pass

    def add_pos_to_graph(self, content_with_pos):
        if not content_with_pos:
            return False

        prev_node = None

        for w, t in content_with_pos[:30]:
            print(w, t)
            current = WordNode(w, t)
            self.add_to_graph(prev_node, current)
            prev_node = current

        return True

    def add_to_graph(self, prev_node, curr_node):
        """
        Add the current word into graph.

        :param prev_node: the previous word node.
        :param curr_node: the current word node.
        """

        if not prev_node:
            self._add_to_graph_dict(prev_node, curr_node)
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
        for w in self._graph_set_detail:
            for v in self._graph_set_detail[w]:
                # v is WordNode.
                if v:
                    self._graph.add_edge(w[0], v.word)

        # it can change to un-direct graph.
        # self._graph = self._graph.to_undirected()

        # Positions for all nodes.
        pos = nx.spring_layout(self._graph)
        nx.draw_networkx_nodes(self._graph, pos, node_size=700, node_color="white")
        nx.draw_networkx_edges(self._graph, pos, width=1, alpha=0.5, edge_color='black')
        nx.draw_networkx_labels(self._graph, pos, font_size=10, font_family='monospace')

        plt.axis('off')
        plt.show()  # Display

    def _add_to_graph_dict(self, prev_node, curr_node):
        """
        Add a node into graph set.

        :param prev_node: the previous word node.
        :param curr_node: the current word node.
        :return: true: insert success, false: it's already in the dictionary.
        """

        tuple_of_prev_node, tuple_of_curr_node = self._tuple_of_node(prev_node), self._tuple_of_node(curr_node)

        # the previous hasn't existed in the dictionary.
        if not self._graph_set_detail.get(tuple_of_prev_node):
            # create a children list of current node.
            self._graph_set_detail[tuple_of_prev_node] = [curr_node]
        else:
            # the child has already appeared before.
            for n in self._graph_set_detail[tuple_of_prev_node]:
                if tuple_of_curr_node == self._tuple_of_node(n):
                    # we have to add 1 time to count variable.
                    n.add_count()
                    return False
            else:
                self._graph_set_detail[tuple_of_prev_node].append(curr_node)

        return True

    def _add_to_node_dict(self, node):
        """
        Add a node to dictionary.

        :param node: a class including word and tag
        :return: true: success, false: insert fail
        """

        tuple_of_node = self._tuple_of_node(node)

        if not self._node_set.get(tuple_of_node):
            self._node_set[tuple_of_node] = node
            return True
        return False

    def _transform(self):
        for s in self._graph_set_detail:
            self._graph_set[s[0]] = []
            for n in self._graph_set_detail[s]:
                self._graph_set[s[0]].append(n.word)
                # for s in self._graph_set:
                #     print(s, end=' -> ')
                #     for n in self._graph_set[s]:
                #         print("'" + n + "'", end=',')
                #     print()

    def _dfs(self, graph, start):
        visited, stack = [], [start, ]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                print(vertex)
                visited.append(vertex)
                # stack.extend(graph[vertex] - visited)
                print(graph[vertex])
                l = [x for x in graph[vertex] if x not in visited]
                print(l)
                stack.extend(l)

        print(visited)
        return visited

    @staticmethod
    def _tuple_of_node(node):
        """
        Create a tuple set of the word node.

        :param node: the current word node.
        :return: None: input a null parameter; otherwise, a tuple of the word and the pos.
        """

        if not node:
            return None, None
        return node.word, node.pos

    @property
    def graph_set_detail(self):
        return self._graph_set_detail


def main():
    a = AnalysisWord(test_text)  # build-in sentence.
    # getter = HTMLContentGetter("https://en.wikipedia.org/wiki/Marvel_Comics")
    # a = AnalysisWord(getter.obtain_content(WikiArticleParser()))
    a.analysis()
    l = a.pos_tag()
    m = MarkovGraph()
    m.add_pos_to_graph(l)

    for s in m.graph_set_detail:
        print(s, end=',     \t')
        for n in m.graph_set_detail[s]:
            print(n, end=',  ')
        print()

        # m.draw_graph()
    m._transform()
    m._dfs(m._graph_set, None)


if __name__ == '__main__':
    main()
