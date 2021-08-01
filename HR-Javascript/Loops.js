// https://www.hackerrank.com/challenges/js10-loops/problem



/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {

    // hint: we can use a string and check with .includes()
    // hint - you have to declare arrays prior to invoking them.

    var vowels = [];
    var nonvowels = [];

    // go through entire string line by line
    // fill vowels and nonvowel variables
    for (let i = 0; i < s.length; i++) {
        let letter = s[i];
        // pick out vowels and add to array
        if ( 'aeiou'.includes(letter) ){
            vowels.push(s[i]);
        } else {
            nonvowels.push(letter);
        }
    }

    // console.log(vowels) // <-- uncomment to double check

    // console.log(nonvowels) // <-- uncomment to double check

    // now go through vowels and nonvoewels line by line and print to console
    for (let i =0; i < vowels.length; i++){
        console.log(vowels[i]);
    }
    // and do the same for non-vowels, which should have a different length
    for (let i =0; i < nonvowels.length; i++){
        console.log(nonvowels[i]);
    }

}
