import json
import sys

def coding_skills(file_name):
    output = dict()
    with open(file_name) as json_file:
        data = json.load(json_file)

    for person in data['people']:
        for skill in person['skills']:
            output[skill['name']] = []

    for person in data['people']:
        for skill in person['skills']:
            output[skill['name']] += [(skill['level'],str(person['first_name'] + ' ' + person['last_name']))]

    for key in output:
        output[key] = list(reversed(sorted(output[key])))
        output[key] = output[key][:1]
        print(key + ' - ' + output[key][0][1])
    return output

def main():
    json_file = sys.argv[1]
    coding_skills(json_file)

if __name__ == '__main__':
    main()
