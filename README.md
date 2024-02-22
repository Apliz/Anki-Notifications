# Notepad for my thoughts

1. Create a README
    1. Installation and user manual
2. In referece to get_decks_dict()
    1. Maybe there's a different function instead of ```all_names_and_ids()``` ? Using ```popitem()``` seems very wrong.
    2. Transfer method to helpers.py
3. Consider refactor of deck_names = [] within get_learnable_cards()
4. Consider if main(), pushover_post(), or grammar() **needs** their return statement
5. Can I legally use 'happy astronaut.jpg'
    1. Rename with underscore
6. Check Licences of all dependences and list for guidance to deciding the licence of this repository.
7. Consider making the imports DRY.
    1. Once import passed around entire codebase?
8. Code documentation
    1. Proper docstrings for all modules and methods
    2. Expected return types ```def foo() -> bar:```
9. Notification UI
    1. Find ways (if any) for  better readabiliy.
10. Consider accessibility
11. If there's an alternative to Pushover to avoid the fee that would be great but I'm not convinced... Maybe I can shoulder the $5 myself? Or can make the installation easier. There's something on [Pushover.net](https://support.pushover.net`i37-including-an-open-source-application-s-api-token-in-its-source-code) about this.
12. Pre-release check
    1. Portability
    2. Test suite
    3. Distributions
13. Create topology.md with methods grouped by page and connection.
14. An easily changable variable to set the maximum times a notification can be sent.
15. Explore the idea of a dynamic crontab entry.
16. Benchmarking
    1. Another header below 'control' to denote the other implementations.
    2. About section
        1. Reference to branches
        2. Better documentation of the average times. Consider incorporating within the table. Consider better dividers. Consider highlighting. Consider size
        3. Better Implementation names. Consider single word. Consider term 'pure Python' (what does that even mean?)
17. Network listener
    1. Allow users to check network against their own URLS
1. Abstract URLS into a constant. Allow easy UPDATE of URL strings

#### Benchmarking can be found here

[Benchmarking](Benchmarks.md)

### Happiest astronaut:  for dopamine purposes

![Happiest Astronaut](/happy%20astronaut.jpg)
