"""
There is a collection of input strings and a collection of query strings. For each query string, determine how many
times it occurs in the list of input strings.

For example, given input "strings=['ab','ab','abc']" and "queries=['ab','abc','bc']", we find "2" instances of "ab",
1 of "abc" and 0 of "bc".For each query, we add an element to our retrun array, "results=[2,1,0]
Function Descrption:
Complete the function matchingStrings in the editor below. The function must return an array of integers representing
the frequency of occurrence of each query string in strings.
matchingStrings has the following parameters:
strings - an array of strings to search
queries - an array of query strings

Input Format:
The first line contains and integer "n", the size of "strings".
Each of the next "n" lines contains a string strings[i].
The next line contains q, the size of queries.
Each of the next q lines contains a string q[i].

Constraints:
1 <= n <= 1000
1 <= q <= 1000
1 <= |strings[i]|,|quries[i]| <= 20

Output Format:
Return an integer array of the results of all queries in order.

Sample Input 1: => 4(array strings) and 3(array queries) like below:
4
aba
baba
aba
xzxb
3
aba
xzxb
ab

Sample Output 1:
2
1
0

Explanation 1:

Here, "aba" occurs twice, in the first and third string. The string "xzxb" occurs once in the fourth string, and "ab"
does not occur at all.

Sample Input 2: => 3(array strings) and 3(array queries) like below:
3
def
de
fgh
3
de
lmn
fgh

Sample Output 2: => 13(array strings) and 5(array queries) like below:
1
0
1

Sample Input 3
13
abcde
sdaklfj
asdjf
na
basdn
sdaklfj
asdjf
na
asdjf
na
basdn
sdaklfj
asdjf
5
abcde
sdaklfj
asdjf
na
basdn

Sample Output 3:
1
3
4
3
2
"""
"""
input tests:
arraystrings = ['def', 'de', 'fgh']
arrayqueries = ['de', 'lmn', 'fgh']
"""


def matchingStrings(strings, queries):
    arr = []
    for i in queries:
        counter = 0
        for j in strings:
            if len(i) == len(j):
                if i in j:
                    counter += 1
        arr.append(counter)
    return arr


if __name__ == '__main__':
    strings_count = int(input())
    strings = []
    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    print('\n'.join(map(str, res)))
