
public class Circle {

    public int x;
    public int y;
    private int r;

    public int vx; // x方向上速度
    public int vy;

    public Circle(int x, int y, int r, int vx, int vy){
        this.x = x;
        this.y = y;
        this.r = r;
        this.vx = vx;
        this.vy = vy;
    }

    public int getR(){return r;}

    // 圆心坐标移动，圆移动。
    public void move(int minx, int miny, int maxx, int maxy){
        x += vx;
        y += vy;

        checkCollision(minx, miny, maxx, maxy);
    }

    private void checkCollision(int minx, int miny, int maxx, int maxy){

        // 碰到左边缘，速度反转
        if(x - r < minx) { x = r;        vx = -vx; }
        if(x + r >= maxx){ x = maxx - r; vx = -vx; }
        if(y - r < miny) { y = r;        vy = -vy; }
        if(y + r >= maxy){ y = maxy - r; vy = -vy; }
    }

}
