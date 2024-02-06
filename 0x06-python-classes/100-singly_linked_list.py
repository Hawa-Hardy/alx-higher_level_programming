#!/usr/bin/python3
"""Definition of classes for a singly-linked list."""


class Node:
    """Represents node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """New Node Initilizer

        Args:
            data (int): New Node's data.
            next_node (Node): Next following node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets and sets the data of the node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets and sets the next_node func of sl Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Definition of a singly-linked list."""

    def __init__(self):
        """Initializer for SinglyLinkedList class."""
        self.__head = None

    def sorted_insert(self, value):
        """Adds a new Node to the SinglyLinkedList.

        Args:
            value (Node): Node to be inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Print() of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
