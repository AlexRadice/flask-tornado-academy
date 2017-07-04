# flask-tornado-academy
Step by step guides to Flask and tornado

Flask Step by Step Example
---------------------------
This is found in sub folder flaskeg. The code is increased incrementally in complexity in 7 steps,
each step having an associated git tag.

|Step # | Subject                                                      | git command |
|-------|--------------------------------------------------------------|--------------------------|
|1      | Most basic flask application possible                        | git checkout Step1_Simple |
|2      | Model, View, Controller and Routing (MVC)                    | git checkout Step2_MVC |
|3      | Flask MethodView base class for creating controllers         | git checkout Step3_MethodView |
|4      | Flask Login for authenticationand Flask Principal for        | git checkout Step4_Auth |
|       | authorisation                                                | |
|5      | Call custom functions from jinja templates                   | git checkout Step5_jinjaglobals |
|6      | Asset bundling and cache busting                             | git checkout Step6_Assets |
|7      | Unit tests                                                   | git checkout Step7_or_0 |


Tornado Step by Step Example
----------------------------
This is found in sub folder tornadoeg. The code is increased incrementally in complexity in 7 steps,
each step having an associated git tag.

|Step # | Subject                                                      | git command |
|------|--------------------------------------------------------------|------------------------------|
|1      | Most basic tornado application possible                      | git checkout Tornado_Step1_Simple |
|2      | Unit tests                                                   | git checkout Tornado_Step2_UnitTests |
|3      | @asynchronous decorator, requires code to call finish()      | git checkout Tornado_Step3-2_async |
|4      | @coroutine decorator simplifies layout of code async         | git checkout Tornado_Step4_coroutine |
|       | Call multiple async I/O operations in series                 | git checkout Tornado_Step4-2_series |
|       | Call multiple async I/O operations in parallel               | git checkout Tornado_Step4-3_parallel |
|       | Create your own async I/O subroutines                        | git checkout Tornado_Step4-4_call_sub |
|5      | Enhance unit tests using mock backends                       | git checkout Tornado_Step5_UnitTests2 |
|6      | Alternative @engine decorator for backends using callbacks   | git checkout Tornado_Step6_engine |
|7      | Async I/O subroutines without decorators                     | git checkout Tornado_Step7_puzzle |
