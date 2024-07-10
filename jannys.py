# ----- 코드 정의 ------
import pprint
import hashlib

member_list = []


class Member():
    # Todo : 코드 구현이 필요합니다.
    def member_info(self):
        member_infos = {}

        name = input('등록할 멤버 이름을 입력하세요 : ')
        username = input('등록할 ID를 입력하세요 : ')
        password = input('등록할 비밀번호를 입력하세요 : ')
        member_infos['name'] = name
        member_infos['username'] = username
        member_infos['password'] = password

        member_list.append(member_infos)

    def display(self):
        show_member = input("등록된 멤버를 조회하시겠습니까? (y/n) : ")
        show_member = show_member.lower()
        while True:
            if show_member == "y":
                pprint.pprint(member_list)
                return
            elif show_member == "n":
                print("조회하지 않습니다.")
                return
            else:
                print("유효하지 않은 입력입니다. 다시 입력해주세요")
                show_member = input("멤버를 조회하시겠습니까? (y/n) : ")


post_list = []


class Post(Member):
    # Todo : 코드 구현이 필요합니다.
    def check_member(self):

        push_name = input("ID를 입력하세요 : ")
        while True:
            if push_name in member_list["name"]:
                break
            else:
                print("ID가 정확하지 않습니다. 다시 입력해주세요")
                push_name = input("ID를 입력하세요 : ")

    def create_post(self):
        print(member_list)
        return
    pass


member = Member()

info_input = input("멤버를 추가하시겠습니까? (y/n) : ")
info_input = info_input.lower()
while True:
    if info_input == "y":

        member.member_info()

        print("-"*20)
        reinput = input('다른 멤버를 추가하시겠습니까? (y/n) : ')
        reinput = reinput.upper()

        if reinput == "y":
            continue
        elif reinput == 'n':
            print('-'*20)
            print('멤버등록을 종료합니다.')
            print('-'*20)
            break
        else:
            print("유효하지 않은 입력입니다. 다시 입력해주세요")
            reinput = input('다른 멤버를 추가하시겠습니까? (y/n) : ')

    elif info_input == "n":
        print("멤버등록을 종료합니다.")
        break
    else:
        print("유효하지 않은 입력입니다. 다시 입력해주세요")
        info_input = input("멤버를 추가하시겠습니까? (y/n) : ")

member.display()

# member_post = Post()
# member_post.create_post()

# member_post.check_member()
