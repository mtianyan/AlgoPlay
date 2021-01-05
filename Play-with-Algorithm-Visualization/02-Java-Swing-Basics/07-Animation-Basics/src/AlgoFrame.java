import java.awt.Graphics2D;
import java.awt.Graphics;
import java.awt.Dimension;
import java.awt.Color;
import java.awt.RenderingHints;

import javax.swing.*;

public class AlgoFrame extends JFrame {

    private int canvasWidth;
    private int canvasHeight;
    private JPanel canvas;

    public AlgoFrame(String title, int canvasWidth, int canvasHeight) {

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

    public AlgoFrame(String title) {

        this(title, 1024, 768);
    }

    public int getCanvasWidth() {
        return canvasWidth;
    }

    public int getCanvasHeight() {
        return canvasHeight;
    }

    // 绘制所需的圆的坐标data
    private Circle[] circles;

    // 绘制
    public void render(Circle[] circles) {
        this.circles = circles;
        // repaint是JFrame提供的函数，作用就是将JFrame中的所有控件刷新一遍。
        // 这就包含了对于AlgoCanvas进行一次刷新，这就会清空canvas，然后重新调用paintComponent方法。
        // 这是内置的清空，刷新。
        repaint();
    }

    private class AlgoCanvas extends JPanel {

        public AlgoCanvas() {
            // 双缓存
            super(true);
        }

        @Override
        public void paintComponent(Graphics g) {
            super.paintComponent(g);

            Graphics2D g2d = (Graphics2D) g;

            // 抗锯齿
            RenderingHints hints = new RenderingHints(
                    RenderingHints.KEY_ANTIALIASING,
                    RenderingHints.VALUE_ANTIALIAS_ON);
            hints.put(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY);
            g2d.addRenderingHints(hints);

            // 具体绘制
            AlgoVisHelper.setStrokeWidth(g2d, 1);
            AlgoVisHelper.setColor(g2d, Color.RED);
            for (int i = 0; i < circles.length; i++) {
                // TODO: 圆与圆之间的碰撞检测
                AlgoVisHelper.fillCircle(g2d, circles[i].x, circles[i].y, circles[i].getR());
            }
        }

        @Override
        public Dimension getPreferredSize() {
            return new Dimension(canvasWidth, canvasHeight);
        }
    }
}


