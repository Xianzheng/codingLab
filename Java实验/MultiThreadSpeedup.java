import java.util.concurrent.CountDownLatch;

public class MultiThreadSpeedup {
    static final int N = 100000000;

    public static void main(String[] args) throws InterruptedException {
        long start = System.currentTimeMillis();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = N - i;
        }

        // 单线程排序
        CountDownLatch latch = new CountDownLatch(1);
        new Thread(() -> {
            sort(arr, 0, N - 1);
            latch.countDown();
        }).start();
        latch.await();
        long end = System.currentTimeMillis();
        System.out.println("Single thread elapsed time: " + (end - start) + " ms");

        // 多线程排序
        start = System.currentTimeMillis();
        int m = N / 2;
        CountDownLatch latch2 = new CountDownLatch(2);
        new Thread(() -> {
            sort(arr, 0, m - 1);
            latch2.countDown();
        }).start();
        new Thread(() -> {
            sort(arr, m, N - 1);
            latch2.countDown();
        }).start();
        latch2.await();
        end = System.currentTimeMillis();
        System.out.println("Multi-thread elapsed time: " + (end - start) + " ms");
    }

    static void sort(int[] arr, int l, int r) {
        if (l >= r) {
            return;
        }
        int i = l, j = r;
        int pivot = arr[(l + r) / 2];
        while (i <= j) {
            while (arr[i] < pivot) {
                i++;
            }
            while (arr[j] > pivot) {
                j--;
            }
            if (i <= j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
        }
        sort(arr, l, j);
        sort(arr, i, r);
    }
}
