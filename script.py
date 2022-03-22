import hashlib, os, shutil

debug = True
runtime = True
leniency = 5


def addExtraSpaces(file):
    with open(file, "a") as file:
        file.write(2*"\n")

def copy(src, dest):
    shutil.copy(src, dest)

def convert_hash(first_file, second_file):
    index, endConditionMet = 0, False

    while not endConditionMet:
        firstHash, secondHash = hash_file(first_file), hash_file(second_file)
        index += 1
        
        if debug:
            print(">> First Message Hash: " + firstHash)
            print(">> Second Message Hash: " + secondHash)
            print(">> Current Index: " + str(index))
            print("\n")

        if firstHash[-leniency:] != secondHash[-leniency:]:
            addExtraSpaces(second_file)
        else:
            print(">> End condition met after " + str(index) + " iterations.")
            endConditionMet = True

def delete(file):
    os.remove(file)

def hash_file(file):
    # make a hash object
   h = hashlib.sha256()

   # open file for reading in binary mode
   with open(file,'rb') as file:
       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

src, dest = "confession_fake.txt", "confession_fake_copy.txt"
target = "confession_real.txt"

# Make a copy of the file before we run, so we don't have to replace it every time.
copy(src, dest)

if debug:
    print(">> First Hash: " + hash_file(dest))
    print(">> Second Hash: " + hash_file(target))

if runtime:

    # Perform the hash attack by convering dest file to have a similar hash to target
    convert_hash(target, dest)

    # Delete the dest file afterwards.
    delete(dest)
