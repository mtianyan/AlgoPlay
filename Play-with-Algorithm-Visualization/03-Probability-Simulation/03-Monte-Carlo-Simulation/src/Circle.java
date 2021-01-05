import java.awt.*;

public class Circle {

    private int x, y, r;

    public Circle(int x, int y, int r){
        this.x = x;
        this.y = y;
        this.r = r;
    }

    public int getX(){ return x; }
    public int getY(){ return y; }
    public int getR(){ return r; }

    // 点是否在圆内
    public boolean contain(Point p){
        // 点p.x值与圆心x 的差平方
        return Math.pow(p.x - x, 2) + Math.pow(p.y - y, 2) <= r*r;
    }
}
