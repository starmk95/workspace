def main():
    while True:
        user_input = input("문장을 입력하세요 (종료하려면 'exit' 입력): ")
        if user_input.lower() == 'exit':
            print("입력을 종료합니다.")
            break
        print("입력한 문장:", user_input)

if __name__ == "__main__":
    main()
