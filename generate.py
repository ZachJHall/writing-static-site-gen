import subprocess
import os

def genPost(file):
    name = file.split('.')[0]
    command = ['pandoc', '-s', '-B', 'public/header.html', 'markdown/' +str(file), '-o', 'public/posts/' + str(name)+'.html']
    subprocess.check_call(command)

def createPosts(dir):
    for file in os.listdir(dir):
        genPost(file)


def main():
    if not os.path.exists("public"):
        os.mkdir("public")
    if not os.path.exists("public/posts"):
        os.mkdir("public/posts")
    createPosts('markdown')
    
main()