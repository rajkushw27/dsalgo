def arrayOfProducts(array):

    product = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    rightRunningProduct = 1

    for i in range(len(array)):
        product[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    for i in reversed(range(len(array))):
        product[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

        return product
