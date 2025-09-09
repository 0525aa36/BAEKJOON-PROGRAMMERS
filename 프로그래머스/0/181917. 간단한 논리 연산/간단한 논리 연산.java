class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean answer = true;
        if((x1 == true || x2 == true) && (x3 == true || x4 == true)){
            answer = true;
        } else {
            answer = false;
        }
        return answer;
    }
}