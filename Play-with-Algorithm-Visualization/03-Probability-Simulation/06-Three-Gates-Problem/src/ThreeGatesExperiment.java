
public class ThreeGatesExperiment {

    private int N;

    public ThreeGatesExperiment(int N){

        if(N <= 0)
            throw new IllegalArgumentException("N must be larger than 0!");

        this.N = N;
    }

    public void run(boolean changeDoor){

        int wins = 0;
        for(int i = 0 ; i < N ; i ++)
            // 换门还是不换门
            if(play(changeDoor))
                // 是否中奖
                wins ++;

        System.out.println(changeDoor ? "Change" : "Not Change");
        System.out.println("winning rate: " + (double)wins/N);
    }

    private boolean play(boolean changeDoor){

        // Door 0, 1, 2
        int prizeDoor = (int)(Math.random() * 3);
        int playerChoice = (int)(Math.random() * 3);

        if( playerChoice == prizeDoor)
            // 最初的选择是正确的，一旦换门会导致失败
            return changeDoor ? false : true;
        else
            // 最初的选择是错误的，一旦换门会成功
            return changeDoor ? true : false;
    }

    public static void main(String[] args) {

        int N = 10000000;
        ThreeGatesExperiment exp = new ThreeGatesExperiment(N);

        exp.run(true);
        System.out.println();
        exp.run(false);
    }
}
