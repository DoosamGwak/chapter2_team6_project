class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        
    def display(self):
        print(f"{self.name}님의 아이디는 {self.username} 입니다.") 

class Post():
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

members = []
member1 = Member('이서원','dino','서원비밀번호')
member2 = Member('망고', 'mango','망고비밀번호')
member3 = Member('상추', 'tree', '상추비밀번호')
members.append(member1)
members.append(member2)
members.append(member3)


name = input("회원 이름 : ")
username = input("회원 아이디 : ")
password = input("회원 비밀번호 : ")
member = Member(name, username, password)
members.append(member)

print("---------회원은 다음과 같습니다.---------")
for member in members:
    member.display()
print("----------------------------------------")


posts = []
posts.append(Post('공룡1','공룡1에 대한 내용','dino'))
posts.append(Post('공룡2','공룡2에 대한 내용','dino'))
posts.append(Post('공룡3','공룡3에 대한 내용','dino'))
posts.append(Post('망고1','망고1에 대한 내용','mango'))
posts.append(Post('망고2','망고2에 대한 내용','mango'))
posts.append(Post('망고3','망고3에 대한 내용','mango'))
posts.append(Post('상추1','상추1에 대한 내용','tree'))
posts.append(Post('상추2','상추2에 대한 내용','tree'))
posts.append(Post('상추3','상추3에 대한 내용','tree'))

while True : 
    posting = input("게시글을 등록하시겠습니다? (y/n) : ")
    if posting.lower() == 'y' :
        author = input("아이디를 입력해주세요 : ")
        title = input("게시글 제목 : ")
        content = input("게시글 내용 : ")
        post = Post(title, content, author)
        posts.append(post)
        print("등록되었습니다.")
    elif posting.lower() == 'n' :
        print("----------게시글 등록 종료-----------")
        break
    else:
        print("y(yes) 또는 n(no) 을 입력해주세요.")

while True:
    author_searching = input("작성자로 검색하시겠습니까? (y/n) : ")
    if author_searching.lower() == 'y' :
        author_search = input("검색할 작성자의 아이디를 입력해주세요 : ")
        print(f"{author_search}님이 작성한 게시글은 다음과 같습니다 : ")
        for post in posts:
            if post.author == author_search:
                print(f"{post.title}")
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
        for post in posts:
            if keyword_search in post.content:
                print(f"{post.title}")
    elif keyword_searching.lower() == 'n' :
        print("----------게시글 검색 종료-----------")
        break
    else:
        print("y(yes) 또는 n(no) 을 입력해주세요.")
