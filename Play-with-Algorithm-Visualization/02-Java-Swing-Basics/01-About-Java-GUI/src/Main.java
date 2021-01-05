import javax.swing.*;
import java.awt.*;

public class Main {

    public static void main(String[] args) {
        // EventQueue 属于awt 事件对象管理，放进java事件分发线程，gui越来越大防止线程错误。
        EventQueue.invokeLater(() -> {
            // JFrame窗口对象，来自swing包
            JFrame frame = new JFrame("Welcome");
            frame.setSize(500, 500);
            // 设置窗口不可被更改大小
            frame.setResizable(false);
            // 默认是隐藏窗口，设置为点叉子关闭
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            // 设置窗口可视化
            frame.setVisible(true);
        });
    }
}
