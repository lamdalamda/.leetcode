#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        

        total_width=len(words[0])
        chosen_index=1

        thisline=words[0]
        
        while chosen_index<len(words):
            if total_width+len(words[chosen_index])+chosen_index<=maxWidth:
                # chosen_index here = number of spaces
                total_width+=len(words[chosen_index])

                chosen_index+=1
                
            else:
                break
        
        if chosen_index==len(words):
            # this will be the lastline
            thisline=""
            for i in range(0,len(words)):
                thisline=thisline+words[i]+" "
                
            if len(thisline)==maxWidth+1:
                return [thisline[0:maxWidth]]
            
            return [thisline+" "*(maxWidth-len(thisline))]
        if chosen_index==1:
            return [words[0]+" "*(maxWidth-len(words[0]))]+self.fullJustify(words[1:],maxWidth) 
        
        
        else:
            
            # chosen_index=3 -> space=2
            space=int((maxWidth-total_width)/(chosen_index-1))
            
            extra_one_space_until=(maxWidth-total_width)%(chosen_index-1)
            thisline=""
            for i in range(0,extra_one_space_until):
                thisline=thisline+words[i]+" "*(space+1)
            for i in range(extra_one_space_until,chosen_index-1):
                thisline=thisline+words[i]+" "*space
                
            thisline+=words[chosen_index-1]
            
            return [thisline]+self.fullJustify(words[chosen_index:],maxWidth) 
        
# @lc code=end

