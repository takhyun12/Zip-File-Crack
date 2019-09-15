import zipfile
import itertools
import os
import time

def crack_ZIP(zfile, password): # 압축파일에 비밀번호를 입력하는 기능
    try:
        zfile.extractall(pwd=password) # 인자를 통해 전달받은 비밀번호로 크랙을 시도한다.
        print('비밀번호를 식별하였습니다. 비밀번호=[%s]' %password.decode()) # 크랙에 성공하면 비밀번호를 알려준다
        return True # 크랙에 성공하면 True(참)을 리턴함
    except: # 비밀번호로 크랙을 시도할 때 오류가 발생하는 경우
        pass # 다음 비밀번호를 대입하기 위해 구문을 pass함
        return False # 크랙에 실패하였으니 False(거짓)을 리턴함

if __name__ == '__main__':
    print('[*] 압축파일 비밀번호 탈취 프로그램 by 공군 군수전산소')
    print('[1/2] 비밀번호 탈취가 필요한 파일을 입력하시오.  예시) C:\업무\자료모음.zip')
    input_zfile = input('[>] ') # 콘솔창에서 파일경로를 입력받음

    if not os.path.exists(input_zfile): # 사용자가 입력한 파일경로에 파일이 존재하지 않는 경우
        print('[!] 잘못된 파일경로를 입력하였습니다. 다시 실행하여 주시기 바랍니다.')
        exit() # 잘못된 파일을 입력하였으니 프로그램을 종료함

    try:
        zfile = zipfile.ZipFile(input_zfile, 'r') # 정상적으로 입력된 압축파일을 zipfile 객체에 할당함
    except:
        print('[!] 정상적인 압축파일이 아닙니다. 다시 실행하여 주시기 바랍니다.')

    level = ['1', '2', '3', '4', '5', '6'] # 크랙의 난이도에 활용될 리스트 (1단계~6단계)
    print('[2/2] 유추되는 비밀번호의 강도를 아래 중 선택하여 입력하시오.  예시) 3')
    print('1 : 비밀번호가 숫자만으로 구성된 경우')
    print('2 : 비밀번호가 영문(소문자)만으로 구성된 경우')
    print('3 : 비밀번호가 영문(대/소문자)만으로 구성된 경우')
    print('4 : 비밀번호가 영문(소문자)와 숫자로 구성된 경우')
    print('5 : 비밀번호가 영문(대/소문자)와 숫자로 구성된 경우')
    print('6 : 비밀번호가 무엇으로 설정 되었는지 유추가 불가한 경우 (특수문자 포함)')
    crack_level = input('[>] ') # 사용자로부터 비밀번호 크랙 시 필요한 강도를 입력받음

    if crack_level not in level:
        print('[!] 1 ~ 6 단계의 숫자만 입력 하실 수 있습니다. 다시 실행하여 주시기 바랍니다.')
        exit()
    else:
        if crack_level == '1': # 사용자가 1을 입력한 경우
            characters = '0123456789'
        elif crack_level == '2': # 사용자가 2를 입력한 경우
            characters = 'abcdefghijklmnopqrstuvwxyz'
        elif crack_level == '3': # 사용자가 3를 입력한 경우
            characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif crack_level == '4': # 사용자가 4를 입력한 경우
            characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        elif crack_level == '5': # 사용자가 5를 입력한 경우
            characters = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif crack_level == '6': # 사용자가 6를 입력한 경우
            characters = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}:"<>?[];,./'

    start_time = time.time() # 크랙이 시작되는 현재시점의 시간을 구함
    for leng in range(1, len(characters)+1):
        it = itertools.product(characters, repeat=leng) #characters에 모든 단어들로 모든 경우의 수를 만듬
        for password in it: # 경우의 수별로 비밀번호 크랙을 반복하여 실시함
            password = ''.join(password)
            result = crack_ZIP(zfile, password.encode('utf-8')) # 비밀번호 크랙시도 후 결과를 받아옴
            if result == True: # 비밀번호 크랙에 성공한 경우
                break # 비밀번호 크랙을 시도하는 반복문을 종료함
        if result == True: # 비밀번호 크랙에 성공한 경우 경우의 수 생성 반복문 또한 종료함
            break
    end_time = time.time() - start_time
    print('[!] 비밀번호 탈취 간 ' + str(end_time) + ' 초 소요됨 ')
