from typing import List, Dict, Any
from utils.logger import setup_logger

logger = setup_logger(__name__)

class Node:
    def __init__(self, block_id: str, block):
        self.id = block_id
        self.block = block
        self.outputs: List['Node'] = []
        self.inputs: List['Node'] = []
        logger.debug(f"Graph Node created: {self.id}")

class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        logger.info("Initialized empty graph")

    def add_node(self, node: Node):
        if node.id in self.nodes:
            logger.warning(f"Node {node.id} already exists; skipping")
            return
        self.nodes[node.id] = node
        logger.debug(f"Added node {node.id}")

    def connect(self, src_id: str, dest_id: str):
        src = self.nodes[src_id]
        dest = self.nodes[dest_id]
        src.outputs.append(dest)
        dest.inputs.append(src)
        logger.debug(f"Connected {src_id} → {dest_id}")