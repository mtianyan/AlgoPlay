import java.awt.*;
import javax.swing.*;

public class AlgoFrame extends JFrame{

    private int canvasWidth;
    private int canvasHeight;

    public AlgoFrame(String title, int canvasWidth, int canvasHeight){

        // 调用父类的title，继承的JFrame构造函数原本该实现的
        super(title);

        this.canvasWidth = canvasWidth;
        this.canvasHeight = canvasHeight;

        setSize(canvasWidth, canvasHeight);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);

        setVisible(true);
    }

    public AlgoFrame(String title){

        this(title, 1024, 768);
    }

    public int getCanvasWidth(){return canvasWidth;}
    public int getCanvasHeight(){return canvasHeight;}
}
