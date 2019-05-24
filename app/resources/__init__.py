from .example import ns as example_ns
from ..utils import PatchedApi

api = PatchedApi()

api.add_namespace(example_ns)
