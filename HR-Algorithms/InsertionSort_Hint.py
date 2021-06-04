    def insertionSort1(n, arr):
        # Write your code here
        # n appears to be the length of the vector
        # original last value
        value = arr[n-1]
        # stop flag
        flag=0
        for i in range(0,len(arr)):
            print('---------')
            print('i=',i)
            # checkpoint, work backwards
            c = len(arr)-i-2
            print('c=',c)
            print('start arr: ',arr)
            # if last vector arr[n-1]
            if value < arr[c] and flag == 0:
                # check if value < c
                print('v < arr@c=',c)
                # special case - we're at c=-1, the end
                if c==-1:
                  # set the first index to value
                  print('setting the first index to value!')
                  arr[0]=value
                else:
                  # move the value at c to the right
                  print('moving value to the right!')
                  arr[c+1]=arr[c]
                # display arr
                print(*arr)
            elif value > arr[c] and flag == 0:
                # check if value > c
                print('v > arr@c=',c)
                print('current c pointer value:',arr[c])
                # put the original value in location to right and stop
                arr[c+1]=value
                # stop flag, if not through with list yet
                if i<len(arr):
                    flag=1
                    print('stop flag set!')
                    print('stop point i=',i)
                    print('stop point c=',c)
                else:
                    flag=0
                # print it out
                print (*arr)
            # case where stopflag has occured, don't do anything
            elif flag == 1:
                # do nothing
                pass

    if __name__ == '__main__':
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        insertionSort1(n, arr)
