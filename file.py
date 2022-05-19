def greeter(func):
    def wrapper(*args, **kwargs):
        return f"Aloha {func(*args, *kwargs).title()}"

    return wrapper

 
def sums_of_str_elements_are_equal(func):
    def wrapper(*args):
        numbers = func(*args).split(' ')
        list_of_nums = []

        for number in numbers:
            if number[0] == '-':
                nums = [-int(n) for n in number[1:]]
            else:
                nums = [int(n) for n in number[:]]

            list_of_nums.append(nums)

        sum1 = sum(list_of_nums[0])
        sum2 = sum(list_of_nums[1])

        if sum1 == sum2:
            print(f'{sum1} == {sum2}')
        else:
            print(f'{sum1} != {sum2}')

    return wrapper()


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
