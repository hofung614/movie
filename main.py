movies = open("movie.txt").read().split("\n")
print("movie list:\n")
for i,j in enumerate(movies,1):
    print("\t%d. %s" % (i, j))
print()

def selection():
    try:
        s = int(input("please select movie by number: "))-1
        if s < 0 or s > len(movies):
            raise
        print("selected [%s]"%(movies[s]))
        return s
    except:
        print("invalid input, please try again")
        selection()

def seat():
    try:
        s = input("please input seat number: ").lower()
        if not 0 < int(s[1:]) < 13 and len(s) == 2 and s[0] in "abcd":
            raise
        if seats[ord(s[0])-97][-int(s[1:])]:
            print("seat is occupied, please try again")
            seat()
        else:
            print("selected [%s]"%(s))
            seats[ord(s[0])-97][-int(s[1:])] = 1
    except:
        print("invalid input, please try again")
        seat()


n = selection()
f = open("seat.txt").read().split("\n")
seats = [list(map(int,i))for i in zip(*[f"{int(j,16):04b}"for j in f[n]])]
print("\n   12 11 10 9  8  7  6  5  4  3  2  1")
for i,j in enumerate(seats,97):
    print(chr(i),*["▢▣"[i]for i in j],sep="  ")
print()
print(f"{'▢ available':>52}")
print(f"{'▣ occupied ':>52}")
seat()
f[n] = "".join("{:x}".format(int("".join(map(str,i)),2))for i in zip(*seats))
seats = open("seat.txt","w")
seats.write("\n".join(f))
seats.close()
