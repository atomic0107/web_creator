import json

json_path = 'web_creator.json'
html_path = 'index.html'

def body_create(f,web_obj):
    f.write("<body></body>\n")

def web_creator(web_obj):
    with open(html_path,mode='w') as f:
        f.write("<html>\n")
        body_create(f,web_obj)
        f.write("</html>\n")

def json_analyze():
    with open(json_path) as f:
        data = json.load(f)

    for i in data.keys():
        print(i)
        web_creator(i)


def main():
    print("main")
    json_analyze()

if __name__ == "__main__":
    main()