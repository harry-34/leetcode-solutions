class Solution {
    public boolean isPalindrome(int x) {
        // Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if (x < 0 || (x % 10 == 0 && x != 0)) return false;
        
        int reversedHalf = 0;
        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }
        
        // x == reversedHalf handles even-length numbers (e.g., 1221)
        // x == reversedHalf / 10 handles odd-length numbers (e.g., 121, middle digit doesn't matter)
        return x == reversedHalf || x == reversedHalf / 10;
    }
}