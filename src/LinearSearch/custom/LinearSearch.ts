var _ = require('lodash');
class Student{
    name: string;

    constructor(name) {
        this.name = name;
    }
    [Symbol.toPrimitive](hint) {
        console.log("hint", hint)
        return this.name;
    }

}
Student.prototype.valueOf = function() {
    return this.name;
}
class LinearSearch {
    static search: <T>(arr: T[], target: T)=>number= function(arr ,target) {
        for (let i = 0; i < arr.length; i++) {
            if (_.isEqual(arr[i],target)) {
                return i;
            }
        }
        return -1;
    }
}


const testList: number[] = [24, 18, 12, 9, 16, 66, 32, 4];
console.log(LinearSearch.search<number>(testList, 16))
console.log(LinearSearch.search<number>(testList, 666))
const studentList: Student[] = [new Student('Alice'),new Student('mtianyan1'),new Student('mtianyan')]
const mtianyan = new Student('mtianyan')
console.log(LinearSearch.search<Student>(studentList, mtianyan))