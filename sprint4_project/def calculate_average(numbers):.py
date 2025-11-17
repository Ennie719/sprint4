def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numerical values.

    Returns:
        float: The average of the numbers, or None if the list is empty.
    """
    if not numbers:  # Check if the list is empty
        return None
    return sum(numbers) / len(numbers)