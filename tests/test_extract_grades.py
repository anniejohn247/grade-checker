# test using python -m tests.test_extract_grades
from src.grade_checker import extract_grades

fake_html_before = """
<table id="studentAssignmentsTable"><tbody>
  <tr><td>Problem sheet</td><td></td><td></td><td></td><td></td><td></td><td>&#160;</td></tbody></table>
"""

fake_html_after = """
<table id="studentAssignmentsTable"><tbody>
  <tr><td>Problem sheet</td><td></td><td></td><td></td><td></td><td></td><td>16.0&#160;</td></tbody></table>
"""

old = extract_grades(fake_html_before)
new = extract_grades(fake_html_after)
print(old)  # {"Problem sheet": ""}
print(new)  # {"Problem sheet": "16.0"}