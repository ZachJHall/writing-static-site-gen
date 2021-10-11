import subprocess
import os
import frontmatter
from datetime import datetime

def genPost(file, title):
    command = ['pandoc', '-s', '-B', 'public/header.html', 'markdown/' + str(file), '-o', 'public/posts/' + title+'.html']
    subprocess.check_call(command)

def createPosts(dir):
    posts = []
    for file in os.listdir(dir):
        with open(dir + '/' + file) as f:
            front = frontmatter.load(f)

            posts.append(
                {
                    'date': front['date'],
                    'title': front['title'],
                    'type': front['date'],
                    'file': file
                }
            )
        genPost(file, front['title'])



    return posts

def insertLinks(file, posts):
    links = ""
    for post in posts:
        links += "<a href='{}'>{}</a>".format('posts/'+post['title']+'.html', post['title'])
        links += "<br>\n\t\t"
    
    with open(file, 'r') as f:
        content = f.read()

    content = content.replace('[links]', links)

    with open(file, 'w') as f:
        f.write(content)
    
        
        
    


def main():
    if not os.path.exists("public"):
        os.mkdir("public")
    if not os.path.exists("public/posts"):
        os.mkdir("public/posts")
    posts = createPosts('markdown')
    posts.sort(key = lambda post: datetime.strptime((post['date']), '%m-%d-%y'))

    insertLinks("public/index.html", posts)
    
main()