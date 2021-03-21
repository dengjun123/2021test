
# def a():
#     print("before")
#     print("a")
#     print("after")


# def enhance(func):
#     print("before")
#     func()
#     print("after")

def tmp(func):
    def wapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")
    return wapper
@tmp
def a(a1):
    print("a")



if __name__ == "__main__":
    a(20)
