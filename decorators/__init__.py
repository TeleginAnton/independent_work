from decorators.cache import lru_cache
try:
    import orjson as json
except ImportError:
    import json
