import pytest
from core.blocks.base_block import BaseBlock

class DummyBlock(BaseBlock):
    def to_code(self):
        return f"# code for {self.name}"

def test_base_block_initialization():
    b = DummyBlock(name="test", foo=42)
    assert b.name == "test"
    assert b.params["foo"] == 42

def test_to_code():
    b = DummyBlock(name="layer1")
    code = b.to_code()
    assert "layer1" in code