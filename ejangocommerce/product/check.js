function longestNonRepeatingSubstr(str) {
    let subStr = '';
    let strArr = [];

    for (let i = 0; i < str.length; i++) {
        let currectChar = str[i];

        if (subStr.includes(currectChar)) {
            strArr.push(subStr);
            subStr = currectChar;
        } else {
            subStr += currectChar;
        }

    }
    strArr.push(subStr);
    let maxLength = 0;
    let longestString = '';
    for (let i = 0; i <strArr.length; i++) {
        let currentVal = strArr[i];
        if (currentVal.length > maxLength) {
            longestString = currentVal;
        }
    }
    return longestString;
}

console.log(longestNonRepeatingSubstr('ABCDDDDEFGHIJ')); // Outputs: DEFGHIJ