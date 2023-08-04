import io
import importlib
import os
import builtins
import sys


import pytest


module_name = "favorite_artist"


def test_script_exists():
    curr_dir = os.getcwd()
    accepted_subfolders = ["src"]
    for subfolder in accepted_subfolders:
        filename = os.path.join(curr_dir, subfolder, f'{module_name}.py')
        if os.path.exists(filename):
            assert True
            return
        print(f"Not found: {filename}")
    new_line = "\n"
    assert False, (f"{module_name}.py was not found.\n"
                   "Make sure it is in an accepted subfolder below:\n"
                   f"{new_line.join(accepted_subfolders)}")


def test_integer_input(monkeypatch):
    # patches the standard output to catch the output of print()
    test_inputs = ["Pablo Picasso", "painter", "Girl before a Mirror", "complex", "colorful"]
    patch_stdout = io.StringIO()
    expected = "Pablo Picasso is my favorite painter!\nMy favorite work from Pablo Picasso is Girl before a Mirror.\nI love it, because is it is so complex and colorful!\n"
    # Returns a new mock object which undoes any patching done inside
    # the with block on exit to avoid breaking pytest itself.
    with monkeypatch.context() as m:
        # patches the input()
        m.setattr('builtins.input', lambda _: test_inputs.pop(0))
        m.setattr('sys.stdout', patch_stdout)
        sys.modules.pop(module_name, None)
        importlib.import_module(name=module_name)
    assert patch_stdout.getvalue() == expected, ("Incorrect output!")


def test_float_input(monkeypatch):
    # patches the standard output to catch the output of print()
    test_inputs = ["P!nk", "singer", "Try", "thought-provoking", "meaningful"]
    patch_stdout = io.StringIO()
    expected = "P!nk is my favorite singer!\nMy favorite work from P!nk is Try.\nI love it, because is it is so thought-provoking and meaningful!\n"
    # Returns a new mock object which undoes any patching done inside
    # the with block on exit to avoid breaking pytest itself.
    with monkeypatch.context() as m:
        # patches the input()
        m.setattr('builtins.input', lambda _: test_inputs.pop(0))
        m.setattr('sys.stdout', patch_stdout)
        sys.modules.pop(module_name, None)
        importlib.import_module(name=module_name)
    assert patch_stdout.getvalue() == expected, ("Incorrect output!")


def test_zeroes_input(monkeypatch):
    # patches the standard output to catch the output of print()
    test_inputs = ["123", "numbers", "0", "easy", "small"]
    patch_stdout = io.StringIO()
    expected = "123 is my favorite singer!\nMy favorite work from 123 is 0.\nI love it, because is it is so easy and small!\n"
    # Returns a new mock object which undoes any patching done inside
    # the with block on exit to avoid breaking pytest itself.
    with monkeypatch.context() as m:
        # patches the input()
        m.setattr('builtins.input', lambda _: test_inputs.pop(0))
        m.setattr('sys.stdout', patch_stdout)
        sys.modules.pop(module_name, None)
        importlib.import_module(name=module_name)
    assert patch_stdout.getvalue() == expected, ("Incorrect output!")
