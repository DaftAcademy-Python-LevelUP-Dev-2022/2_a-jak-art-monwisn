def greeter(func):
    def wrapper(*args, **kwargs):
        return f"Aloha {func(*args, *kwargs).title()}"

    return wrapper

 
def sums_of_str_elements_are_equal(func):
    def wrapper(self):
        numbers = func(self).split(' ')
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
            return f'{sum1} == {sum2}'
        else:
            return f'{sum1} != {sum2}'

    return wrapper


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            return func()

        setattr(klass, func.__name__, inner_wrapper)
        return inner_wrapper

    return outer_wrapper
