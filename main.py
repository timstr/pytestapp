import pytestlib
import pytestlib.operations as ops


def main():
    arr = pytestlib.make_array()
    print(arr)
    arr = ops.sort(arr)
    print(arr)
    arr = ops.reverse(arr)
    print(arr)


if __name__ == "__main__":
    main()
