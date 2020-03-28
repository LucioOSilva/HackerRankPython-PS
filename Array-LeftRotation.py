"""
A left rotation operation on an array of size "n" shifts each of the array's elements 1 unit to the left. For example,
if "2" left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

Given an array of "n" integers and a number, "d", perform "d" left rotations on the array. Then print the updated array
as a single line of space-separated integers.

Input Format:
The first line contains two space-separated integers denoting the respective values of  (the number of integers) and  (the number of left rotations you must perform).
The second line contains  space-separated integers describing the respective elements of the array's initial state.

Constraints:
1 <= n <= 10**5
1 <= d <= n
1 <= ai <= 10**6

Output Format:
Print a single line of "n" space-separated integers denoting the final state of the array after performing
left rotations.

Sample Input:
5 4
1 2 3 4 5

Sample Output:
5 1 2 3 4

Explanation:

When we perform "d=4" left rotations, the array undergoes the following sequence of changes:
    [1,2,3,4,5] => [2,3,4,5,1] => [3,4,5,1,2] => [4,5,1,2,3] => [5,1,2,3,4]
Thus, we print the array's final state as a single line of space-separated values, which is "5 1 2 3 4".
"""


def arr_left_rot(arr, numrot):
    for _ in range(numrot):
        arr.insert(len(arr), (arr[0]))
        arr.pop(0)
    return arr


if __name__ == '__main__':
    nd = input().split()
    try:
        n = int(nd[0])
        d = int(nd[1])
    except (ValueError, TypeError) as error:
        print('An error occurred', {error})
    else:
        arr = list(map(int, input().rstrip().split()))
        if n == len(arr):
            larr = arr_left_rot(arr, d)
            for i in larr:
                print(i, end=' ')
        else:
            print("The number of elements are different of array's lenght")





"""
def leftrotation(array, turn):
    for k,v in array:
        if k+turn <= len(array):
                
"""
