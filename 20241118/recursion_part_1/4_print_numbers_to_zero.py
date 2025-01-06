def call_me(times):
    # Base case
    if times == 0:
        return
    
    # Print the word "call"
    print("call")
    
    # Recursive call with times - 1
    call_me(times - 1)

# Example usage
call_me(5)