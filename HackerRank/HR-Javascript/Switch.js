// https://www.hackerrank.com/challenges/js10-switch/problem
// input s is a string of letters
// adfgt
// the first letter
// use sets, can check if in a set with:
// console.log(setX.has("whatever"));

// note - you don't have to use fancy sets
// you can just use the string operator .includes
// hint - the "switch(input)" just has to be a variable
// You can hypothetically just feed in switch(true) to execute



function getLetter(s) {
    let letter;
    // feed true into switch to execute
    // use .includes method on string to evaluate
    switch (true) {
        case 'aeiou'.includes(s[0]):
            letter = 'A';
            break;
        case 'bcdfg'.includes(s[0]):
            letter = 'B';
            break;
        case 'hjklm'.includes(s[0]):
            letter = 'C';
            break;
        case 'npqrstvwxyz'.includes(s[0]):
            letter = 'D';
            break;
    }
    return letter;
}
