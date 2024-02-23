# Benchmarking

Ran using the [Cprofile](https://docs.python.org/3/library/profile.html#module-cProfile) interface for ```lsprof```

Network speed was approximately 102Mbps with [speedtest.net](https://speedtest.net)

|Test device                    |
|-------------------------------|
|16 GB 1600 MHz DDR3            |
|2.5 GHz Quad-Core Intel Core i7|
|Mid 2015                       |

### Control 
---
POST only - no network listener </br>
``` Average: 0.619s``` </br>
```Average time to complete (TTC): 0.619s```

| Calls | Primitives | time / s | getresponse / s | time-getresponse / s | Calls / s (5sf) |
|-------|------------|--------|-------------|------------------|----------------|
| 10215 | 10063      | 0.313  | 0.247       | 0.066            | 32,636         |
| "     | "          | 0.537  | 0.471       | 0.066            | 19,022         |
| "     | "          | 0.751  | 0.685       | 0.066            | 13,602         |
| "     | "          | 0.529  | 0.460       | 0.069            | 19,310         |
| "     | "          | 0.726  | 0.641       | 0.085            | 14,070         |
| "     | "          | 0.858  | 0.779       | 0.079            | 11,906         |


## Implementations


### Asyncio
Git branch: 'async' </br>
```Average : 0.069s``` </br>
```Average TTC : 0.763s```

| Calls | Primitives | time/s | getresponse | time-getresponse | Calls/s (5S.f) |
|-------|------------|--------|-------------|------------------|----------------|
| 9261  | 9101       | 0.812  | 0.731       | 0.081            |                |
| "     | "          | 0.715  | 0.655       | 0.060            |                |
| "     | "          | 0.741  | 0.681       | 0.060            |                |
| "     | "          | 0.749  | 0.685       | 0.064            |                |
| "     | "          | 0.747  | 0.682       | 0.065            |                |
| "     | "          | 0.814  | 0.729       | 0.085            |                |


## Multi-threading
Git branch: "threading" </br>
```Average : 0.109s``` </br>
```Average TTC : 0.634s```

| Calls | Primitives | time/s | getresponse | time-getresponse | Calls/s (5S.f) |
|-------|------------|--------|-------------|------------------|----------------|
| 8209  | 8037       | 0.748  | 0.663       | 0.085            | 10,975         |
| "     | "          | 0.434  | 0.328       | 0.106            | 18,915         |
| "     | "          | 0.785  | 0.709       | 0.076            | 10,457         |
| "     | "          | 0.674  | 0.499       | 0.175            | 12,001         |
| "     | "          | 0.553  | 0.465       | 0.088            | 14,844         |
| "     | "          | 0.610  | 0.484       | 0.126            | 13,457         |

## Simple Queue
Git branch: "master" </br>
```Average: 0.069s``` </br>
```Average TTC: 0.625s```

| Calls | Primitives | time/s | getresponse | time-getresponse | Calls/s (5S.f) |
|-------|------------|--------|-------------|------------------|----------------|
| 8143  | 7995       | 0.529  | 0.458       | 0.071            |                |
| "     | "          | 0.748  | 0.669       | 0.079            |                |
| "     | "          | 0.508  | 0.444       | 0.064            |                |
| "     | "          | 0.841  | 0.781       | 0.060            |                |
| "     | "          | 0.293  | 0.226       | 0.067            |                |
| "     | "          | 0.831  | 0.757       | 0.074            |                |
