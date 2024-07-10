import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self.hash_password(password)
        self.password_length = len(password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

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
    for _ in range(3):  # 최소한 3개의 게시물을 작성할 수 있도록
        title = input(f"제목을 입력해주세요. : ")
        content = input(f"주제를 입력해주세요. : ")
        posts.append(Post(title, content, author))


# 멤버 및 게시물 생성
while True:
    print("\nCreate Members")
    create_member()

    print("\nMembers:")
    for member in members:
        member.display()

    # 새로운 멤버의 게시물 생성
    print(f"\nCreating posts for {members[-1].name}")
    create_post(members[-1].name)

    another_member = input("새로운 멤버를 추가하시겠습니까? (yes/no): ").lower()
    if another_member != 'yes':
        break

print("\nAll Members:")
for member in members:
    member.display()

print("\nAll Posts:")
for post in posts:
    post.display()

# 검색 과정
while True:
    #
    search_user = input(
        "\n해당 작성자의 게시물 : ")
    print(f"Posts by {search_user}:")
    for post in posts:
        if post.author == search_user:
            print(post.title)

    #
    search_word = input("검색하신 주제로 작성된 게시물 : ")
    print(f"Posts containing '{search_word}':")
    for post in posts:
        if search_word in post.content:
            print(post.title)

    another_search = input(
        "다른 내용을 또 검색하고 싶으신가요? (yes/no): ").lower()
    if another_search != 'yes':
        break

print("검색과정이 종료되었습니다.")
