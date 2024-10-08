import os
import pytest
from gendiff.gendiff import generate_diff


# __file__ — это специальная переменная в Python, которая содержит полный
# путь к файлу, где она используется. Необходима  для определения полного
# путя к папке fixtures относительно текущего местоположения файла.
FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


def read_fixture(file_path):
    with open(file_path) as f:
        return f.read()


def write_fixture(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)


file1_json = os.path.join(FIXTURES_PATH, 'test1_file1.json')
file2_json = os.path.join(FIXTURES_PATH, 'test1_file2.json')
file1_yaml = os.path.join(FIXTURES_PATH, 'test1_file1.yaml')
file2_yaml = os.path.join(FIXTURES_PATH, 'test1_file2.yaml')


file3_json = os.path.join(FIXTURES_PATH, 'test2_file1.json')
file4_json = os.path.join(FIXTURES_PATH, 'test2_file2.json')
file3_yaml = os.path.join(FIXTURES_PATH, 'test2_file1.yaml')
file4_yaml = os.path.join(FIXTURES_PATH, 'test2_file2.yaml')


file5_json = os.path.join(FIXTURES_PATH, 'test3_file1.json')
file6_json = os.path.join(FIXTURES_PATH, 'test3_file2.json')
file5_yaml = os.path.join(FIXTURES_PATH, 'test3_file1.yaml')
file6_yaml = os.path.join(FIXTURES_PATH, 'test3_file2.yaml')


file7_json = os.path.join(FIXTURES_PATH, 'test4_file1.json')
file8_json = os.path.join(FIXTURES_PATH, 'test4_file2.json')
file7_yaml = os.path.join(FIXTURES_PATH, 'test4_file1.yaml')
file8_yaml = os.path.join(FIXTURES_PATH, 'test4_file2.yaml')


file9_json = os.path.join(FIXTURES_PATH, 'test5_file1.json')
file10_json = os.path.join(FIXTURES_PATH, 'test5_file2.json')
file9_yaml = os.path.join(FIXTURES_PATH, 'test5_file1.yaml')
file10_yaml = os.path.join(FIXTURES_PATH, 'test5_file2.yaml')

json_res1 = os.path.join(FIXTURES_PATH, 'results/test1_result_stylish.txt')
json_res2 = os.path.join(FIXTURES_PATH, 'results/test2_result_stylish.txt')
json_res3 = os.path.join(FIXTURES_PATH, 'results/test3_result_stylish.txt')
json_res4 = os.path.join(FIXTURES_PATH, 'results/test4_result_stylish.txt')
json_res5 = os.path.join(FIXTURES_PATH, 'results/test5_result_stylish.txt')


plain_result1 = os.path.join(FIXTURES_PATH, 'results/test1_result_plain.txt')
plain_result2 = os.path.join(FIXTURES_PATH, 'results/test2_result_plain.txt')
plain_result3 = os.path.join(FIXTURES_PATH, 'results/test3_result_plain.txt')
plain_result4 = os.path.join(FIXTURES_PATH, 'results/test4_result_plain.txt')
plain_result5 = os.path.join(FIXTURES_PATH, 'results/test5_result_plain.txt')


test_cases = [
    (generate_diff, file1_json, file2_json, json_res1, 'stylish'),
    (generate_diff, file1_yaml, file2_yaml, json_res1, 'stylish'),
    (generate_diff, file3_json, file4_json, json_res2, 'stylish'),
    (generate_diff, file3_yaml, file4_yaml, json_res2, 'stylish'),
    (generate_diff, file5_json, file6_json, json_res3, 'stylish'),
    (generate_diff, file5_yaml, file6_yaml, json_res3, 'stylish'),
    (generate_diff, file7_json, file8_json, json_res4, 'stylish'),
    (generate_diff, file7_yaml, file8_yaml, json_res4, 'stylish'),
    (generate_diff, file9_json, file10_json, json_res5, 'stylish'),
    (generate_diff, file9_yaml, file10_yaml, json_res5, 'stylish'),

    (generate_diff, file1_json, file2_json, plain_result1, 'plain'),
    (generate_diff, file1_yaml, file2_yaml, plain_result1, 'plain'),
    (generate_diff, file3_json, file4_json, plain_result2, 'plain'),
    (generate_diff, file5_json, file6_json, plain_result3, 'plain'),
    (generate_diff, file5_yaml, file6_yaml, plain_result3, 'plain'),
    (generate_diff, file7_json, file8_json, plain_result4, 'plain'),
    (generate_diff, file7_yaml, file8_yaml, plain_result4, 'plain'),
    (generate_diff, file9_json, file10_json, plain_result5, 'plain'),
    (generate_diff, file9_yaml, file10_yaml, plain_result5, 'plain'),
]


@pytest.mark.parametrize(
    "generate_diff_func, file1, file2, expected_file, format_", test_cases
)
def test_generate_diff(
        generate_diff_func,
        file1,
        file2,
        expected_file,
        format_
):
    expected = read_fixture(expected_file)
    actual = generate_diff_func(str(file1), str(file2), format_)

    assert actual == expected
