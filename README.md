# bakery

## Task:
Given a customer order you are required to determine the cost and pack breakdown for each product.
To save on shipping space each order should contain the minimal number of packs.

## Input:
Each order has a series of lines with each line containing the number of items followed by the
product code. An example input:

* 10 VS5
* 14 MB11
* 13 CF

## Output:

A successfully passing test(s) that demonstrates the following output:
* 10 VS5 $17.98
  - 2 x 5 $8.99
* 14 MB11 $54.8
  - 1 x 8 $24.95
  - 3 x 2 $9.95
* 13 CF $25.85
  - x 5 $9.95
  - 1 x 3 $5.95
