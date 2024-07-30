def sum_container(container):
    if isinstance(container, dict):
        # For dictionaries, sum the values
        return sum(container.values())
    elif isinstance(container, (list, tuple, set)):
        # For lists, tuples, and sets, sum the items directly
        return sum(container)
    else:
        # Print an error message if the container type is unsupported
        raise TypeError(f"Unsupported container type: {type(container)}")
    
    

    # Calculate the sum of the elements in the list [10, 20, 30] using the 'sum' function and store it in the variable 's'

# Print a message indicating the sum of the container and display the value of 's'
print("\nSum of the container: ",sum_container([10, 20, 30]))

