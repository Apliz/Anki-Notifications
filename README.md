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

## Happiest astronaut:  for dopamine purposes

![Happiest Astronaut](/happy%20astronaut.jpg)
