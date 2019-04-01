def reduce_file_path(path):
    path=path.split('/')
    for file in range(len(path)):
        if path[file]=='..':
            path[file-1]=''
            path[file]=''
    while '' in path: 
        path.remove('')
    while '.' in path:
        path.remove('.')
    reduced='/'
    reduced+='/'.join(path)
    return reduced


def main():
    print(reduce_file_path('/home//rositsazz/courses/./Programming-101-Python-2019/week02/../'))
    print(reduce_file_path('/'))
    print(reduce_file_path("/srv/../"))
    print(reduce_file_path("/srv/www/htdocs/wtf/"))
    print(reduce_file_path("/srv/www/htdocs/wtf"))
    print(reduce_file_path("/srv/./././././"))
    print(reduce_file_path("/etc//wtf/"))
    print(reduce_file_path("/etc/../etc/../etc/../"))
    print(reduce_file_path("//////////////"))
    print(reduce_file_path("/../"))

if __name__=='__main__':
    main()