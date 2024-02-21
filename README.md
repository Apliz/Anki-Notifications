# Notepad for my thoughts

1. Create a README
2. Decide how to deal with a failed internet connection.
    1. Work queues? Something like Rabbit MQ or Celery
        a. Huey with RQ
    2. SQL database with ```time.sleep()``` in the script, cap with maximum timeout?
        1. Definitely not a top sensation. But still consider for ease.
3. Sort out ```get_deck_dict()``` for the love of God
    1. Maybe there's a different function instead of ```all_names_and_ids()``` ? Using ```popitem()``` seems very wrong.
4. Proper notification UI - readable and less clunky
5. If there's an alternative to Pushover to avoid the fee that would be great but I'm not convinced... Maybe I can shoulder the $5 myself? Or can make the installation easier. There's something on [Pushover.net](https://support.pushover.net/i37-including-an-open-source-application-s-api-token-in-its-source-code) about this.

## Benchmarking

### Control

###### Pure Python with no queue implementation

| Calls | Primitives | time / s | getresponse / s | time-getresponse / s | Calls / s (5sf) |
|-------|------------|--------|-------------|------------------|----------------|
| 10215 | 10063      | 0.313  | 0.247       | 0.066            | 32,636         |
| "     | "          | 0.537  | 0.471       | 0.066            | 19,022         |
| "     | "          | 0.751  | 0.685       | 0.066            | 13,602         |
| "     | "          | 0.529  | 0.460       | 0.069            | 19,310         |
| "     | "          | 0.726  | 0.641       | 0.085            | 14,070         |
| "     | "          | 0.858  | 0.779       | 0.079            | 11,906         |

###### Pure Python with Asyncio

| Calls | Primitives | time/s | getresponse | time-getresponse | Calls/s (5S.f) |
|-------|------------|--------|-------------|------------------|----------------|
| 9261  | 9101       | 0.812  | 0.731       | 0.081            |                |
| "     | "          | 0.715  | 0.655       | 0.060            |                |
| "     | "          | 0.741  | 0.681       | 0.060            |                |
| "     | "          | 0.749  | 0.685       | 0.064            |                |
| "     | "          | 0.747  | 0.682       | 0.065            |                |
| "     | "          | 0.814  | 0.729       | 0.085            |                |

### Happiest astronaut:  for dopamine purposes

![Happiest Astronaut](/happy%20astronaut.jpg)
