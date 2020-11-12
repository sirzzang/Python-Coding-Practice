def solution(numbers):
    sort_order = {'0':0, ' ':1, '1':2, '2':3, '3':4, '4':5,
                  '5':6, '6':7, '7':8, '8':9, '9':10}
    numbers = [str(number) for number in numbers]
    new_numbers = [number.ljust(6) for number in numbers]
    new_numbers.sort(reverse=True, key=lambda x: (sort_order[x[0]], sort_order[x[1]], sort_order[x[2]], sort_order[x[3]], sort_order[x[4]], sort_order[x[5]]))
    new_numbers = [number.strip(' ') for number in new_numbers]
    return ''.join(new_numbers)

if __name__ == '__main__':
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))