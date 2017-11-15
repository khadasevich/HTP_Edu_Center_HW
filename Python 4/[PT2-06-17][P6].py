import os

def my_wrapper(dir):
    for d, dirs, files in dir:
        for f in files:
            path = os.path.join(d, f)
            yield path

files_lazy_lister = my_wrapper(os.walk('/home/alex/'))
list(files_lazy_lister)


# Extra option. Works faster.
def pathes_genereator(directory):
    for d, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(d, f)
            yield path


def return_of_path(gener, direct):
    gen_obj = gener(direct)
    try:
        while True:
            print next(gen_obj)
    except StopIteration:
        pass

return_of_path(pathes_genereator, '/home/alex')