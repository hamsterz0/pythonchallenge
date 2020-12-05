import urllib.request

def main():
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    number = '12345'
    iters = 400
    while iters:
        new_url = url + number
        req = urllib.request.Request(new_url)
        with urllib.request.urlopen(req) as response:
            res = response.read().decode('utf-8')
            print(res)
            number = res.split(" ")[-1]
        iters -= 1

main()
