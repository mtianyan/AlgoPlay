class LinearSearch {
    static search: <T>(arr: T[], target: T)=>number= function(arr ,target) {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] === target) {
                return i;
            }
        }
        return -1;
    }
}


const testList: number[] = [24, 18, 12, 9, 16, 66, 32, 4];
console.log(LinearSearch.search<number>(testList, 16))
console.log(LinearSearch.search<number>(testList, 666))