'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:
The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
'''

class Encoder:
    # prepend every word with its length followed by a delimiter `;` (example, happy becomes -> 5;happy)
    def encode(self, strs: list) -> str:
        encoded_string = ''
        for s in strs:
            l = len(s)
            encoded_string += (str(l) + ';')
            encoded_string += s
        return encoded_string

    def decode(self, encoded_string: str) -> list:
        decoded_strings = []
        i = 0
        while i < len(encoded_string):
            j = i
            while encoded_string[j] != ';': j += 1
            l = int(encoded_string[i:j])
            i = j+l+1
            decoded_strings.append(encoded_string[j+1:i])
        return decoded_strings

if __name__ == '__main__':
    stringEncoder = Encoder()
    
    # encode
    encoded_string = stringEncoder.encode(['leet','code'])
    print(encoded_string) # 4;leet4;code

    # decode
    decoded_strings = stringEncoder.decode(encoded_string)
    print(decoded_strings) # ['leet', 'code']

