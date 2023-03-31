def calc(arr):
    # list of operators
    opList = ["X", "/", "+", "-"]

    # list of numbers
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # value for final calculation
    result = 0

    # index of array for looping
    index = 0

    # current value to apply operand to with the result
    # this will allow multiple digit operations
    current = ""

    # checks if the last value was an operator
    lastOp = False

    # loop through the array
    while index < len(arr) - 1:

        # adds the first number to the result
        if arr[index] not in opList:
            while index < len(arr) and arr[index] in nums:
                if not lastOp:
                    current += arr[index]
                else:
                    current = arr[index]
                    lastOp = False

                index += 1

            result += int(current)
        
        # handles multiplication
        elif arr[index] == "X":
            lastOp = True
            index += 1

            # adds every numerical digit before multiplying
            while index < len(arr) and arr[index] in nums:
                if not lastOp:
                    current += arr[index]
                else:
                    current = arr[index]
                    lastOp = False

                index += 1

            result *= int(current)

        # handles division
        elif arr[index] == "/":
            lastOp = True
            index += 1

            # adds every numerical digit before dividing
            while index < len(arr) and arr[index] in nums:
                if not lastOp:
                    current += arr[index]
                else:
                    current = arr[index]
                    lastOp = False

                index += 1

            result /= int(current)

        # handles addition
        elif arr[index] == "+":
            lastOp = True
            index += 1

            # adds every numerical digit before adding
            while index < len(arr) and arr[index] in nums:
                if not lastOp:
                    current += arr[index]
                else:
                    current = arr[index]
                    lastOp = False
                index += 1

            result += int(current)

        # handles subtraction
        elif arr[index] == "-":
            lastOp = True
            index += 1

            # adds every numerical digit before subtracting
            while index < len(arr) and arr[index] in nums:
                if not lastOp:
                    current += arr[index]
                else: 
                    current = arr[index]
                    lastOp = False
                index += 1

            result -= int(current)

    return result