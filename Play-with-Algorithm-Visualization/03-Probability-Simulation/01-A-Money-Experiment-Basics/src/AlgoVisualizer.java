import java.awt.*;

public class AlgoVisualizer {

    private static int DELAY = 10;
    private int[] money;
    private AlgoFrame frame;

    public AlgoVisualizer(int sceneWidth, int sceneHeight){

        // 初始化数据,初始时都有100块钱
        money = new int[100];
        for(int i = 0 ; i < money.length ; i ++)
            money[i] = 100;

        // 初始化视图
        EventQueue.invokeLater(() -> {
            frame = new AlgoFrame("Money Problem", sceneWidth, sceneHeight);
            new Thread(() -> {
                run();
            }).start();
        });
    }

    public void run(){

        // 动画逻辑
        while(true){

            // 绘制当前money数组，然后停留40ms,1000/40 25帧
            frame.render(money);
            AlgoVisHelper.pause(DELAY);

            for(int i = 0 ; i < money.length; i ++){
                // 每一个人都不能欠钱
                if(money[i] > 0){
                    // 从0-money.length 前闭后开的区间
                    int j = (int)(Math.random() * money.length);
                    money[i] -= 1;
                    money[j] += 1;
                }
            }
        }
    }

    public static void main(String[] args) {

        int sceneWidth = 1000;
        int sceneHeight = 800;

        AlgoVisualizer vis = new AlgoVisualizer(sceneWidth, sceneHeight);
    }
}