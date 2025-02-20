'''
problem: <
examples:

[[0]]

scenarios

reverse the array

01 10
10 01

input: 2d array of 1 and 0s
work: flip horiz and invert
output: array itself

ideas:

reverse every list
invert every number


'''
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        '''
        [[1,0],[0,1]]
                i
        '''
        def flipHoriz(image):
            for row in image:
                row.reverse()

        def invert(image):
            for row in image:
                for i in range(len(row)):
                    if row[i] == 0:
                        row[i] = 1
                    else:
                        row[i] = 0

        flipHoriz(image)
        invert(image)
        return image
        