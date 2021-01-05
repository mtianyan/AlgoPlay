
public class WinningPrize {

    private double chance;
    private int playTime;
    private int N;

    public WinningPrize(double chance, int playTime, int N){

        if(chance < 0.0 || chance > 1.0)
            throw new IllegalArgumentException("chance must be between 0 and 1!");

        if(playTime <= 0 || N <= 0)
            throw new IllegalArgumentException("playTime or N must be larger than 0!");

        this.chance = chance;
        this.playTime = playTime;
        this.N = N;
    }

    public void run(){
        // 模拟运行

        int wins = 0;
        for(int i = 0 ; i < N ; i ++)
            if(play())
                wins ++;

        System.out.println("winning rate: " + (double)wins/N);
    }

    private boolean play(){
        for(int i = 0 ; i < playTime ; i ++)
            // 从0-1前闭后开之间均匀的数，小于0.2 的概率是20% chance为1时，if语句一定为true
            if(Math.random() < chance)
                return true;
        return false;
    }

    public static void main(String[] args) {

        double chance = 0.2;
        int playTime = 5;
        // 蒙特卡罗次数，每次开五个宝箱
        int N = 1000000;

        WinningPrize exp = new WinningPrize(chance, playTime, N);
        exp.run();
    }
}
