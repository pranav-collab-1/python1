import java.util.scanner;

public class fcfs1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of processes: ");
        int n = scanner.nextInt();
        System.out.print("Enter arrival time for each process:");
        int[] arrivalTime = new int[n];
        for (int i = 0; i<n; i++) {
            arrivalTime[i] = scanner.nextInt();
        }
        System.out.print("Enter burst time for each process:");
        int[] burstTime = new int[n];
        for (int i = 0; i<n; i++) {
            burstTime[i] = scanner.nextInt();
        }
        int[] turnaroundTime = new int[n];
        int[] waitingTime = new int[n];
        int[] completionTime = new int[n];
        int totalTurnaroundTime = 0;
        int totalWaitingTime = 0;
        completionTime[0] = arrivalTime[0] + burstTime[0];
        turnaroundTime[0] = completionTime[0] - arrivalTime[0];
        waitingTime[0] = turnaroundTime[0] - burstTime[0];
        for (int i = 1; i<n; i++) {
            completionTime[i] = completionTime[i-1] + burstTime[i];
            turnaroundTime[i] = completionTime[i] - arrivalTime[i];
            waitingTime[i] = turnaroundTime[i] - burstTime[i];
        }
        for (int i = 0; i<n; i++) {
            totalTurnaroundTime += turnaroundTime[i];
            totalWaitingTime += waitingTime[i];
        }
        System.out.println("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time");
        for (int i = 0; i<n; i++) {
            System.out.println((i+1) + "\t" + arrivalTime[i] + "\t\t" + burstTime[i] + "\t\t" + completionTime[i] + "\t\t" + turnaroundTime[i] + "\t\t" + waitingTime[i]);
        }
        System.out.println("Total Turnaround Time: " + totalTurnaroundTime);
        System.out.println("Total Waiting Time: " + totalWaitingTime);
    }
}