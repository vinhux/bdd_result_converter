import argparse
import read_file, consume_json, generate_html

parser = argparse.ArgumentParser(description='Run BDD Result Converter (JSON -> HTML)')

parser.add_argument(
    '-t', '--type', type=str, nargs='+', 
    help='Specify the type. Options: behave | cucumber'
)

parser.add_argument(
    '-f', '--file', type=str, nargs='+', 
    help='Specify file path to convert'
)

gh = generate_html.GenerateHTML()
rf = read_file.ReadFile()
cj = consume_json.ConsumeJSON()

def main() -> None:
    args = parser.parse_args()
    type = args.type
    # for f in args.files:
    convert(type, args.file)
    

def convert(type, f) -> None:
    test_cases = []
    if type == 'behave':
        file_content = rf.read_file_to_json(f)
        test_cases = cj.convert_json_to_obj(file_content)
    standard_test_cases = cj.standardize_json_format(test_cases)
    gh.generate(standard_test_cases)


if __name__ == '__main__':
    main()