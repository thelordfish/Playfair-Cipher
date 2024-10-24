
ciphertext = "You are jilted at the altar. Shoot her entire side of the family. Shoot to kill."
key="deceptive"
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def first_filter(text):
    if text != None:
        result = "".join([i for i in text if i.isalpha()]).upper()
    else:
        print("No value given")
        return False        
    return result


def remove_dupl_key(key):
    result=[]
    for i in key:
        if i not in result:
            result.append(i)
    return result


def remove_duple_alph(newkey, alphabet):
    result=[]
    for i in alphabet:
        if i not in newkey:
            result.append(i)
    return result

def join_ij(thing):
    result = []
    foundij = False
    for letter in thing:
        if letter not in "IJ":
            result.append(letter)
        elif foundij == False:
            result.append("IJ")
            foundij = True
    return result

        
def full_key(key, alphabet):
    filteredkey = first_filter(key)
    newkey = remove_dupl_key(filteredkey)
    newalph = remove_duple_alph(newkey, alphabet)
    newkey.extend(newalph)
    fullkey = join_ij(newkey)
    return fullkey

def make_matrix(full_key):
    matrix = [[full_key[row*5 + column] for column in range(5)] for row in range(5)]
    return matrix

matrixkey = [make_matrix(full_key(key,alphabet))[i] for i in range(5)]
print("\n\n Here is the matrix displayed on many lines:")
[print(make_matrix(full_key(key,alphabet))[i]) for i in range(5)]

def formatted_ciphertext(ctext):
    ctext = first_filter(ctext).replace("J","I")
    result = ""
    i=0
    while i < len(ctext):
        if i+1 < len(ctext):
            if ctext[i] == ctext[i+1]:
                result += ctext[i] + "X"
                i +=1
            else:
                result += ctext[i] + ctext[i+1]
                i+=2
        else:
            result += ctext[i] + "X"
            i+=1
    return result
   

def separated_ciphertext(ciphertext):
    separated_cipher = [[ciphertext[row*2 + column] for column in range(2)] for row in range(int(len(ciphertext)/2))]
    return separated_cipher

finalctext = separated_ciphertext(formatted_ciphertext(ciphertext))
print(f"\n\n Here is the final formatted cipher text (finalctext) {finalctext}")


def find_coordinates(a, k):
    location = None
    for i, row in enumerate(k):
        for j, column in enumerate(k):
            if a in k[i][j]:
                alocation = i, j
    return alocation


def same_row(a, b, k):
    for row in k:
        if a in row and b in row:
            return True
    return False


def same_column(a, b, k):
   #extract coordinates:
   alocation = find_coordinates(a, k)
   blocation = find_coordinates(b, k)
   #check if their column is the same
   if alocation[1] == blocation[1]:
        return True
   else:
        return False
   
# def test_functions(matrixkey):
#     print(matrixkey)
#     a = input("First Letter:")
#     b = input("Second Letter:")
#     input("Same_column")
#     print(same_column(a, b, matrixkey))
#     input("Same row:")
#     print(same_row(a, b, matrixkey))

# test_functions(matrixkey)
             
def re_coordinate(a, b, k):
    ax,ay = find_coordinates(a, k)
    bx,by = find_coordinates(b, k)
    newa = k[ax][by]
    newb = k[bx][ay]
    return newa, newb

def shift_left(a, b, k):
    ax,ay = find_coordinates(a, k)
    bx,by = find_coordinates(b, k)
  
  #clever bit of modulo maths to make the coordinate wrap around if it goes below 0 when shifting left
    neway = (ay-2) % 5
    newby = (by-2) % 5

    newa = k[ax][neway]
    newb = k[bx][newby]
    return newa, newb

def shift_down(a, b, k):
    ax,ay = find_coordinates(a, k)
    bx,by = find_coordinates(b, k)
    if ax + 2 > 4:
        ax=ax-3
    else:
        ax +=2
    if bx + 2 > 4:
        bx=bx-3
    else:
        bx+=2
    return k[ax][ay], k[bx][by]
    
    newa = k[ax][ay]
    newb = k[bx][by]
    return True


def encrypt(finalctext, matrixkey):
    pt = finalctext
    k = matrixkey
    output = []
    for i in range(len(pt)):
        a = pt[i][0]
        b = pt[i][1]
        if same_row(a, b, k):
            output += shift_left(a, b, k)
        if same_column(a, b, k):
            output += shift_down(a, b, k)
        else:
            output += re_coordinate(a, b, k)
    return output

encryption = "".join(encrypt(finalctext, matrixkey))

print(f"\n \n Here is the encryption: {encryption}")









