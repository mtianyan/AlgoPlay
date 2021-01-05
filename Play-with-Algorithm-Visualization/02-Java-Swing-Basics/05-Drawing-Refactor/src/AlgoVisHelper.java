import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;

public class AlgoVisHelper {

    // 不需要也不能实例化类，类的方法都是静态公有方法，这是工具类的通用做法。
    // 例如math类，不用被实例化，只需要math.method
    private AlgoVisHelper(){}

    public static void strokeCircle(Graphics2D g, int x, int y, int r){

        Ellipse2D circle = new Ellipse2D.Double(x-r, y-r, 2*r, 2*r);
        g.draw(circle);
    }

    public static void fillCircle(Graphics2D g, int x, int y, int r){

        // 传入的数学坐标系，圆心位置被转换为左上角；即x，y整体上移一个半径。
        Ellipse2D circle = new Ellipse2D.Double(x-r, y-r, 2*r, 2*r);
        g.fill(circle);
    }

    public static void setColor(Graphics2D g, Color color){
        g.setColor(color);
    }

    public static void setStrokeWidth(Graphics2D g, int w){
        int strokeWidth = w;
        //  CAP_ROUND 绘制线条的端点是圆形的。JOIN_ROUND 拐弯是平滑的圆形。
        g.setStroke(new BasicStroke(strokeWidth, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND));
    }
}
