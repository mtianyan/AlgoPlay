class LinearSearch {
    static search = function (arr: number[], target: number): number {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] === target) {
                return i;
            }
        }
        return -1;
    }
}


const testList: number[] = [24, 18, 12, 9, 16, 66, 32, 4];
console.log(LinearSearch.search(testList, 16))
console.log(LinearSearch.search(testList, 666))