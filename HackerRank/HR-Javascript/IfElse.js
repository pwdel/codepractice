// https://www.hackerrank.com/challenges/js10-if-else/problem

// hint - using multiple conditionals works differently than in python.


function getGrade(score) {
    let grade;
    // Write your code here
    if(score <=5){
        grade = 'F';
    } else if(score <= 10){
        grade = 'E';
    } else if(score <= 15){
        grade = 'D';
    } else if(score <= 20){
        grade = 'C';
    } else if(score <= 25){
        grade = 'B';
    } else
        grade = 'A';

    return grade;
}


function main() {
    const score = +(readLine());

    console.log(getGrade(score));
}
