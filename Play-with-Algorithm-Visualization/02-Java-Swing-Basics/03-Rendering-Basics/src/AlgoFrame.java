import java.awt.*;
import javax.swing.*;


public class AlgoFrame extends JFrame {


    private int canvasWidth;
    private int canvasHeight;

    public AlgoFrame(String title, int canvasWidth, int canvasHeight){

        // 调用父类的title，继承的JFrame构造函数原本该实现的
        super(title);

        this.canvasWidth = canvasWidth;
        this.canvasHeight = canvasHeight;

        //setSize(canvasWidth, canvasHeight);
        AlgoCanvas canvas = new AlgoCanvas();

        // canvas 内部已经通过覆盖getPreferredSize设置了画布大小，此时则可以不用设置了
        // canvas.setPreferredSize(new Dimension(canvasWidth,canvasHeight));
        setContentPane(canvas);

        // 使用pack方法自动根据扔进容器里的组件，扩展大小
        pack();

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);

        setVisible(true);

        // System.out.println(getContentPane().getBounds());
    }

    public AlgoFrame(String title){

        this(title, 1024, 768);
    }

    public int getCanvasWidth(){return canvasWidth;}
    public int getCanvasHeight(){return canvasHeight;}


    private class AlgoCanvas extends JPanel{

        @Override
        public void paintComponent(Graphics g) {
            // g是此时的一个上下文环境，会被不断的传入
            super.paintComponent(g);

            // 屏幕坐标系，以50，50为左上角，300*300的正方形为包围的圆
            g.drawOval(50, 50, 300, 300);
        }

        @Override
        public Dimension getPreferredSize(){
            return new Dimension(canvasWidth, canvasHeight);
        }
    }
}

