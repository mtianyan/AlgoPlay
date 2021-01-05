import java.awt.*;
import javax.swing.*;
import java.awt.geom.Ellipse2D;

public class AlgoFrame extends JFrame{

    private int canvasWidth;
    private int canvasHeight;

    public AlgoFrame(String title, int canvasWidth, int canvasHeight){

        super(title);

        this.canvasWidth = canvasWidth;
        this.canvasHeight = canvasHeight;

        AlgoCanvas canvas = new AlgoCanvas();
        setContentPane(canvas);
        pack();

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);

        setVisible(true);
    }

    public AlgoFrame(String title){

        this(title, 1024, 768);
    }

    public int getCanvasWidth(){return canvasWidth;}
    public int getCanvasHeight(){return canvasHeight;}


    private class AlgoCanvas extends JPanel{

        @Override
        public void paintComponent(Graphics g) {
            super.paintComponent(g);

            // 转换为Graphics2D进行绘制
            Graphics2D g2d = (Graphics2D)g;

            int strokeWidth = 5;
            g2d.setStroke(new BasicStroke(strokeWidth, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND));


            g2d.setColor(Color.RED);
            // 浮点数性能高，但是double可以省去转换
            Ellipse2D circle = new Ellipse2D.Double(50, 50, 300, 300);
            g2d.draw(circle);

            // 基于状态的绘图直到改变颜色状态
            g2d.setColor(Color.BLUE);
            Ellipse2D circle2 = new Ellipse2D.Double(50, 50, 300, 300);
            g2d.fill(circle2);
        }

        @Override
        public Dimension getPreferredSize(){
            return new Dimension(canvasWidth, canvasHeight);
        }
    }
}

