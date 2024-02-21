"""Benchmark module"""
import cProfile
import asyncio
from main import main

cProfile.run("asyncio.run(main())")
