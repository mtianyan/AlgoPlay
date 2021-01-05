package cn.mtianyan;

/**
 * 我们的第六版Union-Find
 */
public class UnionFind6 implements UF {

    private int[] parent;
    private int[] rank;   // rank[i]表示以i为根的集合所表示的树的层数

    /**
     * 构造函数
     *
     * @param size
     */
    public UnionFind6(int size) {

        parent = new int[size];
        rank = new int[size];

        // 初始化, 每一个parent[i]指向自己, 表示每一个元素自己自成一个集合
        for (int i = 0; i < size; i++) {
            parent[i] = i;
            rank[i] = 1;
        }

    }

    @Override
    public int getSize() {
        return parent.length;
    }

    /**
     * 查找过程, 查找元素p所对应的集合编号 O(h)复杂度, h为树的高度
     *
     * @param p
     * @return
     */
    private int find(int p) {
        if (p < 0 || p >= parent.length)
            throw new IllegalArgumentException("p is out of bound.");

        // 不断去查询自己的父亲节点, 直到到达根节点
        // 根节点的特点: parent[p] == p
//        while(p != parent[p]){
//            parent[p] = parent[parent[p]];
//            p = parent[p]; // 不断上移，直到指向自己
//        }
//        return p;
        // path compression 2, 递归算法
        if (p != parent[p])
            parent[p] = find(parent[p]); // 让根节点来做p节点的父亲
        return parent[p]; // 返回整棵树的根节点
    }

    /**
     * 查看元素p和元素q是否所属一个集合 O(h)复杂度, h为树的高度
     *
     * @param p
     * @param q
     * @return
     */
    @Override
    public boolean isConnected(int p, int q) {
        return find(p) == find(q);
    }


    /**
     * 合并元素p和元素q所属的集 O(h)复杂度, h为树的高度
     *
     * @param p
     * @param q
     */
    @Override
    public void unionElements(int p, int q) {

        int pRoot = find(p);
        int qRoot = find(q);

        if (pRoot == qRoot)
            return;

        // 根据两个元素所在树的rank不同判断合并方向
        // 将rank低的集合合并到rank高的集合上
        if (rank[pRoot] < rank[qRoot])
            parent[pRoot] = qRoot; // 合并以后，上限没变
        else if (rank[qRoot] < rank[pRoot])
            parent[qRoot] = pRoot;
        else { // rank[pRoot] == rank[qRoot]
            parent[pRoot] = qRoot;
            rank[qRoot] += 1;   // 此时 才需要维护rank的值
        }
    }
}