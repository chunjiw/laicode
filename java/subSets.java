// Given a set of characters represented by a String, return a list containing all subsets of the characters.

// Assumptions

// There are no duplicate characters in the original set.
// ​Examples

// Set = "abc", all the subsets are [“”, “a”, “ab”, “abc”, “ac”, “b”, “bc”, “c”]
// Set = "", all the subsets are [""]
// Set = null, all the subsets are []


public class Solution {
  public List<String> subSets(String set) {
    // Write your solution here.
    List<String> result = new ArrayList<String>();
    if (set == null) {
      return result;
    }
    StringBuilder sb = new StringBuilder();
    subset(set, 0, sb, result);    
    return result;
  }
  
  private void subset(String set, int index, StringBuilder solution, List<String> result) {
    if (index == set.length()) {
      result.add(solution.toString());
    } else {
      subset(set, index + 1, solution, result);
      solution.append(set.charAt(index));
      subset(set, index + 1, solution, result);
      solution.deleteCharAt(solution.length() - 1);
    }
  }
}
