# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest

import Prob1
import Prob2


class Test_Prob1:
    def test_replicates_pdf_example(self, monkeypatch, capsys):
        input_values = ['223','251','317','636','766','607','607', '']
        monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        Prob1.largest_two()
        captured = capsys.readouterr().out.splitlines()
        assert '766' in captured[-2], f"The largest number 766 should be appearing on the second to last line of your output!"
        assert '636' in captured[-1], f"The second-largest number 636 should be appearing on the second to last line of your output!"

    def test_alternative_amount_of_values(self, monkeypatch, capsys):
        input_values = ['412', '392', '744', '13', '']
        monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        Prob1.largest_two()
        captured = capsys.readouterr().out.splitlines()
        assert '744' in captured[-2], f"The largest number 744 should be appearing on the second to last line of your output!"
        assert '412' in captured[-1], f"The second-largest number 412 should be appearing on the second to last line of your output!"

    def test_with_negative_values(self, monkeypatch, capsys):
        input_values = ['-42', '36', '-14', '-999999999999999999', '']
        monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        Prob1.largest_two()
        captured = capsys.readouterr().out.splitlines()
        assert '36' in captured[-2], f"The largest number 36 should be appearing on the second to last line of your output!"
        assert '-14' in captured[-1], f"The second-largest number -14 should be appearing on the second to last line of your output!"

    def test_equal_values(self, monkeypatch, capsys):
        input_values = ['13', '13', '']
        monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        Prob1.largest_two()
        captured = capsys.readouterr().out.splitlines()
        assert '13' in captured[-2], f"The largest number 13 should be appearing on the second to last line of your output!"
        assert '13' in captured[-1], f"The second-largest number 13 should be appearing on the second to last line of your output!"


class Test_Prob2:
    def test_correct_symbol(self, capsys):
        Prob2.draw_console_pyramid(3)
        captured = capsys.readouterr().out.strip()
        assert captured[-1] == '*', 'Are you not using the * symbol to build your pyramid?'

    def test_correct_number_of_rows(self, capsys):
        inputs = [1,3,8]
        for r in inputs:
            Prob2.draw_console_pyramid(r)
            captured = capsys.readouterr().out.splitlines()
            assert len(captured) == r, f"You don't seem to be outputting the desired number of rows. You wanted {r} and instead printed {len(captured)}."

    def test_row_growth_rate(self, capsys):
        Prob2.draw_console_pyramid(5)
        captured = capsys.readouterr().out.splitlines()
        for i in range(len(captured)):
            assert captured[i].count('*') == 1 + 2 * i, 'The number of * in each row is not increasing by 2 each time'

    def test_symmetric_pyramid(self, capsys):
        Prob2.draw_console_pyramid(10)
        captured = capsys.readouterr().out.splitlines()
        start = captured[0].find('*')
        for i, row in enumerate(captured):
            assert row.find('*') == start - i, 'The left side of your pyramid is not symmetric?'
            assert row.rfind('*') == start + i, 'The right side of your pyramid is not symmetric?'

    def test_against_left_margin_at_bottom(self, capsys):
        Prob2.draw_console_pyramid(10)
        captured = capsys.readouterr().out.splitlines()
        assert captured[-1][0] == '*', 'Your pyramid should be against the left edge at the bottom, and it seems to not be.'




class Test_Prob3:
    def test_used_a_loop(self):
        with open('Prob3.py', 'r') as f:
            filestr = ''.join(f.readlines())
        assert 'while' in filestr or 'for' in filestr, 'It does not look like you used a loop anywhere in your image.\n'
    
    def test_defined_a_function(self):
        with open('Prob3.py', 'r') as f:
            filestr = ''.join(f.readlines())
        assert 'def' in filestr, 'It does not look like you defined a function anywhere in your image.\n'

    def test_created_a_label(self):
        with open('Prob3.py', 'r') as f:
            filestr = ''.join(f.readlines())
        assert 'GLabel(' in filestr, 'Did you remember to include a centered label in your image?\n'
