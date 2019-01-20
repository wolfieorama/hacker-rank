# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# For example, there are
# socks with colors . There is one pair of color and one of color . There are three odd socks left, one of each color. The number of pairs is

# .

# Function Description

# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

# sockMerchant has the following parameter(s):

#     n: the number of socks in the pile
#     ar: the colors of each sock

# Input Format

# The first line contains an integer
# , the number of socks represented in .
# The second line contains space-separated integers describing the colors

# of the socks in the pile.

# Constraints

# 1 <= n <= 100
# 1 <= ar[i] <= 100 where 0<= 1 <= n

# Output Format

# Print the total number of matching pairs of socks that John can sell.

# require 'json'
# require 'stringio'
require 'set'

# Complete the sockMerchant function below.
def sockMerchant(n, ar)
    s = Set.new
    pair_count = 0 
    for i in 0..n
        if s.include? ar[i]
            pair_count += 1
            s.delete(ar[i])
        else
            s << ar[i]
        end
    end

    return pair_count
end


puts sockMerchant(9, [10,20,20,10,10,30,50,10,20,30])