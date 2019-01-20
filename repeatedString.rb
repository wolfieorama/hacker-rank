# Complete the repeatedString function below.
def repeatedString(s, n)

    def repeatedString(s, n)
        a_count = 0
        a_1 = 0
        a_2 = 0
        m, r = n.divmod(s.length)
    
        if s == "a"
            a_count = n
            return a_count
        else
            s.each_char do |a|
                if a == "a"
                    a_1 += 1
                end
            end
    
            s_2 = s[0...r]
            s_2.each_char do |a|
                if a == "a"
                    a_2 += 1
                end
            end
    
            a_count = (a_1 * m) + a_2
            return a_count
        end 
    end
end

puts repeatedString("abc", 10)