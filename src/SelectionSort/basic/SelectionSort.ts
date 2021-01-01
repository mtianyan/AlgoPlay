class SelectionSort{
    static sort = function (arr: number[]): number[] {
        for (let i = 0; i < arr.length; i++){
            let min_index = i;
            for(let j=i+1; j<arr.length; j++){
                if(arr[j] < arr[min_index]){
                    min_index = j;
                }
            }
            [arr[i], arr[min_index]] = [arr[min_index], arr[i]];
        }
        return arr;
    }

}

const testList: number[] = [1, 4, 2, 3, 6, 5];
console.log(SelectionSort.sort(testList))