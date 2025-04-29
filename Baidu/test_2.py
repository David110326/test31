#Hello world
import os

print("Start test********************************hello world")
print("hello world")
print("hello world hello world")


def set_field(field_name,setvalue):
    field_name_map={
        '2_1':('dropdown','we are'),
        '3_1':('dropdown','he is')
    }
    field_def=field_name_map[field_name]
    if field_def[0]=='dropdown':
        print(field_def[1])
        print(setvalue)

if __name__ == '__main__':
    set_field("2_1","A")