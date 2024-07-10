from pprint import pprint

class Member:
    member_count = 0

    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password
        Member.member_count += 1

    def member_display(self):
        print("이름: ",self.name, "\nID: ", self.id, "\nPassword :", "*"*len(self.password))

class Post:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def post_display(self):
        print("작성자: ",self.id, "\n제목: ", self.title, "\n내용: ", self.content)

members = []
posts = []

def member_input():
    member = Member(input("이름을 입력해주세요: "), 
                    input("ID를 입력해주세요: " ), 
                    input("비밀번호를 입력해주세요: ")) #append에 넣어서 해보기
    
    members.append({"name" : member.name, 
                    "ID" : member.id, 
                    "password" : member.password})
    
    member.member_display


def post_input():
    post = Post(members[-1]["name"], input("제목을 입력해주세요: " ), input("내용을 입력해주세요: "))
    
    posts.append({"ID" : post.id, 
                "title" : post.title, 
                "content" : post.content})
    
    post.post_display
    print(posts)


def input_check():
    check = input("정보를 입력하시겠습니까?: (y/n): ")
    
    if check == 'y':
        member_input()
        post_input()
    elif check == 'n':
        return
    else:
        print("잘못된 입력값입니다. 다시 입력해주세요.")
        input_check()

    input_check()

def search_check():
    check_id = input("유저를 찾으시겠습니까?: (y/n): ")
    
    for post in posts:
        if post["ID"] == check_id:
            print(post)

input_check()
search_check()