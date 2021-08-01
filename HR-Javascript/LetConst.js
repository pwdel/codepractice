// https://www.hackerrank.com/challenges/js10-let-and-const/problem


function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    // declare Pi
    const PI = Math.PI
    // read r as input
    let r = readLine();
    // compute area
    let area = Math.pow(r,2)*PI;
    // Print the area of the circle:
    console.log(area)
    // compute perimeter
    let perimeter = 2*PI*r;
    // Print the perimeter of the circle:
    console.log(perimeter)

    try {
        // Attempt to redefine the value of constant variable PI
        PI = 0;
        // Attempt to print the value of PI
        console.log(PI);
    } catch(error) {
        console.error("You correctly declared 'PI' as a constant.");
    }
}
