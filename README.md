# Notepad for my thoughts

1. Create a README
2. Decide how to deal with a failed internet connection.
    1. Work queues? Something like Rabbit MQ or Celery
        1. Not sure if they provide their own broker service, by REDIS can do this with its vectored database.
        2. Create my own SQL database and sleep() with maximum timeout.
        3. Really doesn't feel good to use sleep(). But maybe it's okay because only 1 user will receive one notification per day by default.
3. Sort out get_deck_dict() inside utils.py
    1. Maybe there's a different function within anki? Popping off the final element feels wrong. What if there's more than one junk element?
4. Proper notification UI. Make it readable, make it less clunky
5. If there's an alternative to Pushover to avoid the fee that would be great but I'm not convinced... Maybe I can shoulder the $5 myself? Or can make the installation easier. There's something on [Pushover.net](https://support.pushover.net/i37-including-an-open-source-application-s-api-token-in-its-source-code) about this.

## Happiest astronaut: for dopamine purposes

![Happiest Astronaut](/happy%20astronaut.jpg)
