# Tornado Async Transformer

Tested with python3.11, may support >=python3.5 but that is untested.

A [libcst](https://github.com/Instagram/LibCST) transformer for updating tornado @gen.coroutine syntax to python3.5+ native async/await and converting list yields to equivalent `asyncio.gather(*coros)`.

### Install
TODO

### Usage
Inside the code directory you want to run the codemod on:
1. Create file `.libcst.codemod.yaml`:
```bash
echo -e \
'generated_code_marker: "@generated"
formatter: ["cat", "-"]
blacklist_patterns: []
modules:
- "tornado_async_transformer"
repo_root: "."' > .libcst.codemod.yaml
```
1. Run the codemod: `python -m libcst.tool codemod tool.TornadoAsyncTransformer SRC`

#### Example Codemod Output 
```diff
from tornado import gen

-@gen.coroutine
-def call_api():
-    response = yield fetch()
+async def call_api():
+    response = await fetch()
     if response.status != 200:
         raise BadStatusError()
-    raise gen.Return(response.data)
+    return response.data
```
