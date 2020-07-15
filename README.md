# substring-frequency
Given a pattern as the first argument and a string of blobs split by "|" show the number of times the pattern is present in each blob and the total number of matches. 

Input:
The input consists of the pattern ("bc" in the example) which is separated by a semicolon followed by a list of blobs ("bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32" in the example). Example input: bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32

Output:
The output should consist of the number of occurrences of the pattern per blob (separated by |). Additionally, the final entry should be the summation of all the occurrences (also separated by |).

Example output: 3|2|1|2|8 where 'bc' was repeated 3 times, 2 times, 1 time, 2 times in the 4 blobs passed in. And 8 is the summation of all the occurrences (3+2+1+2 = 8)
