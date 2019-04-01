import json
import sys

def business_card(file_name):
    result = list()
    with open(file_name) as json_file:
        data = json.load(json_file)

    for person in data['people']:
        name = person['first_name'] + ' ' + person['last_name']
        avatar = person['first_name'].lower()
        file = person['first_name'].lower()+'_'+person['last_name'].lower()+'.html'
        gender = person['gender']
        age = person['age']
        birth_date = person['birth_date']
        birth_place = person['birth_place']

        content = """<!DOCTYPE html>
                    <html>
                    <head>
                      <title>{}</title>
                      <link rel="stylesheet" type="text/css" href="styles.css">
                    </head>
                    <body>
                      <div class="business-card {}">
                        <h1 class="full-name">{}</h1>
                        <img class="avatar" src="avatars/{}.png">
                        <div class="base-info">
                          <p>Age: {}</p>
                          <p>Birth date: {}</p>
                          <p>Birth place: {}</p>
                          <p>Gender: {}</p>
                        </div>
                        <div class="interests">
                          <h2>Interests:</h2>
                    <ul>""".format(name,gender,name,avatar,age,birth_date,birth_place,gender)
        interests = person['interests']
        for interest in interests:
            content += '\n\t<li>{}</li>'.format(interest)
        content += """ </ul>
                    </div>
                    <div class="skills">
                        <h2>Skills:</h2>
                        <ul>"""
        skills = person['skills']
        for skill in skills:
            content += '<li>{} - {}</li>\n'.format(skill['name'],skill['level'])
        content += """ </ul>
                    </div>
                  </div>
                </body>
                </html>"""

        with open(file,'w') as html_file:
            html_file.write(content)
        result+=[file]

    return result

def main():
    file_name=sys.argv[1]
    print(business_card(file_name))

if __name__=='__main__':
    main()