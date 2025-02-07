
# this is a greedy problem for the following reasons:

# we're looking to optimize something -> smallest lexographic on repeating char sequence in order

# we're makeing a decision at every step where we can safely do something without regret -> are we adding the current char to the output stack?

# if the final solution were not using this local choice, could i exchange some piece of it with my local choice and get something at least as good or better, without harming the rest of the solution?

def removeDuplicates(s: str):
    stack = []
    seen = set()

    # map to store the count of each char
    count = {
        char: s.count(char) for char in s
        }

    for char in s:
        # decrement the count of the char because we're curretnly using it
        count[char] -= 1
        #  if we've already seen the char, we can skip it
        if char in seen:
            continue
        # if the current char is smaller than the last char in the stack and the last char in the stack is still present in the string, we can safely remove it from the stack
        while stack and char < stack[-1] and count[stack[-1]] > 0:
            seen.remove(stack.pop())
        # add the current char to the stack and mark it as seen
        stack.append(char)
        seen.add(char)

    return "".join(stack)

print(removeDuplicates("bbaavbs"))