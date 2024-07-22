# Problem: https://www.hackerrank.com/challenges/merge-the-tools/problem
# Score: 40


def merge_the_tools(string, k):

    while string:
        chunk = ''
        partition = string[0:k]

        for i in partition:
            if i not in chunk:
                chunk += i
        print(chunk)
        string = string[k:]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)