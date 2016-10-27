from ch3_stacks_and_queues import Queue


def contains_path_DFS(graph, node1, node2):
    # {
    # 1: [2, 3]
    # 2: [3]
    # 3: [1]
    # }

    def contains_directional_path_DFS(start, end, visited):
        if start == end:
            return True
        else:
            for node in graph[start]:
                if node not in visited:
                    visited.add(node)
                    if contains_directional_path_DFS(node, end, visited):
                        return True
            return False

    return contains_directional_path_DFS(node1, node2, set()) \
           or contains_directional_path_DFS(node2, node1, set())


def contains_path_BFS(graph, node1, node2):
    def contains_directional_path_BFS(start, end):
        visited = set()
        search_queue = Queue()
        search_queue.enqueue(start)
        while not search_queue.is_empty():
            node = search_queue.dequeue()
            visited.add(node)
            if node == end:
                return True
            else:
                for adj in graph[node]:
                    if adj not in visited:
                        search_queue.enqueue(adj)
        return False

    return contains_directional_path_BFS(node1, node2) \
           or contains_directional_path_BFS(node2, node1)


class BinaryNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other or type(other) != BinaryNode:
            return False
        else:
            return self.data == other.data and self.left == other.left and self.right == other.right

    def __repr__(self):
        return str(self.data)


def create_minimal_depth_tree(lst):
    def _create_minimal_depth_tree(i, j):
        if j - i == 0:
            return None
        elif j - i == 1:
            return BinaryNode(lst[i])
        else:
            mid_idx = (j - i) / 2 + i
            mid = lst[mid_idx]
            return BinaryNode(mid, _create_minimal_depth_tree(i, mid_idx),
                              _create_minimal_depth_tree(mid_idx + 1, j))

    return _create_minimal_depth_tree(0, len(lst))


def lst_of_depths_BFS(tree):
    search_queue = Queue()
    end_token = 134523
    search_queue.enqueue(tree)
    search_queue.enqueue(end_token)
    res = [[]]
    while not search_queue.is_empty():
        tree_item = search_queue.dequeue()
        if end_token != tree_item:
            res[-1].append(tree_item.data)
            if tree_item.left:
                search_queue.enqueue(tree_item.left)
            if tree_item.right:
                search_queue.enqueue(tree_item.right)
        elif not search_queue.is_empty():
            res.append([])
            search_queue.enqueue(end_token)
    return res


def check_balanced(tree):
    def get_or_check_height(node):
        # if tree unbalanced, return -1, else return height of tree
        if not node:
            return 0
        left = get_or_check_height(node.left)
        right = get_or_check_height(node.right)
        diff = left - right
        diff = diff if diff >= 0 else diff * -1
        if left == -1 or right == -1:
            return -1
        elif diff > 2:
            return -1
        else:
            return max(left, right) + 1

    return get_or_check_height(tree) != -1


def validate_BST(node):
    if not node:
        return True
    if node.left and node.left.data >= node.data:
        return False
    if node.right and node.right.data <= node.data:
        return False
    return validate_BST(node.left) and validate_BST(node.right)


def successor(tree, item):
    prevs = []
    cur = tree
    while cur and item != cur.data:
        prevs.append(cur)
        if cur.data < item:
            cur = cur.right
        elif cur.data > item:
            cur = cur.left

    # find successor
    if cur.right:
        cur = cur.right
    else:
        prevs.append(cur)
        for i in range(len(prevs) - 1, 0, -1):
            if prevs[i] == prevs[i - 1].left:
                return prevs[i - 1].data
        return None
    while cur.left:
        cur = cur.left
    return cur.data


def build_order(projects, dependencies):
    dependencies = dependencies[:]
    if len(projects) == 1 or len(projects) == 0:
        return projects
    build_order = list(set(projects) - set([j for _, j in dependencies]))
    if not build_order:
        raise Exception("No possible order")
    prev_size = None
    cur_size = len(dependencies)
    while dependencies and prev_size != cur_size:
        potential_projs = set()
        for i in range(len(dependencies) - 1, -1, -1):
            if dependencies[i][0] in build_order:
                potential_projs.add(dependencies.pop(i)[1])
        new_projs = list(potential_projs - set([j for _, j in dependencies]))
        build_order.extend(new_projs)
        prev_size = cur_size
        cur_size = len(dependencies)
    if not dependencies:
        return build_order
    else:
        raise Exception("No possible order")


def build_order_DFS(projects, dependencies):
    dependencies = dependencies[:]
    projects = projects[:]
    res = []

    def dfs_add_projs(node, visited):
        if node in visited:
            raise Exception("No possible order")
        elif node in res:
            return
        else:
            visited.add(node)
            outgoing_edges = []
            for k in range(len(dependencies) - 1, -1, -1):
                i, j = dependencies[k]
                if i == node:
                    outgoing_edges.append(j)
                    dependencies.pop(k)
            res.append(node)
            for outgoing_edge in outgoing_edges:
                dfs_add_projs(outgoing_edge, visited)

    while projects:
        node = projects.pop()
        dfs_add_projs(node, set())
    res.reverse()
    return res


def first_common_ancestor(item1, item2, tree):
    def get_item_path(node, item, path):
        if not node:
            return False
        elif node == item:
            path.append(node)
            return True
        else:
            path.append(node)
            found_in_left = get_item_path(node.left, item, path)
            found_in_right = get_item_path(node.right, item, path)
            if not found_in_left and not found_in_right:
                path.pop()
                return False
            else:
                return True

    path1 = []
    is_item1_found = get_item_path(tree, item1, path1)
    path2 = []
    is_item2_found = get_item_path(tree, item2, path2)

    if not is_item1_found or not is_item2_found:
        return None
    elif len(path1) > len(path2):
        path1 = path1[:len(path2)]
    else:
        path2 = path2[:len(path1)]

    prev = None
    for i in range(len(path1)):
        if path1[i] != path2[i]:
            return prev
        prev = path1[i]
    # if it's in ancestry path
    return path1[-1]


def BST_sequences(tree):
    def sequential_merges(lst1, lst2, merged_lst=[]):
        res = []
        if not lst1 and not lst2:
            return [merged_lst]
        if lst1:
            res.extend(sequential_merges(lst1[:-1], lst2, [lst1[-1]] + merged_lst))
        if lst2:
            res.extend(sequential_merges(lst1, lst2[:-1], [lst2[-1]] + merged_lst))
        return res

    if not tree:
        return [[]]
    left_sequences = BST_sequences(tree.left)
    right_sequences = BST_sequences(tree.right)
    res = []
    for left_sequence in left_sequences:
        for right_sequence in right_sequences:
            sequences = sequential_merges(left_sequence, right_sequence)
            for sequence in sequences:
                sequence.insert(0, tree.data)
            res.extend(sequences)
    return res


def is_subtree(tree_1, tree_2):
    if tree_1:
        return tree_1 == tree_2 or is_subtree(tree_1.left, tree_2) or is_subtree(tree_1.right, tree_2)
    else:
        return False


from random import randint


class BSTRand(BinaryNode):
    def __init__(self, data, parent=None):
        BinaryNode.__init__(self, data)
        self.size = 1
        self.parent = parent

    def insert(self, data):
        cur = self
        prev = None
        while cur:
            prev = cur
            cur.size += 1
            if data <= cur.data:
                cur = cur.left
            else:
                cur = cur.right

        insert_node_parent = prev
        if data <= insert_node_parent.data:
            insert_node_parent.left = BSTRand(data, insert_node_parent)
        else:
            insert_node_parent.right = BSTRand(data, insert_node_parent)

    def find(self, data):
        cur = self
        if cur.data == data:
            return self
        while cur:
            if data < cur.data:
                cur = cur.left
            else:
                cur = cur.right

            if cur and cur.data == data:
                return cur
        return None

    def delete(self, data_or_node):
        if self.size == 1:
            raise IndexError("Can not delete the only node")
        node = data_or_node if type(data_or_node) == BSTRand else self.find(data_or_node)
        cur = None

        def decrement_ancestor_counts(node):
            cur = node
            while cur:
                cur.size -= 1
                cur = cur.parent

        if not node:
            return False

        elif not node.right:
            if node.parent and node.parent.left and id(node.parent.left) == id(node):
                if node.left:
                    node.left.parent = node.parent
                if node.parent:
                    node.parent.left = node.left

            elif node.parent and node.parent.right and id(node.parent.right) == id(node):
                if node.left:
                    node.left.parent = node.parent
                if node.parent:
                    node.parent.right = node.left
            decrement_ancestor_counts(node)

        else:
            cur = node.right
            if not cur.left:
                cur.parent.data = cur.data
                cur.parent.right = cur.right
                if cur.right:
                    cur.right.parent = cur.parent

            else:
                while cur.left:
                    cur = cur.left
                if cur.parent:
                    cur.parent.left = cur.right
                if cur.right:
                    cur.right.parent = cur.parent

                node.data = cur.data
            decrement_ancestor_counts(cur.parent)
        return True

    def get_random_node(self, nth_in_order=None):

        if nth_in_order is None:
            nth_in_order = randint(1, self.size)

        left_size = 0 if not self.left else self.left.size

        # left is empty
        if nth_in_order == left_size + 1:
            return self.data

        elif nth_in_order <= left_size:
            return self.left.get_random_node(nth_in_order)

        else:
            return self.right.get_random_node(nth_in_order - left_size - 1)


def count_paths_sum_to_num_top_bottom(node, num):
    if not node:
        return 0

    def inclusive_count(node, num):
        if not node:
            return 0

        # include itself
        left_inclusive = inclusive_count(node.left, num - node.data)
        right_inclusive = inclusive_count(node.right, num - node.data)
        total_inclusive = 1 if num == node.data else 0
        total_inclusive += left_inclusive + right_inclusive
        return total_inclusive

    # does include itself as start
    inclusive_node_count = inclusive_count(node, num)

    # does not include itself as start
    left_count_noninclusive = count_paths_sum_to_num_top_bottom(node.left, num)
    right_count_noninclusive = count_paths_sum_to_num_top_bottom(node.right, num)

    return inclusive_node_count + left_count_noninclusive + right_count_noninclusive


def count_paths_sum_to_num_bottom_top(tree, num):
    def _count_paths_sum_to_num_bottom_top(node, num, path):
        if not node:
            return 0

        # does include itself as start
        aggregate = node.data
        inclusive_node_count = 0 if aggregate != num else 1
        for i in range(len(path) - 1, -1, -1):
            aggregate += path[i]
            if aggregate == num:
                inclusive_node_count += 1

        # does not include itself as start
        path.append(node.data)
        left_count_noninclusive = _count_paths_sum_to_num_bottom_top(node.left, num, path)
        right_count_noninclusive = _count_paths_sum_to_num_bottom_top(node.right, num, path)
        path.pop()

        return inclusive_node_count + left_count_noninclusive + right_count_noninclusive

    ancestors = []
    return _count_paths_sum_to_num_bottom_top(tree, num, ancestors)


def count_paths_sum_to_num_DP(tree, num):
    def _count_paths_sum_to_num_DP(node, num, aggregate_from_root, aggregates_so_far):
        if not node:
            return 0

        aggregate_from_root += node.data
        aggregates_so_far.setdefault(aggregate_from_root, 0)
        aggregates_so_far[aggregate_from_root] += 1

        key = aggregate_from_root - num
        inclusive_count = 0 if key not in aggregates_so_far else aggregates_so_far[key]

        left_count = _count_paths_sum_to_num_DP(node.left, num, aggregate_from_root, aggregates_so_far)
        right_count = _count_paths_sum_to_num_DP(node.right, num, aggregate_from_root, aggregates_so_far)

        aggregates_so_far[aggregate_from_root] -= 1
        if aggregates_so_far[aggregate_from_root] == 0:
            del aggregates_so_far[aggregate_from_root]

        return inclusive_count + left_count + right_count

    # occurrence of aggregate in the very beginning is one
    aggregates_so_far = {0: 1}
    return _count_paths_sum_to_num_DP(tree, num, 0, aggregates_so_far)
