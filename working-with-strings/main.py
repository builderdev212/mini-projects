def String_Slicer(string):
    string = str(string)
    arr = []
    for char in string:
        arr.append(str(char))
    return arr

def Find_Char(char, string):
    match_arr = []
    string = str(string)
    sliced_string = String_Slicer(string)
    for cr in sliced_string:
        if cr == char:
            match_arr.append(str(cr))
    return match_arr

def Arr_to_String(arr):
    string = ''
    for char in arr:
        string += str(char)
    return string

def Help():
    print('String slicer cuts any string into a array.')
    print('Find char finnds any char in a string, then returns an array of the matched characters.')
    print('Arr to string takes an array and turns it into a string.')
    print('Examples:')
    print('String_Slicer example...')
    st = 'fun'
    sliced = String_Slicer(st)
    print(st, sliced)
    print('Find_Char example...')
    chr = 'e'
    string = 'enter'
    sliced_char = Find_Char(chr, string)
    print(chr, string, sliced_char)
    print('Arr_to_String example...')
    array = ['p','r','i','n','t']
    a_s = Arr_to_String(array)
    print(array, a_s)

if __name__ == '__main__':
    Help()
