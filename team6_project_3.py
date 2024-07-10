# import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.password_length = len(password)

    # def hash_password(self, password):
    #     return hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        masked_password = '*' * self.password_length
        print(
            f"Name : {self.name}, Id : {self.username}, Password : {masked_password}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(
            f"Title : {self.title}, Content : {self.content}, Author : {self.author}")


members = []
posts = []

def create_member():
    name = input("이름을 입력해주세요. : ")
    username = input("ID를 입력해주세요. : ")
    password = input("비밀번호를 입력해주세요. : ")
    members.append(Member(name, username, password))

def create_post(author):
    for _ in range(1):  # 최소한 3개의 게시물을 작성할 수 있도록
        title = input(f"제목을 입력해주세요. : ")
        content = input(f"주제를 입력해주세요. : ")
        posts.append(Post(title, content, author))

print("\nCreate Members")
create_member()

# 새로운 멤버의 게시물 생성
print(f"\nCreating posts for {members[-1].username}")
create_post(members[-1].username)

# 멤버 및 게시물 생성
while True:
    another_member = input("새로운 멤버를 추가하시겠습니까? (y/n): ").lower()
    
    if another_member == 'n':
        break
    
    elif another_member =='y':
        print("\nCreate Members")
        create_member()
        # 새로운 멤버의 게시물 생성
        print(f"\nCreating posts for {members[-1].username}")
        create_post(members[-1].username)
    
    else:
        print("잘못된 입력값입니다. 다시 입력해주세요. (y/n)")

print("\nAll Members:")
for member in members:
    member.display()

print("\nAll Posts:")
for post in posts:
    post.display()


while True:
    author_searching = input("작성자로 검색하시겠습니까? (y/n) : ")
    
    if author_searching.lower() == 'y' :
        author_search = input("검색할 작성자의 아이디를 입력해주세요 : ")
        print(f"{author_search}님이 작성한 게시글은 다음과 같습니다 : ")
        count_author = 0
        
        for post in posts:
            if post.author == author_search:
                print(f"{post.title}")
                count_author += 1
        
        if count_author == 0:
            print("해당 작성자의 게시물이 없습니다.")
    
    elif author_searching.lower() == 'n' :
        print("----------게시글 검색 종료-----------")
        break
    
    else:
        print("y(yes) 또는 n(no) 을 입력해주세요.")
        
while True:
    keyword_searching = input("키워드로 검색하시겠습니까? (y/n) : ")
    
    if keyword_searching.lower() == 'y' :
        keyword_search = input("내용 키워드를 입력해주세요 : ")
        print(f"'{keyword_search}'가 내용에 포함된 게시글은 다음과 같습니다 : ")
        count_keyword = 0
        
        for post in posts:
            if keyword_search in post.content:
                count_keyword += 1
                print(f"{post.title}")
        
        if count_keyword == 0:
            print("키워드에 해당하는 검색결과가 없습니다.")
    
    elif keyword_searching.lower() == 'n' :
        print("----------게시글 검색 종료-----------")
        break
    
    else:
        print("y(yes) 또는 n(no) 을 입력해주세요.")

print("모든 검색과정이 종료되었습니다.")