# Let's look at the lowercase letters.
import string
string.ascii_lowercase

# We will consider the alphabet to be these letters, along with a space.
alphabet = string.ascii_lowercase + " "

# create `letters` here!
num = 0
letters = {}
for i in alphabet:
    letters[num] = i
    num += 1
    
alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

encryption_key = 3

# define `encoding` here!
encoding = {}
for i in range(27):
    encoding[alphabet[i]] = (encryption_key + i) % 27
    
message = "hi my name is caesar"

def caesar(message, encryption_key):
    # return the encoded message as a single string!
    res = ""
    for i in message:
        encoded_letter = letters[encoding[i]]
        res += encoded_letter
    return res    
coded_message = caesar(message, 3)
print(coded_message)
        
decoded_message = caesar(coded_message, -3)
print(decoded_message)
