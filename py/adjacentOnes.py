# https://www.coursera.org/learn/algorithms-part2
# Depth-first search (DFS)
# Breadth-first search (BFS)

def get_number_of_islands(binaryMatrix):
  pass # your code goes here


# visit(binaryMatrix, 0, 3)
def visit(binaryMatrix, i, j):
  # if position i,j == 0 then, move on false
  # if position i,j == 1 then, move right, down, left, right
  # increase counter
  # i,j *= 0
  if binaryMatrix[i, j] == 0:
    return false
  else:
    print("we got 1")
    binaryMatrix[i,j] = 0
    if binaryMatrix[i, j+1] == 1:
      visit(binarymatrix, i, j + 1);
    
    if binaryMatrix[i, j+1] == 1:
      print("we got 1")
      binMatrix[i,j+1] *= 0